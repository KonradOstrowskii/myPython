
import folium
import pandas as pd
import json

data = pd.read_csv('Volcanoes.txt')
lat = list(data["LAT"])
lon = list(data["LON"])
elev =list(data["ELEV"])
name = list(data["NAME"])
vol = " Volcano"


def color_maker(elevation):
     if elevation <=999:
          return "green"
     elif 1000 <= elevation <=2000:
          return "orange"
     else:
          return "red"
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
m = folium.Map(location=[38.7356,-102.9289],zoom_start=7,tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
m.add_child(folium.Marker(location=[32.7356,-16.9289],popup="marker",icon=folium.Icon(color='green')))
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name + vol , name + vol, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = str(color_maker(el)))))

data1 = json.load(open('world.json', encoding='utf-8-sig'))

fgp = folium.FeatureGroup(name = "Wrold Population")    

fgp.add_child(folium.features.GeoJson(data=data1,  
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 20000000 else 'yellow' 
if 20000000 <= x['properties']['POP2005'] < 50000000 else 'orange' if 50000000 <= x['properties']['POP2005'] < 100000000
else 'red'}, 
tooltip = folium.features.GeoJsonTooltip(fields=['NAME','AREA','POP2005'],
aliases=['NAME:','AREA:','POPULATION:'],
style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"))))


m.add_child(fg)
m.add_child(fgp)
m.add_child(folium.LayerControl())


m.save("map.html")
