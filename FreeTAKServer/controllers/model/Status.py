#######################################################
# 
# Status.py
# Python implementation of the Class Status
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:07 AM
# Original author: Corvo
# 
#######################################################


class Status:
    def __init__(self):  
        self.battery = "100" 
        
    # % of the battery on the phone
    
    # battery getter 
    def getbattery(self): 
        return self.battery 

    # battery setter 
    def setbattery(self, battery=0):  
        self.battery=battery 

    # probably boolean to determine if ready or not
     
    # readiness getter 
    def getreadiness(self): 
        return self.readiness 

    # readiness setter 
    def setreadiness(self, readiness=0):  
        self.readiness=readiness 
