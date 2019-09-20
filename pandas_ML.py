import pandas as pd
data = pd.DataFrame({'Country':['Russia','Colombia','Chile'],'Rank':[121,24,15]})
print(data)
print(data.describe())
print(data.info())

"""Let's sort the data frame by Rank - inplace = True will make changes to the data"""
x=data.sort_values(by=['Rank'],ascending=True,inplace=False)

""" We can sort the data by not just one column but multiple columns as well. """
x=data.sort_values(by=['Country','Rank'],ascending=[True,False],inplace=False)
print(x)

""" MAke another data with duplicate data """
da = pd.DataFrame({'k1':['one']*3 + ['two']*4 , 'k2':[3,4,5,2,1,5,1]})
print(da.sort_values(by='k2'))
print(da.drop_duplicates())
print(da.drop_duplicates(subset='k1',keep='last'))    #put keep='first'or 'last' or nothing
