import pandas as pd
#1 creating series and labeling
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
#creating DataFrame
data = {"calories": [420, 380, 390],"duration": [50, 40, 45]}
myvar = pd.DataFrame(data)
print(myvar)
#locating
df = pd.DataFrame(data)
print(df.loc[[0, 1]])
#reading csv files = done
#cleaning data: done
'''1.cleaning empty cells = to clear empty cells(d.dropna(inplace=true)), to replace empty cells with value x(d.fillna(x,inplace=true)
2.removing duplicates = (d.drop_duplicates(inplace=true))
3.cleaning wrong format
4.cleaning wrong data'''

