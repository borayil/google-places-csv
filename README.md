# google-places-csv
This Python script uses Google Places API to search for the defined queries and saves them nicely to a CSV file. Useful when searching for a large set of places on Google.  

# How To
Place your Google Places API key within `GOOGLE_PLACES_API_KEY`. Below this, you will also find other parameters for the search. Change them accordingly.  
Prepare and place your query keywords within the list `queries` which is initialized as  
`queries = ["Joe's BBQ", "barbeque and grill"]`  
After this, the query loop will take care of calling the API and then saving the results in a CSV format file named `results.csv`

# API Wrapper
The wrapper [python-google-places](https://github.com/slimkrazy/python-google-places) allows the use of the Google Places API in a simplistic and efficient way.  
For more information about the API (platforms, pricing, requests, terms) see [Overview | Places API - Google Developers](https://developers.google.com/maps/documentation/places/web-service/overview)

