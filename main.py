from fuzzywuzzy import fuzz

list_A = ['string1', 'string2', 'string3']
list_B = ['string1a', 'string2', 'string1rr', 'string3b_23', 'string3.']

results_list = []

for item_b in list_B:
    max_distance = 0
    closest_match = None
    for item_a in list_A:
        distance = fuzz.ratio(item_b, item_a)
        if distance > max_distance:
            max_distance = distance
            closest_match = item_a
    results_list.append([item_b, closest_match, max_distance])

print('results:', results_list)
