#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
This is a custom implementation of (how I name it) Base-LOL.
It's base 3 with ascii letters. Those are the rules:
    1. Only two characters
    2. The first character uses ascii letters
    3. The second character are only digits from 0-2

So it's limited to 3*26=78 possibilities to store data.

Why? Because this is useless code!
"""
import string
from stringchaos.core import exceptions as exc
from stringchaos.debughelper.debughelper import DebugHelper

d = DebugHelper()


class BaseLOL:
    def __init__(self):
        # all 26 ascii letters
        self.ascii_u = string.ascii_uppercase

        # digits from 0 - 2
        self.digits = string.digits[:3]

    def baseLOL_locator(self, position: int) -> str:
        """
        This method returns an entry from the **Base-LOL** register, based on the position you query.

        The Base-LOL implementation contains two characters. The first character
        represents a **letter** and the second one represents a **digit**.

        letter = **first_char**
        digit = **second_char**

        It loops from 0 to the given position. Beginning with counting up the **second_char**.
        If the **second_char** equals the last digit from **self.digits**, the **first_char** jumps
        one position higher, to the next letter, inside **self.ascii_u**.
        :param position: int
        :return: str -> two characters
        """
        if position >= self._boundary():
            raise exc.BaseLOLOutOfBounds(position)

        first_char = self.ascii_u
        second_char = self.digits
        counter_a = 0
        counter_b = 0
        a = first_char[counter_a]
        b = second_char[counter_b]

        for x in range(position):
            counter_b += 1
            if b == self.digits[-1]:
                counter_a += 1
                counter_b = 0
            a = first_char[counter_a]
            b = second_char[counter_b]

        out = a + b
        return out

    def _boundary(self):
        boundary = len(self.ascii_u) * len(self.digits)
        return boundary
