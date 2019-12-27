# -*- coding: utf-8 -*-
"""
@author: Alejandro Moya García
"""
import random

class Mutation:
    
    """
    Swaps 2 random genes
    """
    def swap(genes):
        index1, index2 = random.sample(range(len(genes)),2)
        genes[index1], genes[index2] = genes[index2], genes[index1]
        return genes
    
    
        