#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from heuristics import Heuristics

class MyHeuristics(Heuristics):
    def __init__(self):
        super().__init__()
        self.patterns = {
                        'iiiii' : 100,
                        '_iiii_' : 30,
                        '_ii_ii_' : 20,
                        '_iii_' : 10,
                        '_ii_' : 5,
                        'ii_' : 2,
                        '_ii' : 2,
                        '__i__' : 1,
                        '1' : 1,
                        't' : -1
                         }