import geopandas as gpd
import folium
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = gpd.read_file('data/COMUNAS.geojson')

for x in data.index:
    color = np.random.randint(16, 256, size=3)
    color = [str(hex(i))[2:] for i in color]
    color = '#'+''.join(color).upper()
    data.at[x, 'color'] = color

def style(feature):
        return {
            'fillColor': feature['properties']['color'],
            'color': feature['properties']['color'],
            'weight': 1
        }

m = folium.Map(location=[4.43889, -75.23222], zoom_start=12)
m

for _, r in data.iterrows():
    # Without simplifying the representation of each borough,
    # the map might not be displayed
    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
folium.GeoJson(data=data, style_function=style).add_to(m)
m

df = pd.read_csv('data/Datos_Ibague_limpios.csv')

df['X'] = df['X'].str.replace(',', '.')
df['Y'] = df['Y'].str.replace(',', '.')
locations = df[['X', 'Y']]
location_list = locations.astype('float').values.tolist()

for point in range(len(location_list[:200])):
    folium.Marker(location_list[point]).add_to(m)