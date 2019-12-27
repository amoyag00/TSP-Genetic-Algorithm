# -*- coding: utf-8 -*-
"""
@author: Alejandro Moya García
"""
from math import hypot

class Distance:
    
    """
    Calculates the euclidean distance
    """    
    def euclideanDist(x1, x2, y1, y2):
        return hypot(x2-x1, y2-y1)