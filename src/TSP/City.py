# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:36:33 2019

@author: Alex
"""

from CommonAlgorithms.Distance import Distance

class City:
    
    def __init__(self, id, x, y):
        self.id= id
        self.x=x
        self.y=y
        
        
    def __eq__(self, other):
        if other is None:
            return False
        else:
            return self.id == other.id
        
        
    def __str__(self):
        return self.id
    
    
    def distanceTo(self, otherCity):
        return Distance.euclideanDist(self.x, otherCity.x, self.y, otherCity.y)
        