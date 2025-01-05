# Import Meteostat library and dependencies
import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Import geocoder to determine user location
import geocoder
g = geocoder.ip('me')

current_date = datetime.datetime.now()

# Set time period
start = datetime.datetime(2010, current_date.month, current_date.day)
end = datetime.datetime(current_date.year, current_date.month, current_date.day)

# Create Point for Vancouver, BC
location = Point(g.lat, g.lng, 10)

# Get daily data for 2018
data = Daily(location, start, end)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()