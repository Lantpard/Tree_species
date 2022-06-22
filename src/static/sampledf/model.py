import pandas as pd
import geopandas as gpd

df_ibague = pd.read_csv('src/static/data/Datos_Ibague_limpios.csv')

df_comunas = gpd.read_file('src/static/data/COMUNAS.geojson')


