import geopandas as gpd
import folium
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from static.sampledf.model import df_comunas,df_ibague
from branca.element import Template, MacroElement
from folium.plugins import MarkerCluster


def mapl2():

    data = df_comunas

    star_coords = (4.430081,-75.2112492)

    folium_map2= folium.Map(location=star_coords, zoom_start=13, tiles ='Stamen Terrain')
  
    #arboles
    #geometrias
    #COMUNA 1
    data1=data[data['COMUNAS']=="COMUNA 1"]
    for _, r in data1.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j, style_function = lambda x:{'fillColor': 'green','color':'black','weight':0.5, 'fillOpacity': 0.4})
        folium.Popup(r['COMUNAS']).add_to(geo_j)
        geo_j.add_to(folium_map2)

    #COMUNA 2
    data1=data[data['COMUNAS']=="COMUNA 2"]
    for _, r in data1.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j, style_function = lambda x:{'fillColor': "red",'color':'black','weight':0.5, 'fillOpacity': 0.4})
        folium.Popup(r['COMUNAS']).add_to(geo_j)
        geo_j.add_to(folium_map2)

    #COMUNA 3
    data1=data[data['COMUNAS']=="COMUNA 3"]
    for _, r in data1.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j, style_function = lambda x:{'fillColor': "blue",'color':'black','weight':0.5, 'fillOpacity': 0.4})
        folium.Popup(r['COMUNAS']).add_to(geo_j)
        geo_j.add_to(folium_map2)

    #COMUNA 4
    data1=data[data['COMUNAS']=="COMUNA 4"]
    for _, r in data1.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j, style_function = lambda x:{'fillColor': "yellow",'color':'black','weight':0.5, 'fillOpacity': 0.4})
        folium.Popup(r['COMUNAS']).add_to(geo_j)
        geo_j.add_to(folium_map2)

    #COMUNA 5
    data1=data[data['COMUNAS']=="COMUNA 5"]
    for _, r in data1.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j, style_function = lambda x:{'fillColor': "orange",'color':'black','weight':0.5,'fillOpacity': 0.4})
        folium.Popup(r['COMUNAS']).add_to(geo_j)
        geo_j.add_to(folium_map2)
    
    #COMUNA 6
    data1=data[data['COMUNAS']=="COMUNA 6"]
    for _, r in data1.iterrows():
        sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
        geo_j = sim_geo.to_json()
        geo_j = folium.GeoJson(data=geo_j, style_function = lambda x:{'fillColor': "violet",'color':'black','weight':0.5,'fillOpacity': 0.4})
        folium.Popup(r['COMUNAS']).add_to(geo_j)
        geo_j.add_to(folium_map2)


    #crear Clusters
    mc=MarkerCluster()
    
    for i in range(len(df_ibague)):
        mc.add_child(folium.Circle(location=[df_ibague['latitude'].iloc[i],df_ibague['longitude'].iloc[i]],radius=2,color= "green"))
    
    folium_map2.add_child(mc)

    return folium_map2