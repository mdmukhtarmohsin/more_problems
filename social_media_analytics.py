
from typing import Counter


posts = [
    {"id": 1, "user": "alice", "content": "Love Python programming!", "likes": 15, "tags": ["Python", "coding"]},
    {"id": 2, "user": "bob", "content": "Great weather today", "likes": 8, "tags": ["weather", "life"]},
    {"id": 3, "user": "alice", "content": "Data structures are fun", "likes": 22, "tags": ["Python", "learning"]},
]

users = {
    "alice": {"followers": 150, "following": 75},
    "bob": {"followers": 89, "following": 120},
}

frequent_tags = Counter([tag for post in posts for tag in post["tags"]])

most_common_tags = frequent_tags.most_common(5)

print("Most common tags:")
for tag, count in most_common_tags:
    print(f"{tag}: {count}")

most_liked_posts = sorted(posts, key=lambda x: x["likes"], reverse=True)[:3]


top_posts_by_likes = sorted(posts, key=lambda x: x["likes"], reverse=True)[:3]

print("Top 3 posts by likes:")
for post in top_posts_by_likes:
    print(f"Post ID: {post['id']}, Likes: {post['likes']}")

total_likes_per_user = {user: sum(post["likes"] for post in posts if post["user"] == user) for user in users}

print("Total likes per user:")
for user, likes in total_likes_per_user.items():
    print(f"{user}: {likes}")


get_user_summary = lambda user: f"{user} has {users[user]['followers']} followers and is following {users[user]['following']} users."

print(get_user_summary("alice"))
print(get_user_summary("bob"))

