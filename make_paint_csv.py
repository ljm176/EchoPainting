# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 17:37:29 2021

@author: lajamu
"""

import openpyxl, csv

picture = input("Enter File name of excel template: ")

letters = []
for i in range(65, 91):
    letters.append(chr(i))

for i in range(6):
    letters.append(letters[0] + letters[i])

plate1536 = []

for i in range(1, 49):
    for letter in letters:
        plate1536.append(letter + str(i))


wb = openpyxl.load_workbook(filename = picture)

ws = wb.active

vals = []

for col in ws.iter_cols():
    for cell in col:
        vals.append(cell.value)

source_dict = {1 : "A1", 2: "B1", 3:"C1", 4 : "D1", 5 : "E1"}

transfers = [[ "Source Well"," Destination Well", "Transfer Volume"]]

for s, d in zip(vals, plate1536):
    if s != None:
        transfers.append([source_dict[s], d, 5])


csvFile = picture[0:-5] + "_ECHO.csv"
with open(csvFile, "w", newline="") as outputcsv:
    echoWriter = csv.writer(outputcsv, delimiter=",")
    for t in transfers:
        echoWriter.writerow(t)