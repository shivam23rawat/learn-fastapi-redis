"""Schema definitions for blog posts."""

from pydantic import BaseModel, ConfigDict, Field


class Post(BaseModel):
    """Schema representing a blog post."""

    user_id: int = Field(..., alias="userId")
    id: int
    title: str
    body: str

    model_config = ConfigDict(populate_by_name=True)
