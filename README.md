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

# 📸 Screenshots



```
<img width="1145" height="242" alt="Screenshot 2026-03-10 at 7 36 27 PM" src="https://github.com/user-attachments/assets/7fefbaad-72ec-469e-a25b-6ac5ecdbf0f9" />
<img width="1310" height="310" alt="Screenshot 2026-03-10 at 7 52 24 PM" src="https://github.com/user-attachments/assets/3e3ba921-7241-44a6-808e-b86268067299" />
<img width="1204" height="390" alt="Screenshot 2026-03-10 at 7 35 17 PM" src="https://github.com/user-attachments/assets/b4b89626-02eb-4a91-a8b5-f6fd5d5ab089" />
<img width="1129" height="220" alt="Screenshot 2026-03-10 at 7 34 13 PM" src="https://github.com/user-attachments/assets/9c98fb7e-4556-4723-b3cb-5229b0d26826" />
<img width="1097" height="336" alt="Screenshot 2026-03-10 at 7 21 11 PM" src="https://github.com/user-attachments/assets/8ffaaa60-e4fc-4458-8c8c-a494bdb4a895" />

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
