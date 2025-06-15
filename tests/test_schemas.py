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
    msg = f"user_id expected {USER_ID}, got {post.user_id}"
    if post.user_id != USER_ID:
        raise AssertionError(msg)
    msg = f"id expected {POST_ID}, got {post.id}"
    if post.id != POST_ID:
        raise AssertionError(msg)
    msg = f"title expected {TITLE}, got {post.title}"
    if post.title != TITLE:
        raise AssertionError(msg)
    msg = f"body expected {BODY}, got {post.body}"
    if post.body != BODY:
        raise AssertionError(msg)
    # Test aliasing and serialization
    serialized = post.model_dump(by_alias=True)
    msg = "userId alias missing in serialized output"
    if "userId" not in serialized:
        raise AssertionError(msg)
    msg = f"userId alias expected {USER_ID}, got {serialized['userId']}"
    if serialized["userId"] != USER_ID:
        raise AssertionError(msg)
