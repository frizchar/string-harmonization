from fuzzywuzzy import fuzz  # Import the fuzz module from the fuzzywuzzy library for string matching


def find_closest_matches(set_A, set_B):
    """
    Finds the closest matches between two sets of strings using fuzzy matching.

    Parameters:
    set_A (set): A set of strings to match against.
    set_B (set): A set of strings to find matches from.

    Returns:
    list: A list of lists containing each string from set_A, its closest match from set_B, and the matching score.
    """
    results_list = []  # Initialize an empty list to store results

    # Iterate over each item in set_A
    for item_a in set_A:
        max_distance = 0  # Initialize the maximum distance (similarity score) found so far
        closest_match = None  # Initialize variable to hold the closest match

        # Iterate over each item in set_B to find the best match for item_a
        for item_b in set_B:
            distance = fuzz.ratio(item_b, item_a)  # Calculate the similarity score between item_a and item_b

            # If the calculated distance is greater than the current max_distance
            if distance > max_distance:
                max_distance = distance  # Update max_distance with the new highest score
                closest_match = item_b  # Update closest_match with the current best match

        # Append a list containing the original string from set_A, its closest match, and the similarity score
        results_list.append([item_a, closest_match, max_distance])

    return results_list  # Return the list of results


if __name__ == "__main__":
    # Example usage of the find_closest_matches function
    set_A = {'string1', 'string2', 'string3'}  # Define a set of strings to search for matches
    set_B = {'string1a', 'string2', 'string1rr', 'string3b_23', 'string3.'}  # Define a set of strings to match against

    results = find_closest_matches(set_A, set_B)  # Call the function to find closest matches
    print('results:', results)  # Print the results
