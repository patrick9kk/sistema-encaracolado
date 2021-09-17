#! / usr / bin / env python
# codificação: utf-8

# Em [5]:


# importando bibliotecas !!
importar  plotly . expresso  como  px
importar  plotly . grafos_objetos à  medida que  avançam
importar  pandas  como  pd
importar  data e hora

# pegando os dados e colocando dados!
ti  =  '1998-01-01'
tf  =  '2009-12-31'
df  =  pd . read_csv ( 'C: / Users / Desktop / APC TRAB / data / MGB-IPH_DischargeData_AmazonBasin.txt' , delimiter = "\ s +" , engine = 'python' , header = None )
data  =  pd . intervalo_de_datas ( início = ti , fim = tf , freq = 'D' )
df [ 'data' ] =  data ;
df . set_index ( 'data' , inplace = True )
# df.tail ()


# Em [31]:


# colocando na var intervalo o intervalo para não escrever todos ex y [1,2,3,4,5,6,7,8]
intervalo  = [ x + 1  para  x  no  intervalo ( 0 , 2 )]

# plootando o grafico
fig  =  px . linha ( df , x = data , y = intervalo )

# titulo e essa linha que mostra os dados so de passar na região
fig . update_layout ( hovermode = 'x unificado' , title_text = 'Vazões do (s) rio (s)' , title_x = 0,5 )
fig . show ()
# !!!!!!!!!!! falta arrumar legenda e deixar bonito e no futoro adicionar o valor do rio que o usuario clicar !!!!!!!!!!!!


# No[ ]:


