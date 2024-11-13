# data.py

users = [
    {"id": "1", "name": "James", "email": "james@example.com"},
    {"id": "2", "name": "Alice", "email": "alice@example.com"},
    {"id": "3", "name": "Bob", "email": "bob@example.com"}
]

posts = [
    {"id": "101", "user_id": "1", "title": "James's first post", "content": "Hello world!"},
    {"id": "102", "user_id": "1", "title": "James's second post", "content": "Another post!"},
    {"id": "103", "user_id": "2", "title": "Alice's post", "content": "Welcome to my profile!"},
    {"id": "104", "user_id": "3", "title": "Bob's post", "content": "This is Bob speaking."}
]

comments = [
    {"id": "201", "post_id": "101", "content": "Great post!"},
    {"id": "202", "post_id": "101", "content": "Interesting thoughts!"},
    {"id": "203", "post_id": "102", "content": "Thanks for sharing!"},
    {"id": "204", "post_id": "104", "content": "Nice to meet you, Bob!"}
]
