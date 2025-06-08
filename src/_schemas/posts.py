"""Schema definitions for blog posts."""

from pydantic import BaseModel, Field


class Post(BaseModel):
    """Schema representing a blog post."""

    user_id: int = Field(..., alias="userId")
    id: int
    title: str
    body: str

    class Config:
        """Pydantic configuration for the Post schema."""

        populate_by_name = True
