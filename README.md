# google-places-csv
This Python script uses Google Places API to search for the defined queries and saves them nicely to a CSV file. Useful when searching for a large set of places on Google.  

# How To
The initial code section is where the query parameters are setup.
```python
GOOGLE_PLACES_API_KEY = '???'
DETAILS_ENABLED = False # Further details API call
LAT = 52.3676 # Lattitude of search area 
LNG = 4.9041 # Longitude of search area
LAT_LNG = {'lat': LAT, 'lng': LNG}
LANGUAGE = lang.ENGLISH # Language of results from Google API
RADIUS = 1000 # Radius of search (in meters)
```
Place your Google Places API key within `GOOGLE_PLACES_API_KEY`. Below this, you will also find other parameters for the search. Note that `DETAILS_ENABLED` should be set to `True` if extra details such as address and phone number are needed in the result. (This results in an extra API call!)

Prepare and place your query keywords within a list of strings named `queries` before the query loop starts.
```python
# Setup the query words here
queries = ["bbq", "grill"] # keywords, type of place etc.
```
After this, the query loop will take care of calling the API and then saving the results in a CSV format file named `results.csv`

## Google Places API Wrapper
The wrapper [python-google-places](https://github.com/slimkrazy/python-google-places) allows the use of the Google Places API in a simplistic and efficient way. It has other search functions and parameters as well which are not used in this script.
For more information about the API (platforms, pricing, requests, terms) see [overview of the Places API](https://developers.google.com/maps/documentation/places/web-service/overview)

