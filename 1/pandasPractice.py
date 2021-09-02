import pandas as pd

df=pd.read_csv("example.csv")
print(df)

print(list(df.columns))

print(df['SL.No'])

print(list(df.iloc[:,0]))
print(list(df.iloc[:,1]))

print(list(df.iloc[0]))
print(list(df.iloc[1]))

print(df[0:2])

g=df.groupby("Attribute A")
print(g)

# for grp, grpdata in g:
	# print(grp, grpdata)

print(df.fillna(0))
print(df.fillna(method='ffill'))
print(df.fillna(method='bfill'))

values={"Attribute A":0, "Attribute B":1, "Attribute C":"ADITI",}
print(df.fillna(value=values))