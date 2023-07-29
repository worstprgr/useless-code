#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from stringchaos.core import exceptions as exc
from stringchaos.res import big_dict
from stringchaos.debughelper.debughelper import DebugHelper

d = DebugHelper()


class Useless:
    def __init__(self):
        self.reg_l = big_dict.register_l_dict
        self.reg_u = big_dict.register_u_dict
        self.reg_s = big_dict.register_s_dict
        self.concat_reg = {**self.reg_l, **self.reg_u, **self.reg_s}

    def query(self, query: str) -> str:
        """
        Prepares the query for the Base-LOL decoder:
            1. If there's white space -> remove it
            2. Convert it to upper case
            3. Convert it to a list
            4. Check if the query is even
            5. Make pairs of two characters
            6. Decode it and return
        :param query: str as Base-LOL
        :return: str as ASCII
        """
        query = query.strip()

        if ' ' in query:
            query = query.replace(' ', '')

        query = list(query.upper())
        step = 2

        def list_to_pairs() -> str:
            _list = []
            for x in range(0, len(query), step):
                split = query[x:x + step]
                split = ''.join(split)
                _list.append(split)
            out = self._baseLOL_decode(_list)
            return out

        if (len(query) % 2) == 0:
            result = list_to_pairs()
            d.debug_mode(result)
            return result
        else:
            raise exc.BaseLOLQueryNotEven

    def _baseLOL_decode(self, _list: list) -> str:
        """
        Decodes a Base-LOL query to ASCII.
        :param _list: list with the Base-LOL content
        :return: str
        """
        _temp = []
        for x in _list:
            _temp.append(self.concat_reg[x])
        result = ''.join(_temp)
        return result
