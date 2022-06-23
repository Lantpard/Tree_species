import geopandas as gpd
import folium
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from static.sampledf.model import df_comunas,df_ibague
from branca.element import Template, MacroElement
from folium.plugins import MarkerCluster


def mapl():

  data = df_comunas

  star_coords = (4.430081,-75.2112492)

  folium_map = folium.Map(location=star_coords, zoom_start=13, tiles ='Stamen Terrain')

  #arboles
  #geometrias
  #COMUNA 1
  data1=data[data['COMUNAS']=="COMUNA 1"]
  for _, r in data1.iterrows():
      sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
      geo_j = sim_geo.to_json()
      geo_j = folium.GeoJson(data=geo_j, style_function = lambda x:{'fillColor': 'green','color':'black','weight':0.5, 'fillOpacity': 0.4})
      folium.Popup(r['COMUNAS']).add_to(geo_j)
      geo_j.add_to(folium_map)

  #COMUNA 2
  data1=data[data['COMUNAS']=="COMUNA 2"]
  for _, r in data1.iterrows():
    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function = lambda x:{'fillColor': "red",'color':'black','weight':0.5, 'fillOpacity': 0.4})
    folium.Popup(r['COMUNAS']).add_to(geo_j)
    geo_j.add_to(folium_map)

  #COMUNA 3
  data1=data[data['COMUNAS']=="COMUNA 3"]
  for _, r in data1.iterrows():
    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function = lambda x:{'fillColor': "blue",'color':'black','weight':0.5, 'fillOpacity': 0.4})
    folium.Popup(r['COMUNAS']).add_to(geo_j)
    geo_j.add_to(folium_map)

  #COMUNA 4
  data1=data[data['COMUNAS']=="COMUNA 4"]
  for _, r in data1.iterrows():
    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function = lambda x:{'fillColor': "yellow",'color':'black','weight':0.5, 'fillOpacity': 0.4})
    folium.Popup(r['COMUNAS']).add_to(geo_j)
    geo_j.add_to(folium_map)

  #COMUNA 5
  data1=data[data['COMUNAS']=="COMUNA 5"]
  for _, r in data1.iterrows():
    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function = lambda x:{'fillColor': "orange",'color':'black','weight':0.5,'fillOpacity': 0.4})
    folium.Popup(r['COMUNAS']).add_to(geo_j)
    geo_j.add_to(folium_map)
  
  #COMUNA 6
  data1=data[data['COMUNAS']=="COMUNA 6"]
  for _, r in data1.iterrows():
    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j, style_function = lambda x:{'fillColor': "violet",'color':'black','weight':0.5,'fillOpacity': 0.4})
    folium.Popup(r['COMUNAS']).add_to(geo_j)
    geo_j.add_to(folium_map)

  #capa Arbolado
  #COMUNA 1
  df1=df_ibague[df_ibague['comuna']==1]
  for i in range(len(df1)):
    folium.Circle(location=[df1['latitude'].iloc[i],df1['longitude'].iloc[i]],radius=2,color= ('red' if (df1['estado_sanitario'].iloc[i]=="Muerto") else ( 'orange' if (df1['estado_sanitario'].iloc[i]=="Critico") else ( 'yelow' if (df1['estado_sanitario'].iloc[i]=="Enfermo") else "green")))).add_to(folium_map)
  
  #COMUNA 2
  df1=df_ibague[df_ibague['comuna']==2]
  for i in range(len(df1)):
    folium.Circle(location=[df1['latitude'].iloc[i],df1['longitude'].iloc[i]],radius=2,color= ('red' if (df1['estado_sanitario'].iloc[i]=="Muerto") else ( 'orange' if (df1['estado_sanitario'].iloc[i]=="Critico") else ( 'yelow' if (df1['estado_sanitario'].iloc[i]=="Enfermo") else "green")))).add_to(folium_map)

  #COMUNA 3
  df1=df_ibague[df_ibague['comuna']==3]
  for i in range(len(df1)):
    folium.Circle(location=[df1['latitude'].iloc[i],df1['longitude'].iloc[i]],radius=2,color= ('red' if (df1['estado_sanitario'].iloc[i]=="Muerto") else ( 'orange' if (df1['estado_sanitario'].iloc[i]=="Critico") else ( 'yelow' if (df1['estado_sanitario'].iloc[i]=="Enfermo") else "green")))).add_to(folium_map)
  
  #COMUNA 4
  df1=df_ibague[df_ibague['comuna']==4]
  for i in range(len(df1)):
    folium.Circle(location=[df1['latitude'].iloc[i],df1['longitude'].iloc[i]],radius=2,color= ('red' if (df1['estado_sanitario'].iloc[i]=="Muerto") else ( 'orange' if (df1['estado_sanitario'].iloc[i]=="Critico") else ( 'yelow' if (df1['estado_sanitario'].iloc[i]=="Enfermo") else "green")))).add_to(folium_map)
  
  #COMUNA 5
  df1=df_ibague[df_ibague['comuna']==5]
  for i in range(len(df1)):
    folium.Circle(location=[df1['latitude'].iloc[i],df1['longitude'].iloc[i]],radius=2,color= ('red' if (df1['estado_sanitario'].iloc[i]=="Muerto") else ( 'orange' if (df1['estado_sanitario'].iloc[i]=="Critico") else ( 'yelow' if (df1['estado_sanitario'].iloc[i]=="Enfermo") else "green")))).add_to(folium_map)
  
  #COMUNA 6
  df1=df_ibague[df_ibague['comuna']==6]
  for i in range(len(df1)):
    folium.Circle(location=[df1['latitude'].iloc[i],df1['longitude'].iloc[i]],radius=2,color= ('red' if (df1['estado_sanitario'].iloc[i]=="Muerto") else ( 'orange' if (df1['estado_sanitario'].iloc[i]=="Critico") else ( 'yelow' if (df1['estado_sanitario'].iloc[i]=="Enfermo") else "green")))).add_to(folium_map)

  #centroide
  data['Center_point'] = data['geometry'].centroid
  data["lat"] = data.Center_point.map(lambda p: p.x)
  data["long"] = data.Center_point.map(lambda p: p.y)

  for _, r in data.iterrows():
    lat = r["lat"]
    lon = r["long"]
    folium.Marker(location=[lon,lat], popup=r['COMUNAS'],icon=folium.Icon(color='lightblue',icon="home")).add_to(folium_map)

  template = """
  {% macro html(this, kwargs) %}

  <!doctype html>
  <html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>jQuery UI Draggable - Default functionality</title>
    <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    
    <script>
    $( function() {
      $( "#maplegend" ).draggable({
                      start: function (event, ui) {
                          $(this).css({
                              right: "auto",
                              top: "auto",
                              bottom: "auto"
                          });
                      }
                  });
  });

    </script>
  </head>
  <body>

  
  <div id='maplegend' class='maplegend' 
      style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
      border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
      
  <div class='legend-title'>Estado Sanitario</div>
  <div class='legend-scale'>
    <ul class='legend-labels'>
      <li><span style='background:red;opacity:0.7;'></span>Muerto</li>
      <li><span style='background:orange;opacity:0.7;'></span>Critico</li>
      <li><span style='background:yellow;opacity:0.7;'></span>Enfermo</li>
      <li><span style='background:green;opacity:0.7;'></span>Sano</li>

    </ul>
  </div>
  </div>
  
  </body>
  </html>

  <style type='text/css'>
    .maplegend .legend-title {
      text-align: left;
      margin-bottom: 5px;
      font-weight: bold;
      font-size: 90%;
      }
    .maplegend .legend-scale ul {
      margin: 0;
      margin-bottom: 5px;
      padding: 0;
      float: left;
      list-style: none;
      }
    .maplegend .legend-scale ul li {
      font-size: 80%;
      list-style: none;
      margin-left: 0;
      line-height: 18px;
      margin-bottom: 2px;
      }
    .maplegend ul.legend-labels li span {
      display: block;
      float: left;
      height: 16px;
      width: 30px;
      margin-right: 5px;
      margin-left: 0;
      border: 1px solid #999;
      }
    .maplegend .legend-source {
      font-size: 80%;
      color: #777;
      clear: both;
      }
    .maplegend a {
      color: #777;
      }
  </style>
  {% endmacro %}"""

  macro = MacroElement()
  macro._template = Template(template)

  folium_map.get_root().add_child(macro)

  return folium_map