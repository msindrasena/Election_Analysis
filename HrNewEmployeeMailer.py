import os
import csv

filePath = os.path.join('.\', 'newEmployees.csv')

fileData = []

with open(file=filePath, newLine = '') as fileObject: 
    fileObject = csv.reader()
    