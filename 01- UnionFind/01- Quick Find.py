# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 12:55:19 2018

TO-DO: Read in N, union calls and connected calls from external file

@author: liamg_000
"""

import numpy as np

class QuickFindUF():
    def __init__(self, N):
        try:
            self.id_arr = np.array([i for i in range(N)])
            print(self.id_arr)
        except:
            print("Data Structure creation failed. Please pass an integer next time.")
    
    
    def connected(self,p,q):
        try:
            return self.id_arr[p] == self.id_arr[q]
        except:
            print("Please pass integers between 0 and 9")
            return 0
        
    
    def union(self,p,q):
        p_id = self.id_arr[p]
        q_id = self.id_arr[q]
        
        self.id_arr[self.id_arr == p_id] = q_id
                   
                   
""" Quick Test """
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
