from googlemaps import Client
apiKey = 'AIzaSyDP0pM9ag___m0xGd6peTDdVRTGyjRgv80'
lat1 = input("Please enter latitude for location A: ")
lng1 = input("Please enter longitude for location A: ")
lat2 = input("Please enter latitude for location B: ")
lng2 = input("Please enter longitude for location B: ")
maps = Client(apiKey)
distMatrix = maps.distance_matrix((lat1,lng1),(lat2,lng2))
dist = distMatrix['rows'][0]['elements'][0]['distance']['text']
print("Distance: " + dist)