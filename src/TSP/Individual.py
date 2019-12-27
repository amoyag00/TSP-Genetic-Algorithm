# -*- coding: utf-8 -*-
"""
@author: Alejandro Moya García
"""
from random import shuffle

class Individual:
    
    def __init__(self, cities):
        self.cities = cities.copy()
        shuffle(self.cities)
    
    """
    Deep copy of the individual
    """
    def clone(self):
        copy = Individual(self.cities)
        copy.cities = []
        for city in self.cities:
            copy.cities.append(city)
        return copy
    

    def setCities(self, cities):
        self.cities = cities
        
    
    """
    Calculates the distance of path
    """
    def calcFitness(self):
        distance = 0.0
        for i in range(0,len(self.cities)-1):
            distance += self.cities[i].distanceTo(self.cities[i+1])
        distance += self.cities[-1].distanceTo(self.cities[0])
        self.fitness= distance
        
        
    def getFitness(self):
        return self.fitness
    
    
    def isFitterThan(self, other):
        return self.fitness < other.fitness
        
    def __str__(self):
        string = "["
        for city in self.cities:
            string += str(city.id) +", "
        string = string [:-2]+"]"
        return string
    