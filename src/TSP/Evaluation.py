# -*- coding: utf-8 -*-
"""
@author: Alejandro Moya García
"""
from DataLoader import DataLoader
from Plotter import Plotter
import time

class Evaluation:
    
    """
    Calculates Mean Best Fitness (MBF), Average Number of Evaluations to a 
    Solution (AES), Success Rate (SR), progress curves and execution times.
    Plots the average results obtained from a number of specified executions
    """
    def evaluate(numRuns):
        #MBF
        bestFitnessList = []
        #AES
        numFitnessEvalList = []
        #SR
        successTimes = 0
        successThreshold = 155579.694769357
        #PROGRESS CURVE
        numGenerations = 10000
        fittestValues = [0] * numGenerations
        unfittestValues = [0] * numGenerations
        meanFitnessValues = [0] * numGenerations
        #TIME
        times = []
        
        for i in range(0,numRuns):
            GA = DataLoader().loadData()
            GA.setPlotStats(False)
            start = time.time()
            GA.run()
            end = time.time()
            times.append(end-start)
            
            #MBF
            bestFitness = GA.getBestFitness()
            bestFitnessList.append(bestFitness)
            
            #SR
            if bestFitness > successThreshold:
                successTimes += 1
                #AES
                numFitnessEvalList.append(GA.getNumFitnessEvals())
            
            fittestValues = [sum(x) for x in zip(fittestValues, GA.fittestValues)]
            unfittestValues = [sum(x) for x in zip(unfittestValues, GA.unfittestValues)]
            meanFitnessValues = [sum(x) for x in zip(meanFitnessValues, GA.meanFitnessValues)]
            print("Run nº", i+1)  
        
        #PROGRESS CURVE
        fittestValues = [x / numRuns for x in fittestValues]
        meanFitnessValues = [x / numRuns for x in meanFitnessValues]
        unfittestValues = [x / numRuns for x in unfittestValues]
        
        MBF = sum(bestFitnessList)/len(bestFitnessList)
        SR = (successTimes/numRuns)*100
        AES = sum(numFitnessEvalList)/len(numFitnessEvalList)
        MET = sum(times)/len(times)
        Plotter.plotConvergence(fittestValues, meanFitnessValues, unfittestValues)
        Plotter.plotText(["Mean Best Fitness: " + str(MBF), "Success Rate: " + str(SR)+"%", "Average number of evalutions to a Solution: " + str(AES), "Mean Execution Time: "+str(MET)+" (s)"])
        print ("MBF: ", MBF)
        print ("Sucess Rate: ", SR)
        print ("AES: ", AES)
        print ("Mean execution time: ", MET)
    
    
    """
    Evaluates how the fitness evolves as the crossover rate increments
    """
    def evaluateCrossoverRateFitness():
        bestFitnessValues =  []
        meanFitnessValues = []
        worstFitnessValues = []
        
        numIterPerCrossoverRate = 5
        crossoverRateIncrement = 20
        crossoverRateValues = list(range(0, 101, crossoverRateIncrement))
        
        for i in range(0, len(crossoverRateValues)):
            bestFitnessValuesSum = []
            meanFitnessValuesSum = []
            worstFitnessValuesSum = []
            
            for j in range(0,numIterPerCrossoverRate):
                GA = DataLoader().loadData()
                GA.setPlotStats(False)
                GA.crossoverRate = crossoverRateValues[i]/100
                GA.run()
                bestFitnessValuesSum.append(GA.getBestFitness())
                meanFitnessValuesSum.append(GA.getMeanFitness())
                worstFitnessValuesSum.append(GA.getWorstFitness())
            bestFitnessValues.append(sum(bestFitnessValuesSum)/len(bestFitnessValuesSum))
            meanFitnessValues.append(sum(meanFitnessValuesSum)/len(meanFitnessValuesSum))
            worstFitnessValues.append(sum(worstFitnessValuesSum)/len(worstFitnessValuesSum))
            print(str(crossoverRateValues[i])+ "% crossover rate evaluated")
        Plotter.plotCrossoverRateEvaluation(crossoverRateValues, bestFitnessValues, meanFitnessValues, worstFitnessValues)
    
    
    
    """
    Evaluates how the speed of convergence evolves as the crossover rate increments
    """
    def evaluateCrossoverRateSpeed():
        bestFitnessValuesEachRate =  []
        
        numIterPerCrossoverRate = 5
        crossoverRateIncrement = 20
        numGen=100
        crossoverRateValues = list(range(0, 101, crossoverRateIncrement))
        
        for i in range(0, len(crossoverRateValues)):
            bestFitnessValuesCurrentRate = [0]*numGen
            
            
            for j in range(0,numIterPerCrossoverRate):
                GA = DataLoader().loadData()
                GA.setPlotStats(False)
                GA.crossoverRate = crossoverRateValues[i]/100
                GA.numberGenerations = numGen
                GA.run()
                bestFitnessValuesCurrentRate=[sum(x) for x in zip(bestFitnessValuesCurrentRate, GA.getFittestValues())] 
                
            bestFitnessValuesEachRate.append([x / numIterPerCrossoverRate for x in bestFitnessValuesCurrentRate])
            print(str(crossoverRateValues[i])+ "% crossover rate evaluated")
        Plotter.plotCrossoverRateSpeedEvaluation(crossoverRateValues, bestFitnessValuesEachRate, numGen)          
        
        
Evaluation.evaluate(50)