# Geolocation Service

This web app is designed to take a street address as an input and return the latitude, longitude, and state of the address in JSON format. In order to use the API, simply add /geolcator/<street address> in the URL. For example:
  
`
localhost:5000/geolocator/1600 Pennsylvania Ave NW Washington DC 20500
`

This app also includes US state geodata from the US Census Bureau in JSON format at:

`
localhost:5000/geodata
`
