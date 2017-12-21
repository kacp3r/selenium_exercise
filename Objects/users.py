import csv


def get_user_data(file_name):
    """Extracts a list of user dicts with email and password from CSV text file."""
    users = []
    data_file = open(file_name, "r")
    reader = csv.reader(data_file)
    # skip headers
    next(reader, None)
    # add rows from reader to list
    for row in reader:
        users.append({})
        users[-1]['email'] = row[0]
        users[-1]['password'] = row[1]
    return users
