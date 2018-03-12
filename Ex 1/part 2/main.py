from googlemaps import Client
import math

def distCal(lat1, lng1, lat2, lng2):
    earthRad = 6371
    latDis = math.radians(lat2 - lat1)
    lngDis = math.radians(lng2 - lng1)
    a = math.pow(math.sin(latDis / 2),2) \
        + math.pow(math.sin(lngDis / 2),2) \
        * math.cos(math.radians(lat1))*math.cos(math.radians(lat2))
    c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
    check = earthRad * c
    return check
lat1 = float(input("Please enter latitude for location A: "))
lng1 = float(input("Please enter longitude for location A: "))
lat2 = float(input("Please enter latitude for location B: "))
lng2 = float(input("Please enter longitude for location B: "))
dist = round(distCal(lat1, lng1, lat2, lng2), 3)
print("Distance: " + str(dist) + "km")