<#
* @ Author: Akshaya Niraula
* @ Create Time: 2021-11-14 07:14:31
* @ Modified by: Akshaya Niraula
* @ Modified time: 2021-11-15 01:33:46
* @ Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
#>


# Run this file to build and publish

# this are the arguments passed in
param($build, $publish, $copyTypings, $publishToProd)

# branches map to be build
# The key of the map MUST be the Branches of assembly--crawler project
# The value of the map WILL be the Directory name of PYOFW (current project)
$branchesToLocalDirMap = @{
  "main"     = "pyOFW";
  "WTRG1035" = "pyOFW1035";
}

# Environment variables to be loaded
$script:assemblyCrawlerDir = "" 
$script:pypiUsername = ""
$script:pypiPassword = ""

# package Dir
$packageName = "pyOFW"
$script:packageDir = Join-Path $PWD "src" $packageName
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
  return $version
}

function Copy-Branches {
  Import-Env
  
  Set-Location $script:assemblyCrawlerDir

  foreach ($map in $branchesToLocalDirMap.GetEnumerator()) {
    git checkout $map.Key
    $sourceDir = Join-Path $assemblyCrawlerDir "typings"
    $targetDir = Join-Path $script:typingsDir $map.Value

    # remove the existing folder
    Remove-Item -Force -Recurse $targetDir
    Write-Host "Removed the local contents: $targetDir" -ForegroundColor Magenta

    Write-Host "[$($map.Key)] About to copy typings contents from: $sourceDir" -ForegroundColor DarkBlue
    Copy-Item -Force -Recurse -Path $sourceDir -Destination $targetDir
    Remove-Item -Force -Recurse -Path (Join-Path $targetDir "TestAssemblyNET48")
    Write-Host "[$($map.Key)] Copied contents to $targetDir" -ForegroundColor DarkGreen
  }

  Set-Location $script:currentWorkingDir
  Write-Host "Done copying branches" -ForegroundColor DarkGreen
}
function New-Build {
  # Check if the current directory has setup.py file
  $setupPyPath = Join-Path -Path $PWD -ChildPath  "setup.py"

  if (-not (Test-Path $setupPyPath)) {
    throw "No setup.py file detected at this location: {$PWD} "
  }

  if ($copyTypings -eq "True") {
    Copy-Branches
  }
  else {
    Write-Host "Skipped copying typings" -ForegroundColor Red
  }

  # Make sure to work from current project dir
  Set-Location $script:currentWorkingDir
  Write-Host "CWD = $($script:currentWorkingDir)" -ForegroundColor DarkBlue

  Write-Host "BUILD: Perform cleaning" -ForegroundColor DarkBlue
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