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


# Rotina de pplotagem
import matplotlib.pyplot as plt

title_font_size = '20'
axis_fontsize   = 20
figwidth        = 30
figheigh        = 5
xlabel          = 'Year'
ylabel          = 'Discharge $(m^3/s)$'
Qobs_label       = 'Qobs'
Qsim_label       = 'Qsim'
fig_format      = 'png' #.eps .ps .pdf


fig, (ax1, ax2) = plt.subplots(1, 2,figsize = (10,10))
# fig.suptitle('Sharing x per column, y per row')
# fig, ax = plt.subplots(1,2,figsize = (20,20))
rios.plot(color='blue',
             edgecolor = 'black',
             ax = ax1,
             alpha=.5)
# rios.apply(lambda x: ax1.annotate(text=x.MINI_12, xy=x.geometry.centroid.coords[0], ha='right'), axis=1);
fig.suptitle('VAZÕES NA AMAZÔNIA', fontsize=16);

l=10
Q[l][:].plot(figsize=(figwidth,figheigh), 
                        linewidth=1, color='red', 
                        fontsize=20,
                        label=Qsim_label) 
plt.xlim(pd.Timestamp(ti), pd.Timestamp(tf));plt.ylim(0, max(Q[l][:]))
plt.ylabel(ylabel, fontsize=axis_fontsize);plt.xlabel(xlabel, fontsize=axis_fontsize);
#plt.legend(fontsize=15);plt.title('Unit-Chatchment: '+str(BC_id[BC_id.index(l)]),fontsize=title_font_size)
# plt.axis('equal')
plt.show()