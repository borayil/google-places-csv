import csv
from googleplaces import GooglePlaces, lang

GOOGLE_PLACES_API_KEY = '?'
DETAILS_ENABLED = False # Further details API call
LAT = 10.00 # Lattitude of search area 
LNG = 10.00 # Longitude of search area
LANGUAGE = lang.ENGLISH # Language of results from Google API
RADIUS = 50000 # Radius of search (in meters)

# --- CSV Setup ---
f = open('results.csv', 'w')
writer = csv.writer(f)
# Header setup
if DETAILS_ENABLED:
    csv_header = ["Name", "Geo Location", "Google Places ID"]
else:
    csv_header = ["Name", "Address", "Telephone Number", "Website"] # TODO: Add all fields that come with details
writer.writerow(csv_header)

# Google Places API wrapper instance
google_places = GooglePlaces(GOOGLE_PLACES_API_KEY)

# Setup the query words here
queries = ["Joe's BBQ", "barbeque and grill"] # special names, type of place etc.

# --- Query loop ---
# TODO: Add timeout handling
for q in queries:
    query_result = google_places.text_search(query=q, lat_lng={'lat': LAT, 'lng': LNG}, language=LANGUAGE, radius=RADIUS)
    for place in query_result.places:
        if DETAILS_ENABLED:
            place.get_details(language=LANGUAGE) # Further API call to get details
            row_data = [place.name, place.formatted_address, place.local_phone_number, place.website, place.url]
        else:
            row_data = [place.name, place.geo_location, place.place_id]
        writer.writerow(row_data) # Write to CSV file

# Close CSV file
f.close()


