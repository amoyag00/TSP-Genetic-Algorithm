# -*- coding: utf-8 -*-
"""
@author: Alejandro Moya García
"""
import random

class Crossover:
        
    """
    Creates two children using Partially Mapped Crossover algorithm
    """
    def PMX(parent1, parent2):
        size = len(parent1)
        child1 = [None] * size
        child2 = [None] * size
        
        # Select random crosspoints
        crossPoint1 = random.randint(0, size-1)
        crossPoint2 = random.randint(crossPoint1+1,size)
        
        # Copy gene segments from parents
        for i in range(crossPoint1, crossPoint2):
            child1[i] = parent1[i]
            child2[i] = parent2[i]
        
        # Copy genes from the other parent segment that have not been copied yet
        for i in range(crossPoint1, crossPoint2):
            if parent2[i] not in child1:
                index = Crossover.findSlot(i, parent2, child1)
                child1[index] = parent2[i]
                
            if parent1[i] not in child2:
                index = Crossover.findSlot(i, parent1, child2)
                child2[index] = parent1[i]
        
        # Fill children with the genes not present in the segment
        for i in range(0, crossPoint1):
            if child1[i] is None:
                child1[i] = parent2[i]
            if child2[i] is None:
                child2[i] = parent1[i]
                
        for i in range(crossPoint2, size):
            if child1[i] is None:
                child1[i] = parent2[i]
            if child2[i] is None:
                child2[i] = parent1[i]        
        
        children = [child1, child2]
        return children
        
    
    
    # Find a free position for the gene      
    def findSlot(index, parent, child):
        if(child[index] is None):
            return index
        else:
            return Crossover.findSlot(parent.index(child[index]), parent, child)
           
            