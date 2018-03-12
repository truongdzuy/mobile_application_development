from googlemaps import Client
apiKey = 'AIzaSyDgoY6l7wIw2ekbf2aYnCjUyYTKxFVG9p0'
lat = input("Please enter latitude: ")
lng = input("Please enter longitude: ")
maps = Client(apiKey)
reverseGeo = maps.reverse_geocode((lat,lng))
address = reverseGeo[0]['formatted_address']
print(address)