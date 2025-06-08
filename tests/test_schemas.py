"""Test module for Post schema."""

from src._schemas.posts import Post

USER_ID = 1
POST_ID = 2
TITLE = "T"
BODY = "B"


def test_post_schema() -> None:
    """Test the Post schema fields."""
    data = {"userId": USER_ID, "id": POST_ID, "title": TITLE, "body": BODY}
    post = Post(**data)
    if post.user_id != USER_ID:
        msg = f"user_id expected {USER_ID}, got {post.user_id}"
        raise AssertionError(msg)
    if post.id != POST_ID:
        msg = f"id expected {POST_ID}, got {post.id}"
        raise AssertionError(msg)
    if post.title != TITLE:
        msg = f"title expected {TITLE}, got {post.title}"
        raise AssertionError(msg)
    if post.body != BODY:
        msg = f"body expected {BODY}, got {post.body}"
        raise AssertionError(msg)
