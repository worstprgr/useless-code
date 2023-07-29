#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import socket
import random
import string
from stringchaos.core import exceptions as exc
from stringchaos.core.baselol import BaseLOL
from stringchaos.debughelper.debughelper import DebugHelper

d = DebugHelper()


class Utils:
    def __init__(self):
        self.blol = BaseLOL()
        self.seed = 3537133769733142071383
        self.ab = string.ascii_lowercase
        self.s_chars = ' !?&*+-#_.,;:'

    def bigd_gen_static(self, range_max: int) -> None:
        """
        Generate the content for the static big_dict.py dictionary
        :param range_max: the upper boundary for the Base-LOL locator
        :return: None
        """
        for x in range(range_max):
            o = self.blol.baseLOL_locator(x)
            dict_build = f"\t'{o}': '',"
            print(dict_build)

    def bigd_gen_upper(self, prev_dict: dict) -> dict:
        """
        Creates a dict with upper case letters, based on the
        dict, with the lower case letters
        :param prev_dict: dict with lower case letters
        :return: dict -> {<BASE_LOL>: <upper case letters>}
        """
        _list = self._dictval_to_list(prev_dict)
        _dict = {}
        length = len(_list)
        counter = 0
        offset = 1
        min_range = length
        max_range = min_range * 2
        min_range += offset
        max_range += offset

        for x in range(min_range, max_range):
            o = self.blol.baseLOL_locator(x)
            _dict.update({o: _list[counter].upper()})
            counter += 1
        return _dict

    def bigd_gen_special(self, prev_dicts: [dict]) -> dict:
        """
        Creates a dict with special characters, defined in the class constructor
        :param prev_dicts: previous dict, for calculating the new boundaries for the Base-LOL locator
        :return: dict -> {<BASE_LOL>: <special characters>}
        """
        _dict = {}
        special_c_list = list(self.s_chars)
        len_special_c_list = len(special_c_list)
        len_prev_dicts = self.lenof_dicts(prev_dicts)
        counter = 0
        offset = 1
        min_range = len_prev_dicts
        max_range = len_special_c_list + min_range
        min_range += offset
        max_range += offset

        for x in range(min_range, max_range):
            o = self.blol.baseLOL_locator(x)
            _dict.update({o: special_c_list[counter]})
            counter += 1
        return _dict

    def missing_register(self) -> list:
        """
        Some letters where missing in the initial dict,
        so I'm adding the missing ones
        :return: list
        """
        return self.entropy(self.ab)

    def entropy(self, low_e: str) -> list:
        """
        Shuffles the order of a list.
        :param low_e: list to shuffle
        :return: list with higher entropy
        """
        random.seed(self.seed)
        high_e = []
        rand_int_list = [x for x in range(0, len(low_e))]
        random.shuffle(rand_int_list)

        for x in rand_int_list:
            high_e.append(low_e[x])
        return high_e

    @staticmethod
    def lenof_dicts(dicts_list: list):
        """
        calculates the total length of multiple dicts.
        :param dicts_list: multiple dicts in a list
        :return: int
        """
        total_dict_len = 0
        for x in dicts_list:
            total_dict_len += len(x.keys())
        return total_dict_len

    @staticmethod
    def lookup_hostname(ip_addr: str) -> str or None:
        """
        Gets the hostname of a server, based on the ip address.
        :param ip_addr: str -> IP address, without port
        :return: str -> hostname
        """
        try:
            hostname = socket.gethostbyaddr(ip_addr)[0].lower()
            d.debug_mode(hostname)
            return hostname
        except socket.herror:
            d.debug_mode('Hostname not found')
            return None

    @staticmethod
    def enum_any(ldt: list or dict or tuple) -> None:
        """
        Simple enumerator for lists, dicts and tuples
        :param ldt: list, dict or tuple
        :return: None
        """
        if type(ldt) is list:
            for x in ldt:
                print(x)
        elif type(ldt) is dict:
            for x in ldt.keys():
                print(f'{x}: {ldt[x]}')
        elif type(ldt) is tuple:
            for x in ldt:
                print(x)
        else:
            raise exc.EnumAnyWrongInput

    @staticmethod
    def _dictval_to_list(this_dict: dict) -> list:
        """
        Converts a dict to a list, but drops the keys.
        :param this_dict: A dict you want to convert
        :return: list
        """
        _list = []
        for x in this_dict.values():
            _list.append(x)
        return _list
