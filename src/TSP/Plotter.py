# -*- coding: utf-8 -*-
"""
@author: Alejandro Moya García
"""
import matplotlib.pyplot as plotter

class Plotter:
    
    """
    Plots a graphic with points representing cities and lines representing the path
    """
    def plotCities(cities, path):
        plotter.figure(num="Traveling Salesman Problem")
        for city in cities:
            plotter.scatter(city.x,city.y, color="black", s=70)
            plotter.text(city.x + 0.5, city.y +0.2, city.id, fontsize = 9)
            
        plotter.scatter(path[0].x,path[0].y, color="red", s=140)
        for i in range(0, len(path)-1):
            x = [path[i].x, path[i+1].x]
            y = [path[i].y, path[i+1].y]
            plotter.plot(x, y, "b-")
        x = [path[len(path)-1].x, path[0].x]
        y = [path[len(path)-1].y, path[0].y]
        plotter.plot(x, y, "b-")
        plotter.show(block=True)
    

    """
    Plots the progress curve of the algorithm showing the best, worst and mean
    fitness of each generation
    """                           
    def plotConvergence(fittestValues, meanFitnessValues, unfittestValues):
        plotter.figure (num="Convergence")
        plotter.xlabel('Generation nº')
        plotter.ylabel('Fitness')
        generations = list(range(0,len(fittestValues)))           
        
        plotter.plot(generations, unfittestValues,"r-", label="Worst Fitness")
        plotter.plot(generations, meanFitnessValues,"b-", label="Mean Fitness")
        plotter.plot(generations, fittestValues,"g-", label="Best Fitness")
        
        plotter.legend(loc='upper center', shadow=True, fontsize='x-large')
        plotter.show(block=True)
    
    """
    Plots lines under the x-axis label
    """
    def plotText(lines):
        textstr = '\n'
        for line in lines:
            textstr += line+'\n'
        plotter.xlabel("Generation nº\n\n"+textstr)
        plotter.tight_layout()
        plotter.show(block=True)
    
    
    """
    Plots the evolution of the best, mean and worst fitness as the crossover rate increases
    """
    def plotCrossoverRateEvaluation(crossoverRateValues, fittestValues, meanFitnessValues, unfittestValues):
        plotter.figure (num="Crossover Rate Fitness Evaluation")
        plotter.xlabel('Crossover Rate')
        plotter.ylabel('Fitness')
                 
        plotter.plot(crossoverRateValues, unfittestValues,"r-", label="Worst Fitness")
        plotter.plot(crossoverRateValues, meanFitnessValues,"b-", label="Mean Fitness")
        plotter.plot(crossoverRateValues, fittestValues,"g-", label="Best Fitness")
        
        plotter.legend(loc='upper center', shadow=True, fontsize='x-large')
        plotter.show(block=True)
        
    """
    Plots the average progress curve for different crossover rate values
    """
    def plotCrossoverRateSpeedEvaluation(crossoverRateValues, fittestValuesEachRate, numGen):
        plotter.figure (num="Crossover Rate Speed Evaluation")
        plotter.xlabel('Generation nº')
        plotter.ylabel('Fitness')
        
        for i in range(0, len(crossoverRateValues)):
            plotter.plot(list(range(0,numGen)), fittestValuesEachRate[i], label="Best Fitness " + str(crossoverRateValues[i])+"% crossover rate")
        legend = plotter.legend(loc='upper center', shadow=True, fontsize='x-large')
        for legobj in legend.legendHandles:
            legobj.set_linewidth(5.0)
        plotter.show(block=True)
        
        
    def closePreviousPlots():
        plotter.close("all")
        
        
    