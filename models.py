from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Boolean,
    ForeignKey,
    Table
)
from sqlalchemy.orm import relationship
from database import Base


# ==============================
# MANY-TO-MANY ASSOCIATION TABLE
# ==============================

post_tag = Table(
    "post_tag",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)


# ==============================
# AUTHOR MODEL
# ==============================

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    bio = Column(Text)
    email = Column(String, unique=True, nullable=False)
    avatar_url = Column(String)
    joined_date = Column(DateTime)

    posts = relationship("Post", back_populates="author", cascade="all, delete")


# ==============================
# CATEGORY MODEL
# ==============================

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    description = Column(Text)

    posts = relationship("Post", back_populates="category", cascade="all, delete")


# ==============================
# TAG MODEL
# ==============================

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)

    posts = relationship(
        "Post",
        secondary=post_tag,
        back_populates="tags"
    )


# ==============================
# POST MODEL
# ==============================

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    published_date = Column(DateTime)
    status = Column(String, default="draft")

    author_id = Column(Integer, ForeignKey("authors.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))

    # Relationships
    author = relationship("Author", back_populates="posts")
    category = relationship("Category", back_populates="posts")

    tags = relationship(
        "Tag",
        secondary=post_tag,
        back_populates="posts"
    )

    comments = relationship(
        "Comment",
        back_populates="post",
        cascade="all, delete"
    )


# ==============================
# COMMENT MODEL
# ==============================

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    author_name = Column(String, nullable=False)
    created_at = Column(DateTime)
    is_approved = Column(Boolean, default=False)

    post_id = Column(Integer, ForeignKey("posts.id"))

    post = relationship("Post", back_populates="comments")