#Developer: Ashutosh Jha(realashu)
import folium
import pandas
data = pandas.read_csv("Volcanoes.txt")
elv = list(data["ELEV"])
lat = list(data["LAT"])
lon = list(data["LON"])
def color_picker(e):
    x =""
    if e<1000:
        x ="green"
    elif e>=1000 and e<2000:
        x="orange"
    elif e >=2000 and e <3000:
        x ="lightred"
    elif e >=3000 and e <4000:
        x = "red"
    else:
        x="darkred"
    return x
map1=folium.Map(location=[37.2570000,-113.6210022],zoom_start=4,tiles="Mapbox Control Room")
fv=folium.FeatureGroup(name="Volcanoes")
for el,lt,ln in zip(elv,lat,lon):
    fv.add_child(folium.Marker(location=[lt,ln],angle=90, popup=str(el) +"m.",fill_color=color_picker(el),color="grey",fill_opacity=0.8,fill=True))
fp=folium.FeatureGroup(name="Population")
fp.add_child(folium.GeoJson(data=open("wd.json", "r", encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 400000000 else 'red'}))

map1.add_child(fv)
map1.add_child(fp)
map1.add_child(folium.LayerControl())
map1.save("Map.html")
