def streaming_weather_data(**kwargs):
    """
    callback function 
    get San Francisco weather data 
    """
    df = weather_data(['San Francisco'])
    df['time'] = [pd.Timestamp.now()]
    return df.set_index('time')

# Make a streaming dataframe 
df = PeriodicDataFrame(streaming_weather_data, interval='30s')

# panel dashboard for streaming data 
pn_realtime = pn.Column(
    pn.Row(
      df[['Temprature']].hvplot.line(title='Temprature', backlog=1000),
      df[['Humidity']].hvplot.line(title='Humidity', backlog=1000)),
  df[['Wind Speed']].hvplot.line(title='Wind Speed', backlog=1000)
)
