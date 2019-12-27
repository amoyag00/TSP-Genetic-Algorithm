# -*- coding: utf-8 -*-
"""
@author: Alejandro Moya García
"""

from DataLoader import DataLoader

def main():
    GA = DataLoader().loadData()
    GA.run()
main()