import pandas
import folium
import csv

#kraje_slovenske = f"http://download.freemap.sk/AdminLevel/kraje.json"




df = pandas.read_csv('emisie.csv')
INDICATOR = 'Kraj'
data = df[df['Kraj'] == INDICATOR]
max_year = data['Rok'].max()
data = data[data['Rok'] == max_year]

map_data = data[['Kraj', 'Hodnota']]

m = folium.Map(location=[49.130606, 18.681453], zoom_start=7)
folium.Choropleth(
    geo_data='kraje.json',
    data=map_data,
    columns=['Kraj', 'Hodnota'],
    key_on='properties.REF',
    fill_color='YlGnBu',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Produkcia emisii v tonach za rok 2019'
).add_to(m)
ms = m.save('mapa.html')
