import numpy as np


def find_best_matches(test_encodings, dataset_encodings, tolerance):
    matched_indexes = []

    for i, test_encoding in enumerate(test_encodings):
        best_match = -1
        best_distance = tolerance + 1

        for j, dataset_encoding in enumerate(dataset_encodings):
            distance = np.linalg.norm([a - b for a, b in zip(test_encoding, dataset_encoding)])

            if distance <= tolerance and distance < best_distance:
                best_match = j
                best_distance = distance

        matched_indexes.append(best_match)

    return matched_indexes
