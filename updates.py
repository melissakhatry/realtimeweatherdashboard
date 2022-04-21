cities = ['San Francisco', 'Los Angeles', 'Santa Barbara', 'Sacramento', 'Fresno','San Diego', 'San Luis Obispo']

def weather_plot(col, cities=cities):
    """
    plot weather data on a map 
    col: 'Temprature', 'Humidity', 'Wind Speed'
    """
    df = weather_data(cities)
    df['x'], df['y'] = lnglat_to_meters(df['lon'], df['lat'])
    table = hv.Table(df[['name', col]]).opts(width=800)
    points = df.hvplot.scatter('x','y', c=col, cmap='bkr', hover_cols=['name'])
    map_tiles  = EsriImagery().opts(alpha=0.5, width=900, height=480, bgcolor='white')
    return  pn.Column(points * map_tiles, table)
