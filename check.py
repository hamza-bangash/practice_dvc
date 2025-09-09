import pandas as pd

data = {
    'id':[1,2,3,4,5,6],
    'name':['Hamza','mustafa','ashir','aimal','tayab','amir']
}

df = pd.DataFrame(data)

df.to_csv('data/name.csv',index=False)