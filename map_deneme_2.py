import folium
m = folium.Map(location=[40.75834, 30.38001])
folium.Marker(location=[40.75834, 30.38001], popup='Sakarya').add_to(m)

folium.Map(m)