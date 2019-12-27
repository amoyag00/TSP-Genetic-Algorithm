"""
@author: Alejandro Moya García
"""

class TerminationCondition:
    
    """
    Checks if the algorithm has reached the maximum number of generations
    """    
    def checkGenerations(generationCount, numberGenerations):
        return generationCount >= numberGenerations
    
        