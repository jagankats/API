import pyowm

# free OWM Current Weather API KEY & Authentication
weather_key = 'YOUR OWM Current Weather API KEY'
weather_owm = pyowm.OWM(weather_key)
weather_mgr = weather_owm.weather_manager()

# Search for current weather in London (Great Britain) and get details
location = weather_mgr.weather_at_place('Ludhiana,IN')
weather_report = location.weather

# to get reference time of connection
ref_time = 'Date & Time: '+str(weather_report.reference_time(timeformat='date').strftime('%d-%b-%Y %H:%M:%S'))
print(ref_time)

# get the status of weather condition
status = 'Weather Condition: '+str(weather_report.detailed_status)
print(status)

# get the speed of wind in km/hour
wind_speed = 'Wind Speed: '+str(weather_report.wind()['speed'])+' km/h'
print(wind_speed)

# for humidity percentage
humidity = 'Humidity: '+str(weather_report.humidity)+' %'
print(humidity)

# attach degree celsius symbol to all temperature related variables
degree_celsius = str(u"\N{DEGREE SIGN}")+'C'
current_temp = 'Temperature: '+str(weather_report.temperature('celsius')['temp'])+degree_celsius
max_temp = 'Max Temperature: '+str(weather_report.temperature('celsius')['temp_max'])+degree_celsius
min_temp = 'Min Temperature: '+str(weather_report.temperature('celsius')['temp_min'])+degree_celsius
feels_like_temp = 'Feels Like: '+str(weather_report.temperature('celsius')['feels_like'])+degree_celsius
print(current_temp, max_temp, min_temp, feels_like_temp)

# to get the percentage of clouds in weather
clouds = 'Cloudiness: '+str(weather_report.clouds) + ' %'
print(clouds)


# free OWM Agro API KEY & Authentication
agro_key = 'YOUR OWM Agro API KEY'
agro_owm = pyowm.OWM(agro_key)
agro_mgr = agro_owm.agro_manager()

# free OWM Agro API Polygon id & Authentication
pol_id = 'YOUR Created Polygon ID of Aggriculture Field'
field_polygon = agro_mgr.get_polygon(pol_id)
soil = agro_mgr.soil_data(field_polygon)

# to get temperature of the soil surface
surface_temp = 'Surface Temp of Soil: '+str(soil.surface_temp(unit='celsius'))+degree_celsius
print(surface_temp)

# to get the temperature of soil at 10cm of depth
temp_at_10cm = 'Soil Temp at 10cm of Depth: '+str(soil.ten_cm_temp(unit='celsius'))+degree_celsius
print(temp_at_10cm)

# to get moisture content in soil
soil_moisture = 'Soil Moisture: '+str(soil.moisture*100) + ' %'
print(soil_moisture)
