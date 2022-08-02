
import folium
import pandas as pd

data = pd.read_csv('Volcanoes.txt')
lat = list(data["LAT"])
lon = list(data["LON"])
m = folium.Map(location=[32.7356,6.9289],zoom_start=7,tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
m.add_child(folium.Marker(location=[32.7356,-16.9289],popup="marker",icon=folium.Icon(color='green')))
for lt,ln in zip(lat,lon):
     fg.add_child(folium.Marker(location=[lt,ln],popup="marker",icon=folium.Icon(color='green')))

m.add_child(fg)

m.save("map.html")
print(data)


