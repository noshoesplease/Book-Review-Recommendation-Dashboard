import json

def create_unique_reviewer_list():

    input_path = '../data/book_data_chunk22.json'
    output_path = '../data/unique_reviewer_chunk22.json'

    review_list = []

    with open(input_path, 'r') as j:
        review_list_text = j.readlines()

    for review in review_list_text:
        review_list.append(json.loads(review))

    unique_reviewer_set = set()
    for review in review_list:
        unique_reviewer_set.add(review['reviewerID'])

    unique_reviewer_list = []
    for reviewer in review_list:
        if reviewer['reviewerID'] in unique_reviewer_set:
            unique_reviewer_list.append(reviewer)
            unique_reviewer_set.remove(reviewer['reviewerID'])

    with open(output_path, 'w') as j:
        for unique_reviewer in unique_reviewer_list:
            json.dump(unique_reviewer, j)
            j.write('\n')

create_unique_reviewer_list()