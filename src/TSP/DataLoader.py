# -*- coding: utf-8 -*-
"""
@author: Alejandro Moya Garcia
"""
import xml.etree.ElementTree as XMLReader
from City import City
from GeneticAlgorithm import GeneticAlgorithm
from Individual import Individual

class DataLoader:

    def loadData(self):
        GA=self.loadGAParams()
        cities=self.loadProblem()
        GA.setCities(cities)
        return GA
    
    """
    Loads the cities from a XML file
    """
    def loadCities(self):
        xmlCities = XMLReader.parse("../../data/"+self.filename).getroot()
        cities = []
        
        for city in xmlCities.findall('city'):
            id = city.find('id').text
            x = float(city.find('x').text)
            y = float(city.find('y').text)
            cities.append(City(int(id)-1, x, y))
        return cities
    
    

    """
    Loads the genetic algorithm parameters from a XML file
    """
    def loadGAParams(self):
        GAParams = XMLReader.parse("../../data/GAParams.xml").getroot()
        
        crossRate = float(GAParams.find('crossRate').text)
        mutationRate = float(GAParams.find('mutationRate').text)
        populationSize= int(GAParams.find('populationSize').text)
        mutationType = GAParams.find('mutationType').text
        crossType = GAParams.find('crossType').text
        parentSelectType = GAParams.find('parentSelectionType').text
        tournamentSize = int(GAParams.find('parentSelectionType').attrib['k'])
        survivorSelectType = GAParams.find('survivorSelectionType').text
        elitism = int(GAParams.find('survivorSelectionType').attrib['elitism'])
        terminationCondition = GAParams.find('terminationCondition').text
        numberGenerations = int(GAParams.find('terminationCondition').attrib['numberGenerations'])
        self.filename = GAParams.find('fileName').text
       
        GA=GeneticAlgorithm(crossRate, mutationRate, populationSize,
                            mutationType, crossType, parentSelectType,tournamentSize,
                            survivorSelectType, elitism,terminationCondition,
                            numberGenerations)
        return GA

    def loadProblem(self):
        isCoordinate = False
        file = open("../../data/kroA100.tsp", "r")
        cities =[]
        
        for line in file:
            data = []
            if line == "EOF\n":
                break
            if isCoordinate:
                data = line.split()
                cities.append(City(int(data[0])-1, float(data[1]), float(data[2])))
                
            if line == "NODE_COORD_SECTION\n":
                isCoordinate = True
        file.close()
        #######################################################
        citiesOpt = []
        isCoordinate = False
        file = open("../../data/kroA100.opt.tour", "r")
        for line in file:
            data = []
            if line == "-1\n":
                break
            if isCoordinate:
                citiesOpt.append(cities[int(line.rstrip())-1])
                
            if line == "TOUR_SECTION\n":
                isCoordinate = True
        file.close()
        fittest = Individual(cities)
        fittest.setCities(citiesOpt)
        fittest.calcFitness()
        print("Best tour fitness: ",fittest.fitness)
        return cities