# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 12:55:19 2018

@author: liamg_000
"""

class QuickFindUF():
    def __init__(self, N):
        try:
            self.N = N
            self.id_arr = [None] * N
            self.sz_arr = [1] * N
            for i in range(N):
                self.id_arr[i] = i
        except:
            print("Constructor failed")
            
    
    
    def root(self, i):
        while i != self.id_arr[i]:
            self.id_arr[i] = self.id_arr[self.id_arr[i]]
            i = self.id_arr[i]
            
        return i
    
    
    def connected(self,p,q):
        try:
            return self.root(p) == self.root(q)      
        except:
            print("Error in Connected")
            return 0
        
    
    def union(self,p,q):
        try:
            root_p = self.root(p)
            root_q = self.root(q)
            
            if root_p == root_q:
                return
            
            if self.sz_arr[root_p] < self.sz_arr[root_q]:
                self.id_arr[root_p] = root_q
                self.sz_arr[root_q] += self.sz_arr[root_p]
                
            else:
                self.id_arr[root_q] = root_p
                self.sz_arr[root_p] += self.sz_arr[root_q]
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
