#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import argparse


class DebugHelper:
    def __init__(self):
        self.parse = argparse.ArgumentParser()
        self.parse.add_argument(
            '--debug',
            action='store_true'
        )
        self.args = self.parse.parse_args()

    def debug_mode(self, anything):
        if self.args.debug:
            print(anything)
