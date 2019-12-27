# -*- coding: utf-8 -*-
"""
@author: Alejandro Moya García
"""
import random
import xml.etree.ElementTree as XMLWriter
from xml.dom import minidom
from City import City

class TSPGenerator:
    
    def __init__(self, numCities):
        self.numCities = numCities
        
    """
    Generates a problem instance of `numCities` cities
    """
    def generateInstance(self):
        bound = 10000
        cities = []
        for i in range(0, self.numCities):
            x = random.randint(0, bound)
            y = random.randint(0, bound)
            city = City(str(i+1), str(x), str(y))
            cities.append(city)
        return cities
    
    """
    Saves the problem instance in a XML file
    """
    def saveInstance(self, cities, filename):
        root = XMLWriter.Element('cities')
        for city in cities:
           xmlCity = XMLWriter.SubElement(root,'city')
           cityId = XMLWriter.SubElement(xmlCity, 'id')
           cityId.text = city.id
           x = XMLWriter.SubElement(xmlCity,'x')
           x.text = city.x
           y = XMLWriter.SubElement(xmlCity,'y')
           y.text = city.y
        
        data = minidom.parseString(XMLWriter.tostring(root)).toprettyxml(indent="   ")
        with open("../../data/" + filename, "w") as file:
            file.write(data)
        file.close()
           
gen = TSPGenerator(1000)
gen.saveInstance(gen.generateInstance(), "TSPInstance1000.xml")      