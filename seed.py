from datetime import datetime
from database import SessionLocal
from models import Author, Category, Tag, Post, Comment


def seed_data():
    db = SessionLocal()

    # Clear existing data (optional but recommended for testing)
    db.query(Comment).delete()
    db.query(Post).delete()
    db.query(Tag).delete()
    db.query(Category).delete()
    db.query(Author).delete()
    db.commit()

    # ================= AUTHORS =================
    author1 = Author(
        name="Antriksh Manwadkar",
        bio="Full Stack Developer and Tech Blogger",
        email="antriksh@example.com",
        avatar_url="https://example.com/avatar1.png",
        joined_date=datetime.utcnow(),
    )

    author2 = Author(
        name="Jane Smith",
        bio="Backend Engineer & GraphQL Enthusiast",
        email="jane@example.com",
        avatar_url="https://example.com/avatar2.png",
        joined_date=datetime.utcnow(),
    )

    db.add_all([author1, author2])
    db.commit()

    # ================= CATEGORIES =================
    category1 = Category(
        name="Technology",
        slug="technology",
        description="All about tech"
    )

    category2 = Category(
        name="Programming",
        slug="programming",
        description="Coding tutorials and guides"
    )

    db.add_all([category1, category2])
    db.commit()

    # ================= TAGS =================
    tag1 = Tag(name="GraphQL", slug="graphql")
    tag2 = Tag(name="Python", slug="python")
    tag3 = Tag(name="FastAPI", slug="fastapi")
    tag4 = Tag(name="Backend", slug="backend")

    db.add_all([tag1, tag2, tag3, tag4])
    db.commit()

    # ================= POSTS =================
    post1 = Post(
        title="Getting Started with GraphQL",
        content="Complete beginner guide to GraphQL...",
        published_date=datetime.utcnow(),
        status="published",
        author_id=author1.id,
        category_id=category2.id,
    )

    post2 = Post(
        title="FastAPI + Strawberry Setup",
        content="How to build GraphQL APIs using FastAPI...",
        published_date=datetime.utcnow(),
        status="draft",
        author_id=author1.id,
        category_id=category2.id,
    )

    post3 = Post(
        title="Advanced Backend Architecture",
        content="Deep dive into scalable backend systems...",
        published_date=datetime.utcnow(),
        status="archived",
        author_id=author2.id,
        category_id=category1.id,
    )

    db.add_all([post1, post2, post3])
    db.commit()

    # ================= POST-TAG RELATION =================
    post1.tags = [tag1, tag2]
    post2.tags = [tag2, tag3]
    post3.tags = [tag4]

    db.commit()

    # ================= COMMENTS =================
    comment1 = Comment(
        content="Great article!",
        author_name="John Doe",
        post_id=post1.id,
        created_at=datetime.utcnow(),
        is_approved=True,
    )

    comment2 = Comment(
        content="Very helpful explanation!",
        author_name="Alice",
        post_id=post1.id,
        created_at=datetime.utcnow(),
        is_approved=False,
    )

    comment3 = Comment(
        content="Nice backend insights.",
        author_name="Bob",
        post_id=post3.id,
        created_at=datetime.utcnow(),
        is_approved=True,
    )

    db.add_all([comment1, comment2, comment3])
    db.commit()

    db.close()
    print("✅ Database seeded successfully!")


if __name__ == "__main__":
    seed_data()