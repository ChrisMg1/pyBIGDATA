import pandas as pd

filename = 'C:/Users/blue/Documents/sample_data/parking-citations.csv'
# filename = 'C:/Users/ZVM_cm/Documents/ADAC-data/DE_BAYERN_2018_09.csv'

gl = pd.read_csv(filename)

gl['number'].count()


gl.head()
gl.info(memory_usage='deep')

df = pd.DataFrame(data=gl)

data = pd.DataFrame.from_csv('C:/Users/ZVM_cm/Documents/ADAC-data/DE_BAYERN_2018_09.csv')

df.groupby(['assetId']).groups.keys()

