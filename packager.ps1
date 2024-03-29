<#
* @ Author: Akshaya Niraula
* @ Create Time: 2021-11-14 07:14:31
* @ Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
#>


# Run this file to build and publish
#
#
####################################################################################
#
#                       Read this before building python package
#
####################################################################################
# Make sure:
# To sync assembly-crawler on web (GitHub) <<< IMPORTANT (Make sure the checkout contents)
# To update the version number in setup.py <<< IMPORTANT
# To update the Water version in src\pyofw\tool\cmd.py <<< IMPORTANT
# To copy the right branch from GitHub, scroll down and update $branchesToLocalDirMap  <<< IMPORTANT
# To update the MANIFEST.in, if any new file [types] are added
# To run the tests - all test should pass
# From debug tab (Ctrl + Shift + D), select the right option to build/publish.
# ----------------------------------------------------------------------------------
# NO need to run this file directly!
# -----------------------------------------------------------------------------------
#
#
#
#
#
####################################################################################
#
#                       Root Files/Directories in the project
#
####################################################################################
#
# .github:          This file is generated by github. Could contain CI/CD stuff
# .vscode:          This file is generated by VSCode
# build:            This directory is generated by python packager
# dist:             this directory is generated by python packager. Contains wheel and tar.gz
# example:          This directory contains some examples on using pyofw
# misc:             This directory contains images for .MD files and other misc items
# notebook:         This directory contains the Jupyter Notebook files, (supplement to examples)
# src:              This director contains the main source code, typings etc
# testsLocal:       This directory contains the tests of src files
# .env:             This file is not synced contains sensitive information
# .gitignore:       This file contains information to be ignored during sync
# copy_to_site_package.py:   This file directly copies from src to Site_packages module dir
# LICENSE:          This file contains the license information
# MANIFEST:         This file is generated by python packager
# MANIFEST.in:      This file contains the logic for MANIFEST contents
# packager.psi:     This file helps prepare and build, plus publish the package
# README.md:        This file contains the readme content
# requirements.txt: This file contains the requirements for the package
# setup.cfg:        This file contains the configuration
# setup.py:         this file helps to build the python package
# -----------------------------------------------------------------------------------


####################################################################################
#
#                       Build a Package (For Testing)
#
####################################################################################
# From Run and Debug (Ctrl + Shift + D), Select: PS: Build Copy Typing
# Push the green triangle to run
# If everying runs smoothly
# Crate Virtual environment for testing the installer
## Open your terminal and navigate to the directory where you want to create the virtual environment
## python -m venv pyofwInstallEnv
# Activating the Virtual Environment:
## pyofwInstallEnv\Scripts\activate
# Install the package build to this environment for testing
## from the given virtual environment, pip install "path/to/the/wheel.whl"


# these are the arguments passed in
param($build, $publish, $copyTypings, $publishToProd)

# Stop the execution of the code on any error
$ErrorActionPreference = "Stop"

# branches map to be build
# The key of the map MUST be the Branches of assembly--crawler project (by Kris, not the forked one)
# The value of the map WILL be the Directory name of PYOFW (current project)
$branchesToLocalDirMap = @{
  "main"     = "pyofw";
  "WTRG1035" = "pyofw1035";
  "WTRG1036" = "pyofw1036";
  "WTRG1040" = "pyofw1040";
}

# Environment variables to be loaded
$script:assemblyCrawlerDir = "" 
$script:pypiUsername = ""
$script:pypiPassword = ""

# package Dir
$packageName = "pyofw"
$script:packageDir = Join-Path $PWD (Join-Path "src" $packageName)
$script:typingsDir = Join-Path $packageDir "typings"

# Cache the current working directory
$script:currentWorkingDir = $PWD

