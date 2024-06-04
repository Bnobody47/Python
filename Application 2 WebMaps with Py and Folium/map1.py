import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
map.save("Map1.html")