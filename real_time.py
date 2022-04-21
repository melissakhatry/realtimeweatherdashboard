pane = pn.Tabs(
    ('Real Time', pn_realtime),
    ('Refresh Weather Dashboard', pn_weather)
    ).servable()

pane