function Import-Env {
  Write-Host "About to load the env variables from .env file" -ForegroundColor DarkBlue

  $localEnvFile = Join-Path $PWD ".\.env"
  if (-not(Test-Path $localEnvFile)) {
    throw "The .env file could not be located. Exited."
  }

  # Path of the .env file
  $content = Get-Content $localEnvFile -ErrorAction Stop

  #load the content to environment
  foreach ($line in $content) {
    if ($line.StartsWith("#")) { continue };
    if ($line.Trim()) {
      $line = $line.Replace("`"", "")
      $kvp = $line -split "=", 2
      [Environment]::SetEnvironmentVariable($kvp[0].Trim(), $kvp[1].Trim(), "Process") | Out-Null
    }
  }

  $script:assemblyCrawlerDir = $env:ASSEMBLY_CRAWLER_DIR
  $script:pypiUsername = $env:PYPI_USERNAME
  $script:pypiPassword = $env:PYPI_PASSWORD

  $errorMessage = "Environment variable shouldn't be blank: "
  if ([string]::IsNullOrEmpty($script:assemblyCrawlerDir)) { throw $errorMessage + "assemblyCrawlerDir" }
  if ([string]::IsNullOrEmpty($script:pypiUsername)) { throw $errorMessage + "pypiUsername" }
  if ([string]::IsNullOrEmpty($script:pypiPassword)) { throw $errorMessage + "pypiPassword" }

  Write-Host "Got the env variables" -ForegroundColor DarkGreen
}

function Get-Version {
  $setup_filepath = Join-Path $PSScriptRoot "setup.py"
  if (!(Test-Path $setup_filepath)) {
    Write-Host "setup.py could not be located. Returning." -ForegroundColor DarkRed
    return -1
  }

  $match = Get-Content $setup_filepath | Select-String -Pattern 'package_version = "(.*)"'
  $version = $match.Matches.Groups[1].Value
  Write-Host "Version: $version" -ForegroundColor Gray
  return $version
}

function Test-CopyStatus {
  param (
    [string]$SourcePath,
    [string]$TargetPath
  )

  # Recursively list all items in the source and target directories
  $sourceItems = Get-ChildItem -Path $SourcePath -File -Recurse
  $targetItems = Get-ChildItem -Path $TargetPath -File -Recurse

  # Compare the two lists of items
  $differences = Compare-Object -ReferenceObject $sourceItems -DifferenceObject $targetItems -Property FullName

  if ($differences.Count -eq 0) {
    Write-Host "All files and folders have been successfully copied." -ForegroundColor DarkGreen
  }
  else {
    $notCopiedItems = $differences | ForEach-Object {
      $_.InputObject.FullName
    }
    Write-Error "Some files or folders were not copied:`r`n$($notCopiedItems -join "`r`n")"
  }
}

function Copy-Branches {
  Write-Host "-------------- START COPYING BRANCHES --------------" -ForegroundColor DarkGray

  
  Set-Location $script:assemblyCrawlerDir
  Write-Host "Working directory set to: $script:assemblyCrawlerDir" -ForegroundColor Magenta

  # Make sure the remote branches are crated to local repo
  git fetch

  foreach ($map in $branchesToLocalDirMap.GetEnumerator()) {
    Write-Host (("." * 30) + " $($map.Key) " + ("." * 30)) -ForegroundColor DarkGray

    git stash
    git checkout ($map.Key)
    Write-Host "Checked out $($map.Key)"
    
    $sourceDir = Join-Path $assemblyCrawlerDir "typings"
    $targetDir = Join-Path $script:typingsDir $map.Value
    Write-Host "Source Dir: $sourceDir"
    Write-Host "Target Dir: $targetDir"

    # remove the existing folder
    if (Test-Path $targetDir) {
      Remove-Item -Force -Recurse $targetDir
      Write-Host "Removed the local contents: $targetDir" -ForegroundColor Magenta
    }

    Write-Host "[$($map.Key)] About to copy typings contents from: $sourceDir" -ForegroundColor DarkBlue
    Copy-Item -Force -Recurse -Path $sourceDir -Destination $targetDir
    # Test-CopyStatus -SourcePath $sourceDir -TargetPath $targetDir
    
    Remove-Item -Force -Recurse -Path (Join-Path $targetDir "TestAssemblyNET48")
    Write-Host "[$($map.Key)] Copied contents to $targetDir" -ForegroundColor DarkGreen
    Write-Host ("." * 100) -ForegroundColor DarkGray
  }

  Set-Location $script:currentWorkingDir
  Write-Host "Working directory set back to: $script:assemblyCrawlerDir" -ForegroundColor Gray

  Write-Host "Done copying branches" -ForegroundColor DarkGreen
  Write-Host "-------------- x -------------- x -------------- x --------------" -ForegroundColor DarkGray
}

function Copy-StubFiles {
  Write-Host "-------------- START COPYING STUB FILES --------------" -ForegroundColor DarkGray

  $sourceDir = Join-Path $assemblyCrawlerDir "typings"
  $targetDir = Join-Path $script:typingsDir $map.Value
  Write-Host "Source Dir: $sourceDir"
  Write-Host "Target Dir: $targetDir"

}


function New-Build {
  Write-Host "About to start a new build" -ForegroundColor Green

  # Check if the current directory has setup.py file
  $setupPyPath = Join-Path -Path $PWD -ChildPath  "setup.py"

  if (-not (Test-Path $setupPyPath)) {
    throw "No setup.py file detected at this location: {$PWD} "
  }

  Import-Env  

  if ($copyTypings -eq "True") {
    Write-Host "Copy typings is true, So start copying..." -ForegroundColor Blue
    Copy-Branches
    #Copy-StubFiles
  }
  else {
    Write-Host "Skipped copying typings" -ForegroundColor Red
  }

  # Make sure to work from current project dir
  Set-Location $script:currentWorkingDir
  Write-Host "CWD = $($script:currentWorkingDir)" -ForegroundColor DarkBlue

  Write-Host "BUILD: Perform cleaning" -ForegroundColor DarkBlue

  # make sure setup.py exists
  if (-not(Test-Path .\setup.py)) {
    Write-Error "setup.py could not be located on root path"
  }
  python.exe .\setup.py clean --all

  Write-Host "BUILD: Creating..." -ForegroundColor DarkBlue
  python.exe .\setup.py bdist_wheel sdist
  Write-Host "BUILD: Done." -ForegroundColor DarkGreen
}

function Publish-Build {
  if (-not (Test-Path (Join-Path -Path $script:currentWorkingDir -ChildPath "build"))) {
    throw "build directory is not detected at this location: {$script:currentWorkingDir} "
  }

  # Import- username and password
  Import-Env

  # Make sure to work from current project dir
  Set-Location $script:currentWorkingDir
  Write-Host "CWD = $($script:currentWorkingDir)" -ForegroundColor DarkBlue

  $version = Get-Version

  # Make sure this action wasn't accidental
  $response = Read-Host "Are you sure to publish $version version to $publishToProd ? yes/no"
  if ($response -eq "yes") {
    Write-Host "PUBLISH [$version]: working..." -ForegroundColor DarkBlue
    
    if ($publishToProd -eq "pypi.org") {
      twine.exe upload dist/$version/*.whl -u $script:pypiUsername -p $script:pypiPassword --verbose
      Write-Host "PUBLISH [$version]: Done. Published to pypi.org" -ForegroundColor DarkGreen
    }
    else {
      twine.exe upload --repository testpypi dist/$version/*.whl -u $script:pypiUsername -p $script:pypiPassword --verbose
      Write-Host "PUBLISH [$version]: Done. Published to TEST.pypi.org" -ForegroundColor DarkGreen
    }
  }
  else {
    Write-Host "OK. Skipped." -ForegroundColor DarkYellow
  }
}

# Perform Build if selected
if ($build -eq "build") {
  New-Build
}


# Perform Publish if selected
if ($publish -eq "publish") {
  Publish-Build
}