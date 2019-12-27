# -*- coding: utf-8 -*-
"""
@author: Alejandro Moya García
"""
from Individual import Individual
from Plotter import Plotter
from CommonAlgorithms.Selection import Selection
from CommonAlgorithms.Crossover import Crossover
from CommonAlgorithms.Mutation import Mutation
from CommonAlgorithms.TerminationCondition import TerminationCondition
import random
import sys


class GeneticAlgorithm:
    
    def __init__(self, crossoverRate, mutationRate, populationSize,
                            mutationType, crossType, parentSelectType, tournamentSize,
                            survivorSelectType, elitism, terminationCondition, numberGenerations):
        self.crossoverRate = crossoverRate
        self.mutationRate = mutationRate
        self.populationSize = populationSize
        self.mutationType = mutationType
        self.crossoverType=crossType
        self.parentSelectType = parentSelectType
        self.tournamentSize = tournamentSize
        self.survivorSelectType= survivorSelectType
        self.elitism = elitism
        self.numParents = 2
        self.terminationCondition = terminationCondition
        self.numberGenerations = numberGenerations
        self.generationCount = 1
        self.fitnessPreviousGen = 0
        self.numFitnessEvals = 0
        self.fittest = None
        self.fittestValues = []
        self.unfittestValues = []
        self.meanFitnessValues = []
        self.plotStats = True
        
    def setPlotStats(self, value):
        self.plotStats = value
        
        
    def setCities(self, cities):
        self.cities = cities
               
    """
    Creates the first generation
    """
    def populate(self):
        self.currentGen = []
        for i in range(0,self.populationSize):
            newIndividual = Individual(self.cities)
            newIndividual.calcFitness()
            self.numFitnessEvals +=1
            self.currentGen.append(newIndividual)
            
    
    """
    Creates the next generation of individuals and replaces the last one.
    The steps in the creation of a new generation are:
        1. Parent selection
        2. Crossover
        3. Mutation
        4. Evaluation of the offspring
        5. Elitism
    """       
    def createNextGeneration(self):
        nextGen = []
        while(len(nextGen) < self.populationSize):
            #Selection
            parents = self.selectParents()
            
            #Crossover
            children = []
            if(random.uniform(0,1) <self.crossoverRate):
                children = self.crossover(parents)
            else:
                children.append(parents[0].clone())
                children.append(parents[1].clone())
          
            # Mutation
            if(random.uniform(0,1) < self.mutationRate):
                children[0] = self.mutate(children[0])
            if(random.uniform(0,1) < self.mutationRate):
                children[1] = self.mutate(children[1])
                
            # Evaluation
            children[0].calcFitness()
            children[1].calcFitness()
            self.numFitnessEvals += 2
            
            nextGen.extend(children)
            
        # Elitism
        if(self.elitism > 0):
            Selection.performElitism(self.currentGen, nextGen, self.elitism)
            
        self.currentGen = nextGen   
    
    
    """
    Performs the chosen selection type
    """
    def selectParents(self):
        if self.parentSelectType == "tournament":
            return Selection.tournamentSelection(self.currentGen, self.numParents, self.tournamentSize)
        else:
            print ("Error. Invalid parent selection type")
            sys.exit()
    
    
    """
    Performs the chosen crossover type
    """    
    def crossover(self, parents):
        if self.crossoverType == "pmx":
            children = Crossover.PMX(parents[0].cities.copy(), parents[1].cities.copy())
        else:
            print ("Error. Invalid crossover type")
            sys.exit() 
            
        child1 = Individual(self.cities)
        child1.setCities(children[0])
        
        child2 = Individual(self.cities)
        child2.setCities(children[1])
    
        return [child1, child2]
    
    
    """
    Performs the chosen mutation type
    """
    def mutate(self, individual):
        if self.mutationType == "swap":
            mutatedIndividual = individual.clone()
            mutatedIndividual.cities = Mutation.swap(mutatedIndividual.cities)
            return mutatedIndividual
        else:
            print ("Error. Invalid mutation type")
            sys.exit()
    
    
    """
    Checks if the genetic algorithm has met the termination condition
    """
    def hasTerminated(self):
        if self.terminationCondition == "generations":
            return TerminationCondition.checkGenerations(self.generationCount, self.numberGenerations)
        else:
            print ("Error. Invalid termination condition")
            sys.exit()


    """
    Creates new generations until a termination condition is met and then plots
    the results
    """
    def run(self): 
        self.populate()
        self.calcStats(self.currentGen)
        self.fitnessPreviousGen = Selection.getMeanFitness(self.currentGen)
            
        while not self.hasTerminated():
            self.createNextGeneration()
            self.generationCount+=1
            self.calcStats(self.currentGen)
            
        print("Fittest: "+ str(self.fittestValues[-1]))    
        if self.plotStats:    
            Plotter.closePreviousPlots()
            Plotter.plotCities(list(self.cities), Selection.getFittest(self.currentGen).cities)
            Plotter.plotConvergence(self.fittestValues, self.meanFitnessValues, self.unfittestValues)
    
    
    """
    Calculates the best fitness, the mean fitness and the worst fitness of a generation
    """
    def calcStats(self, population):
        fittest = population[0]
        unfittest = population[0]
        sumFitness =  0.0
        for individual in population:
            if individual.isFitterThan(fittest):
                fittest = individual
            if unfittest.isFitterThan(individual):
                unfittest = individual
            sumFitness += individual.fitness
        self.fittestValues.append(fittest.fitness)
        self.unfittestValues.append(unfittest.fitness)
        self.meanFitnessValues.append(sumFitness/len(population))
      
        
    def getBestFitness(self):
        return self.fittestValues[-1]
    
    
    def getWorstFitness(self):
        return self.unfittestValues[-1]
    
    
    def getMeanFitness(self):
        return self.meanFitnessValues[-1]
    
    
    def getNumFitnessEvals(self):
        return self.numFitnessEvals
    
    
    def getFittestValues(self):
        return self.fittestValues
        
