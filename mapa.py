#Lendo os dados
import geopandas as gpd
shpfdir = 'shapefiles/'
nome_rios = 'AmazonDrainage.shp'

rios = gpd.read_file(shpfdir+nome_rios)
rios.tail()


#Armazenando as coordenadas em listas
import plotly.express as px
import shapely.geometry
import numpy as np
lats = []
lons = []
names = []

for feature, name in zip(rios.geometry, rios.MINI_12): #Itera uma lista com o nome e coordenadas das bacias
    #Verifica se feature é linestrings ou multilinestring e armazena em uma variavel de forma iteravel
    if isinstance(feature, shapely.geometry.linestring.LineString):
        linestrings = [feature]
    elif isinstance(feature, shapely.geometry.multilinestring.MultiLineString):
        linestrings = feature.geoms
    else:
        continue
    for linestrings in linestrings: #Armazena latitude, longitude e nomes em suas respectivas listas
        x, y = linestrings.xy
        lats = np.append(lats, y)
        lons = np.append(lons, x)
        names = np.append(names, [name]*len(y))
        lats = np.append(lats, None)
        lons = np.append(lons, None)
        names = np.append(names, None)

#Construção do mapa
fig = px.line_mapbox(lat=lats, lon=lons, hover_name=names, height=500)
fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4,
                    margin={"r":0,"t":0,"l":0,"b":0})
fig.show()