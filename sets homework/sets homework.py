our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Common destinations
common_destinations = our_routes & competitor_routes

# Unique destinations for your airline
unique_to_our_airline = our_routes - competitor_routes

# Destinations neither airline shares
neither_airline_destinations = our_routes ^ competitor_routes

print("Common destinations:", common_destinations)
print("Unique destinations for our airline:", unique_to_our_airline)
print("Destinations neither airline shares:", neither_airline_destinations)

duplicated_list = [1, 1, 2, 1, 3, 4, 1, 2, 3, 4]
deduplicated_list = []
for item in duplicated_list:
    if item not in deduplicated_list:
        deduplicated_list.append(item)
print(deduplicated_list)
