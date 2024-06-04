import folium
map = folium.Map(location=[9.023922774520175, 38.84411708394214], zoom_start=6, tiles="Mapbox Bright")

map.add_child(folium.Marker())

map.save("Map1.html")