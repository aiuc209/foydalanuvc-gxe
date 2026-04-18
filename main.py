def extract_info(users):
    return [(user['username'], user['email']) for user in users]

users = [
    {'username': 'john', 'email': 'john@example.com', 'age': 25},
    {'username': 'jane', 'email': 'jane@example.com', 'age': 30},
    {'username': 'bob', 'email': 'bob@example.com', 'age': 35}
]

result = extract_info(users)
print(result)
