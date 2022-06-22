import geopandas as gpd
import folium
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from static.sampledf.model import df_ibague

def mapl():
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

    m = folium.Map(location=[4.430081,-75.2112492], zoom_start=13, tiles ='Stamen Terrain')
    m

    for _, r in data.iterrows():
        # Without simplifying the representation of each borough,
        # the map might not be displayed
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
    folium.GeoJson(data=data, style_function=style).add_to(m)
    m

    

    df_ibague['X'] = df_ibague['X'].str.replace(',', '.')
    df_ibague['Y'] = df_ibague['Y'].str.replace(',', '.')
    locations = df_ibague[['X', 'Y']]
    location_list = locations.astype('float').values.tolist()

    for point in range(len(location_list[:200])):
        folium.Marker(location_list[point]).add_to(m)

    return m