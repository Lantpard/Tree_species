import pandas as pd
import geopandas as gpd

df_ibague = pd.read_csv('src/static/data/Datos_Ibague_limpios.csv',dtype={'latitude':float,'longitude':float})

df_comunas = gpd.read_file('src/static/data/COMUNAS.geojson')


#df1=df_ibague[df_ibague['comuna']==1]
#for i in range(len(df1)):
#    print(df1['latitude'].iloc[i],df1['longitude'].iloc[i])

#print(len(df1))