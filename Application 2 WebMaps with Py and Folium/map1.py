import folium
map = folium.Map(location=[9.023, 38.84], zoom_start=6, titles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
for coordinates in [[9.023, 38.84], [9.023922774520175, 38.84411708394214]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")