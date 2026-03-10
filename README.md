# 🚀 GraphQL Blog Content Management System

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green?logo=fastapi)
![GraphQL](https://img.shields.io/badge/GraphQL-Strawberry-pink?logo=graphql)
![Database](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)

A **GraphQL-based Blog Content Management System** built using **FastAPI, Strawberry GraphQL, SQLAlchemy, and SQLite**.

This project demonstrates how to build a **modern API-driven blog platform** where users can manage:

* Authors
* Categories
* Tags
* Blog Posts
* Comments

All operations are performed through **GraphQL Queries and Mutations**.

---

# ✨ Features

🧑 Author Management
📂 Category Management
🏷 Tag Management
📝 Blog Post Creation
🚀 Publish Blog Posts
💬 Comment System
⚡ GraphQL Queries & Mutations
🗄 SQLite Database Integration

---

# 🛠 Tech Stack

| Technology             | Usage                  |
| ---------------------- | ---------------------- |
| **Python**             | Backend Language       |
| **FastAPI**            | Web Framework          |
| **Strawberry GraphQL** | GraphQL Implementation |
| **SQLAlchemy**         | ORM                    |
| **SQLite**             | Database               |
| **Uvicorn**            | ASGI Server            |

---

# 📁 Project Structure

```
GRAPHQL-MINI-PROJECT
│
├── venv/                # Virtual environment
│
├── blog.db              # SQLite database
│
├── database.py          # Database connection setup
│
├── models.py            # SQLAlchemy database models
│
├── schema.py            # GraphQL schema (Queries & Mutations)
│
├── main.py              # FastAPI application entry point
│
├── seed.py              # Sample data generator
│
└── README.md            # Project documentation
```

---

# ⚙️ Installation



### 1 Create Virtual Environment

```
python -m venv venv
```

---

### 2 Activate Environment

Mac / Linux

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

---

### 3 Install Dependencies

```
pip install fastapi uvicorn strawberry-graphql sqlalchemy
```

---

### 4 Run Server

```
python -m uvicorn main:app --reload
```

Open GraphQL Playground:

```
http://127.0.0.1:8000/graphql
```

---

# 🔎 Example GraphQL Queries

### Create Author

```graphql
mutation{
  createAuthor(name:"Antriksh",email:"test@test.com",bio:"Developer"){
    id
    name
  }
}
```

---

### Create Post

```graphql
mutation{
  createPost(input:{
    title:"GraphQL Blog"
    content:"GraphQL is powerful"
    authorId:1
    categoryId:1
    tagIds:[1]
  }){
    id
    title
  }
}
```

---

### Publish Post

```graphql
mutation{
  publishPost(postId:1){
    id
    status
  }
}
```

---

### Query Posts

```graphql
query{
  posts{
    id
    title
    status
  }
}
```

---


# 📚 Learning Outcomes

Through this project you will learn:

* GraphQL API development
* FastAPI integration
* SQLAlchemy ORM
* Query & Mutation design
* API-driven backend architecture

---

# 🎓 Academic Purpose

This project was created as a **GraphQL Mini Project** to demonstrate the implementation of a **Blog Content Management System using GraphQL APIs**.

---

⭐ If you like this project, consider giving it a **star on GitHub**!
