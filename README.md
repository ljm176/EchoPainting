# EchoPainting

Takes an excel sheet with a 1536 well plate format and turns it into a CSV for printing with the Labcyte ECHO. 

# Useage

Run make_paint_csv.py and enter the name of the excel file with the picture you want to convert to an ECHO compatible CSV. Can run with template.xlsx to see an example. Take the output file (with the "_ECHO.csv" ) and load into the ECHO robot. 

Source plate should be setup with color 1 at A1, 2 at B1 etc. 
