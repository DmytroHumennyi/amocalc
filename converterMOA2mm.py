import os.path
from tabulate import tabulate
import numpy as np
import json


class Amo: # Amunition : balistic
    def __init__ (self,vendor='def',calibre='223'): # Init
        self.vendor = vendor
        self.calibre = calibre
            
    def save (self): # Saving the Amunition dataset  
        jsonFileName = self.vendor+self.calibre
        if (os.path.exists (jsonFileName)) and (input (f"file {jsonFileName} esist. Would You like re-write it? (y/n): ") == 'y') or not (os.path.exists (jsonFileName)) :
            self.balistic = {}
            print (f"\n New Amo : {self.vendor}, {self.calibre} \n")
            index = 0
            while input("Add one data to the Set? (y/n): ") != 'n':
                index = index + 1
                distance = input ("Distande [m]: ")
                deviation = input ("Deviation [mm]:")
                velicity = input ("Velocity [m/s]: ")
                self.balistic.update ({index:[distance, deviation,velicity]})
            with open (jsonFileName,'w') as f:
                json.dump (self.balistic, f)

    def load (self): # load balistaic dataset from a JSON
        jsonFileName = self.vendor+self.calibre
        if os.path.exists (jsonFileName):
             with open (jsonFileName,'r') as f:
                 self.balistic = json.load(f)
             print ("The DataSet is loaded successfully") # Loading tha Amunition dataset

    def show (self, table = True): # Visualisation the balistaic dataset from a JSON
        if table == True:
             print ("Distance [m], Deviation [mm], Velocity (m/s) ")
             print (f"Amo : {self.vendor}, {self.calibre}")
             print (tabulate(self.balistic))
        else:
            print ("Visualisation is disabled") # Print table of balistic (Distance, Deviation, Velocity)
    
    def get (self, distance = 0): # Getting deviation (in mm) regarding to distance of shoting.
        tol = 0.01
        x = distance
        for sets in self.balistic.values():
            if abs(x - float(sets[0])) < tol:
                y = float(sets[1])
                return y
            else:
                if x > float(sets[0]):
                    dis_l = float(sets[0])
                    dev_l = float(sets[1])
                    vel_l = float(sets[2])
                if x < float(sets[0]):
                    dis_h = float(sets[0])
                    dev_h = float(sets[1])
                    vel_h = float(sets[2])
                    break
        x1 = dis_l
        x2 = dis_h
        y1 = dev_l
        y2 = dev_h
        z1 = vel_l
        z2 = vel_h

        y = y1 + (x-x1)*((y2-y1)/(x2-x1)) # interpolate Deviation
        z = z1 + (x-x1)*((z2-z1)/(x2-x1)) # interpolate Velocity
        return y

## BODY
#amo = Amo (input ("Plase give vendor name: "))
amo = Amo ('sts','223')
amo.save ()
amo.show ()
amo.load ()
y = amo.get (float(input ("Pleae give Distance: ")))
print (f"Correction should be:{int(y)}, [mm]")
