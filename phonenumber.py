
import phonenumbers
from phonenumbers import geocoder

# from folium import Map, Marker
number = input("Enter the number with country code: ")
# key = "get the from the opencage website"
try:
    check_number = phonenumbers.parse(number)
    number_location = geocoder.description_for_number(check_number,"en")
    print(number_location)

    from phonenumbers import carrier

    service_provider = phonenumbers.parse(number)
    print(carrier.name_for_number(service_provider,"en"))

    from opencage.geocoder import OpenCageGeocode

    geocoder = OpenCageGeocode("947c4a82e0094109801eae853f41dbc2") #or just this key in key variable up and pass the variable
    querry = str(number_location)
    result = geocoder.geocode(querry)

    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']
    print(lat,lng)
      
            #    for google map
    # map_location = Map(location=[lat,lng],zoom_start=9)
    # Marker([lat,lng], popup=number_location).add_to(map_location)
    # map_location.save("location.html")

except Exception as e:
   print(f"An error occered: {e}")