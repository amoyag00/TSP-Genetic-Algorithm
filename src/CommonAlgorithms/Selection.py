# -*- coding: utf-8 -*-
"""
@author: Alejandro Moya García
"""
import random

class Selection:
    
    """
    Performs a parent selection using tournament algorithm
    """
    def tournamentSelection(population, numParents, tournamentSize):
        matingPool = []
        populationCopy = population.copy()
        while(len(matingPool) < numParents):
            tournament = random.sample(populationCopy,tournamentSize)
            fittest = tournament[0]
            for individual in tournament:
                if(individual.isFitterThan(fittest)):
                    fittest = individual
            matingPool.append(fittest)
            populationCopy.remove(fittest)
        return matingPool
    
    
    """
    Guarantees the best n individuals from the previous generation are present
    in the new one if there is not better individual than them
    """
    def performElitism(currentGen, nextGen, elitism):
        currentGenCopy = currentGen.copy()
        for i in range(0, elitism):
            currentFittest = Selection.getFittest(currentGenCopy)
            offspringFittest = Selection.getFittest(nextGen)
            if(currentFittest.isFitterThan(offspringFittest)):
                nextGen.remove(Selection.getUnfittest(nextGen))
                nextGen.append(currentFittest)
                currentGenCopy.remove(currentFittest)
                
    """
    returns the fittest individual of the population
    """         
    def getFittest(population):
        fittest=population[0]
        for individual in population:
            if individual.isFitterThan(fittest):
                fittest = individual
        return fittest
    
    
    """
    returns the unfittest individual of the population
    """
    def getUnfittest(population):
        unfittest=population[0]
        for individual in population:
            if unfittest.isFitterThan(individual):
                unfittest = individual
        return unfittest
    
    
    """
    returns the mean fitness of the population
    """
    def getMeanFitness(population):
        total = sum(individual.fitness for individual in population)
        return total/len(population)
    