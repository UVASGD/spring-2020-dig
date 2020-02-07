#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 23:15:18 2020

@author: michael
"""

class Location:
    
    name = ''
    description = ''
    things = []
    
    coordinates = (0, 0, 0)
    
    def describe(self):
        
        print(self.description)
        
        for thing in self.things:
            thing.describe()
        
    