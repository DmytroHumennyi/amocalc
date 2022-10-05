import os.path
from tabulate import tabulate
import numpy as np
import json


class Amo:
    def __init__ (self,vendor='def',calibre='0'):
        self.vendor = vendor
        self.calibre = calibre # Precondition
            
    def save (self):
    # create a JSON file and save ther Balistic paramets of Amunition.
    # JSON file name: VendorCalibre
    # Balistic parameters: Distance [Correcrion, Velicity]    
        jsonFileName = self.vendor+self.calibre
        if os.path.exists (jsonFileName):
             if input (f"file {jsonFileName} esist. Would You like re-write it? (y/n): ") == 'y':
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
                    json.dump (self.balistic, f) # Saving the Amunition dataset

    def load (self):
    # load balistaic dataset from a JSON 
    # JSON file name: VendorCalibre
    # Balistic parameters: Distance [Correcrion, Velicity]    
        jsonFileName = self.vendor+self.calibre
        if os.path.exists (jsonFileName):
             with open (jsonFileName,'r') as f:
                 self.balistic = json.load(f)
             print ("The DataSet is loaded successfully") # Loading tha Amunition dataset

    def show (self, table = True):
    # Visualisation the balistaic dataset from a JSON 
    # After loaing the data from JSON file
    # it can be visualised as Table or Graph
        if table == True:
             print ("Distance [m], Deviation [mm], Velocity (m/s) ")
             print (f"Amo : {self.vendor}, {self.calibre}")
             print (tabulate(self.balistic))
        else:
            print ("Visualisation is disabled") # Print table of balistic (Distance, Deviation, Velocity)
    
    def get (self, distance = 0):
    # Getting deviation (in mm) regarding to distance of shoting.
    # To estimate it ther is Interplation methods of colculation
    # Param's:
    #   distance (in meters)
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
        y = y1 + (x-x1)*((y2-y1)/(x2-x1))    
        return y # Getting deviation (in mm) relates to to Distance



 ## BODY
      

amo = Amo ("rem","223")
amo.load ()
while True:

    y = float(amo.get (float(input ("Pleae give Distance: "))))
    print (f"Correction should be:{int(y)}, [mm]")
