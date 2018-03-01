# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 12:55:19 2018

@author: liamg_000
"""

import numpy as np

class QuickFindUF():
    def __init__(self, N):
        try:
            self.id_arr = np.array([i for i in range(N)])
            self.N = N
            print(self.id_arr)
        except:
            print("Data Structure creation failed. Please pass an integer next time.")
            
    
    
    def root(self, i):
        while i != self.id_arr[i]:
            i = self.id_arr[i]
            
        return i
    
    
    def connected(self,p,q):
        try:
            return self.root(p) == self.root(q)      
        except:
            print("Please pass integers between 0 and", self.N)
            return 0
        
    
    def union(self,p,q):
        try:
            i = self.root(p)
            j = self.root(q)
            
            self.id_arr[i] = j
        except:
            print("Error in Union")
                   
                       
if __name__ ==  "__main__":
    quick_finder = QuickFindUF(10)
    
    quick_finder.union(0,5)
    quick_finder.union(5,6)
    quick_finder.union(1,2)
    quick_finder.union(2,7)
    quick_finder.union(8,3)
    quick_finder.union(3,4)
    quick_finder.union(4,9)
    
    print(quick_finder.connected(0,5))
    print(quick_finder.connected(0,1))
    print(quick_finder.connected(1,7))
    print(quick_finder.connected(2,9))
    print(quick_finder.connected(8,4))
    print(quick_finder.connected(8,5))
    print(quick_finder.connected(8,9))
    print(quick_finder.connected(0,7))
    print(quick_finder.id_arr)
