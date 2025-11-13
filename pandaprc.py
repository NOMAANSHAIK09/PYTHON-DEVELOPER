import pandas as pd


df = pd.read_csv("employees.csv", sep=",")
#ATRIBUTES:

#PRINT NO OF ROW AND COL
sp=df.shape
#PRINT NO OF COL WITH KEYS 
col1 = df.columns
#PRINT RANGE OF INDEX
ind=df.index
#PRINT ALL DATA IN NESTED SETS 
val=df.values
#PRINT SIZE OD DATA
siz = df.size

#METHODS
#print first 5 rows
hed=df.head()
#print last row
tal = df.tail()
print(tal)

