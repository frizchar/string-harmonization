from fuzzywuzzy import fuzz


def find_closest_matches(set_A, set_B):
    results_list = []

    for item_a in set_A:
        max_distance = 0
        closest_match = None
        for item_b in set_B:
            distance = fuzz.ratio(item_b, item_a)
            if distance > max_distance:
                max_distance = distance
                closest_match = item_b
        results_list.append([item_a, closest_match, max_distance])

    return results_list


if __name__ == "__main__":
    # Example usage
    set_A = {'string1', 'string2', 'string3'}
    set_B = {'string1a', 'string2', 'string1rr', 'string3b_23', 'string3.'}

    results = find_closest_matches(set_A, set_B)
    print('results:', results)
