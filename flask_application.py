# flask_application.py

from flask import Flask, jsonify
from data import users, posts, comments

flask_app = Flask(__name__)


@flask_app.route('/')
def hello():
    return "Hello, Flask!"


# 1. List available users
@flask_app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# 2. Show detailed info of a user profile by user id
@flask_app.route('/user/<user_id>', methods=['GET'])
def get_user_profile(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

# 3. List all posts for a specific user
@flask_app.route('/user/<user_id>/posts', methods=['GET'])
def get_user_posts(user_id):
    user_posts = [post for post in posts if post["user_id"] == user_id]
    if user_posts:
        return jsonify(user_posts), 200
    return jsonify({"error": "No posts found for this user"}), 404



# 4. List available posts
@flask_app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts), 200

# 5. List all comments for a specific post
@flask_app.route('/post/<post_id>/comments', methods=['GET'])
def get_post_comments(post_id):
    post_comments = [comment for comment in comments if comment["post_id"] == post_id]
    if post_comments:
        return jsonify(post_comments), 200
    return jsonify({"error": "No comments found for this post"}), 404

if __name__ == '__main__':
     flask_app.run(port=5002, debug=True)  # Run this API on port 5002
