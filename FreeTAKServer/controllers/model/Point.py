#######################################################
# 
# point.py
# Python implementation of the CoT point
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:07 AM
# Original author: Corvo
# 
#######################################################
# Latitude referred to the WGS 84 ellipsoid in degrees

class Point:

    def __init__(self):
        self.le = "9999999.0"
        self.ce = "9999999.0"
        self.hae = "00.00000000"
        self.lon = "00.00000000"        
        self.lat = "00.00000000"


    # ce getter 
    def getce(self): 
        return self.ce 

    # ce setter 
    def setce(self, ce):
        self.ce=ce 

    # le getter 
    def getle(self): 
        return self.le 

    # le setter 
    def setle(self,le):  
        self.le=le


    # lat getter 
    def getlat(self):
        return self.lat 

    # lat setter 
    def setlat(self, lat):  
        self.lat=lat

        # lon getter 
    def getlon(self):
        return self.lon 

    # lon setter 
    def setlon(self,lon):
        self.lon=lon
  
    def gethae(self):
        return self.hae

    def sethae(self,hae):
        self.hae = hae
