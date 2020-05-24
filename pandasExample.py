import pandas as pd

# AAPLTable = pd.read_csv("AAPL.csv")
# type(AAPLTable)
# print(type(AAPLTable))
# print(AAPLTable.shape)
# AAPLTable.index
data = [['tom',10],['nick',15],['jul',13]]
df=pd.DataFrame(data,index=['a',2,3],columns=['name','age'],)
print(df)