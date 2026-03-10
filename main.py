from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema
from database import engine
from models import Base
from database import Base, engine
Base.metadata.create_all(bind=engine)

# Create tables
Base.metadata.create_all(engine)

app = FastAPI()

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")