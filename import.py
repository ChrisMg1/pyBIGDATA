import pandas as pd
gl = pd.read_csv('C:/Users/ZVM_cm/Documents/ADAC-data/DE_BAYERN_2018_09.csv', encoding='utf-8')
gl.head()
gl.info(memory_usage='deep')

df = pd.DataFrame(data=gl)

data = pd.DataFrame.from_csv('C:/Users/ZVM_cm/Documents/ADAC-data/DE_BAYERN_2018_09.csv')

df.groupby(['assetId']).groups.keys()

