from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.utils.tags import tags_metadata
description = """
GroupChat 
"""

app = FastAPI(title="Group Chat Application", openapi_tags=tags_metadata,
              description=description)
origins = [
    '*'
]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['*'],
                   allow_headers=['*'])

