#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 14:42:27 2020

@author: michael
"""

class Thing:
    
    name = ''
    
    description = ''
    
    noticability = .5
    
    health = 1
    
    current_location = ''
    
    composition = []
    
    def describe(self, detail):
        print(self.description)
        
        
        