#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Importando librarias
import datetime
import pandas as pd
import geopandas as gpd

# Localização das pastas e documentos
output_file = 'figuras/'
input_file = 'data/'
shpfdir = 'shapefiles/'
nome_dados = 'MGB-IPH_DischargeData_AmazonBasin.txt'
nome_rios = 'AmazonDrainage.shp'

# Leitura e armazenamento dos dados
ti='1998-01-01'
tf='2009-12-31'
Q = pd.read_csv(input_file+nome_dados, delimiter="\s+",engine='python',header=None) # Armazena a base de dados na variável data
Q['date'] = pd.date_range(start=ti, end=tf, freq='D');Q.set_index('date', inplace=True)
rios = gpd.read_file(shpfdir+nome_rios)
rios.tail()


# In[15]:


import plotly.express as px
import shapely.geometry
import numpy as np
lats = []
lons = []
names = []

aux = 0
for feature, name in zip(rios.geometry, rios.MINI_12): # percorre lista de cods e o nome da bacia!!!!!
    if isinstance(feature, shapely.geometry.linestring.LineString): # verifica se é uma linestring
        # O objeto LineString construído representa uma ou mais linhas lineares conectadas entre os pontos.
        linestrings = [feature] # recebe as cod

    elif isinstance(feature, shapely.geometry.multilinestring.MultiLineString): # verifica se é uma multilinestring
        linestrings = feature.geoms

    else:
        continue
    for linestrings in linestrings: # coloca as variaveis nas listas 
        x, y = linestrings.xy
        lats = np.append(lats, y)
        lons = np.append(lons, x)
        names = np.append(names, [name]*len(y))
        lats = np.append(lats, None)
        lons = np.append(lons, None)
        names = np.append(names, None)

fig = px.line_mapbox(lat=lats, lon=lons, hover_name=names, height=500) # faz o mapa com as variaveis 
fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4,
                    margin={"r":0,"t":0,"l":0,"b":0})
#fig = px.line_geo(lat=lats, lon=lons, hover_name=names, scope='south america', height=800)
fig.show()


# In[3]:





# In[4]:





# In[ ]:



