'''
Author: Akshaya Niraula
Create Time: 2021-10-14 20:08:58
Copyright: Copyright (c) 2021 Akshaya Niraula. See LICENSE for details
'''

import unittest
import logging


class TestOfwBase(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s.%(msecs)03d %(levelname)s [%(filename)s]:\t%(message)s",
            datefmt="%d %H:%M:%S",
        )
