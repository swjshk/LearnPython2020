import pandas as pd
AAPLTable = pd.read_csv("AAPL.csv")
type(AAPLTable)
print(type(AAPLTable))
print(AAPLTable.shape)
AAPLTable.index
