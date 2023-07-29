#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class BaseLOLOutOfBounds(Exception):
    """
    The input exceeded the boundaries of Base-LOL
    """
    def __init__(self, position):
        self.message = f'The given position >>{position}<< is out of bounds.'
        super().__init__(self.message)


class BaseLOLQueryNotEven(Exception):
    """
    The input is not an even list
    """
    def __init__(self):
        self.message = 'The query is not even. Double check the input.'
        super().__init__(self.message)


class EnumAnyWrongInput(Exception):
    """
    The input is not a list, dict or tuple
    """
    def __init__(self):
        self.message = 'Wrong Input. Make sure it is a list, dict or tuple.'
        super().__init__(self.message)
