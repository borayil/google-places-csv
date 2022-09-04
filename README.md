# google-places-csv
This Python script uses Google Places API to search for the defined queries and saves them nicely to a CSV file. Useful when searching for a large set of places on Google.  

# How To
The initial code section is where the query parameters are setup.
```python
GOOGLE_PLACES_API_KEY = '?'
DETAILS_ENABLED = False # Further details API call
LAT = 10.00 # Lattitude of search area 
LNG = 10.00 # Longitude of search area
LANGUAGE = lang.ENGLISH # Language of results from Google API
RADIUS = 50000 # Radius of search (in meters)
```
Place your Google Places API key within `GOOGLE_PLACES_API_KEY`. Below this, you will also find other parameters for the search.  

Prepare and place your query keywords within a list of strings named `queries` before the query loop starts.
```python
# Setup the query words here
queries = ["Joe's BBQ", "barbeque and grill"] # special names, type of place etc.
```
After this, the query loop will take care of calling the API and then saving the results in a CSV format file named `results.csv`

## API Wrapper
The wrapper [python-google-places](https://github.com/slimkrazy/python-google-places) allows the use of the Google Places API in a simplistic and efficient way.  
For more information about the API (platforms, pricing, requests, terms) see [Overview | Places API - Google Developers](https://developers.google.com/maps/documentation/places/web-service/overview)

