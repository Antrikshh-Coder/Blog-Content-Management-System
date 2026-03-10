import strawberry
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Author, Post, Category, Tag, Comment


# ================= TYPES =================

@strawberry.type
class AuthorType:
    id: int
    name: str
    email: str
    bio: Optional[str]
    joined_date: datetime


@strawberry.type
class CategoryType:
    id: int
    name: str
    slug: str
    description: Optional[str]


@strawberry.type
class TagType:
    id: int
    name: str
    slug: str


@strawberry.type
class CommentType:
    id: int
    content: str
    author_name: str
    created_at: datetime
    is_approved: bool
    post_id: int


@strawberry.type
class PostType:
    id: int
    title: str
    content: str
    status: str
    published_date: Optional[datetime]
    author_id: int
    category_id: int


# ================= INPUT TYPES =================

@strawberry.input
class CreatePostInput:
    title: str
    content: str
    author_id: int
    category_id: int
    tag_ids: List[int]


@strawberry.input
class CreateCommentInput:
    post_id: int
    author_name: str
    content: str


# ================= MUTATIONS =================

@strawberry.type
class Mutation:

    # Create Author
    @strawberry.mutation
    def create_author(self, name: str, email: str, bio: Optional[str] = None) -> AuthorType:
        db: Session = SessionLocal()

        author = Author(
            name=name,
            email=email,
            bio=bio,
            joined_date=datetime.utcnow()
        )

        db.add(author)
        db.commit()
        db.refresh(author)

        return author


    # Create Category
    @strawberry.mutation
    def create_category(self, name: str, slug: str, description: Optional[str] = None) -> CategoryType:
        db: Session = SessionLocal()

        category = Category(
            name=name,
            slug=slug,
            description=description
        )

        db.add(category)
        db.commit()
        db.refresh(category)

        return category


    # Create Tag
    @strawberry.mutation
    def create_tag(self, name: str, slug: str) -> TagType:
        db: Session = SessionLocal()

        tag = Tag(
            name=name,
            slug=slug
        )

        db.add(tag)
        db.commit()
        db.refresh(tag)

        return tag


    # Create Post
    @strawberry.mutation
    def create_post(self, input: CreatePostInput) -> PostType:
        db: Session = SessionLocal()

        post = Post(
            title=input.title,
            content=input.content,
            author_id=input.author_id,
            category_id=input.category_id,
            status="draft"
        )

        db.add(post)
        db.commit()
        db.refresh(post)

        # attach tags
        tags = db.query(Tag).filter(Tag.id.in_(input.tag_ids)).all()
        post.tags = tags
        db.commit()

        return post


    # Publish Post
    @strawberry.mutation
    def publish_post(self, post_id: int) -> PostType:
        db: Session = SessionLocal()

        post = db.query(Post).filter(Post.id == post_id).first()

        if not post:
            raise Exception("Post not found")

        post.status = "published"
        post.published_date = datetime.utcnow()

        db.commit()
        db.refresh(post)

        return post


    # Create Comment
    @strawberry.mutation
    def create_comment(self, input: CreateCommentInput) -> CommentType:
        db: Session = SessionLocal()

        comment = Comment(
            content=input.content,
            author_name=input.author_name,
            post_id=input.post_id,
            created_at=datetime.utcnow(),
            is_approved=False
        )

        db.add(comment)
        db.commit()
        db.refresh(comment)

        return comment


# ================= QUERIES =================

@strawberry.type
class Query:

    @strawberry.field
    def authors(self) -> List[AuthorType]:
        db: Session = SessionLocal()
        return db.query(Author).all()


    @strawberry.field
    def categories(self) -> List[CategoryType]:
        db: Session = SessionLocal()
        return db.query(Category).all()


    @strawberry.field
    def tags(self) -> List[TagType]:
        db: Session = SessionLocal()
        return db.query(Tag).all()


    @strawberry.field
    def posts(self) -> List[PostType]:
        db: Session = SessionLocal()
        return db.query(Post).all()


    @strawberry.field
    def post(self, id: int) -> Optional[PostType]:
        db: Session = SessionLocal()
        return db.query(Post).filter(Post.id == id).first()


    @strawberry.field
    def comments(self, post_id: int) -> List[CommentType]:
        db: Session = SessionLocal()
        return db.query(Comment).filter(Comment.post_id == post_id).all()


# ================= SCHEMA =================

schema = strawberry.Schema(query=Query, mutation=Mutation)