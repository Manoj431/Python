import xlrd     
      
# Define the location of the file     
loc = ("E:\Manoj\Java_io")     
      
# To open the Workbook     
wb = xlrd.open_workbook(loc)     
sheet = wb.sheet_by_index(0)     
          
sheet.cell_value(0, 0)  

#Extracting all columns name..
for i in range(sheet.cols):
    print(sheet.cell_value(0,i))

#extract a particular row value
print(sheet.row_values(1))