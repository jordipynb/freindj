from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from reindj import Freindj

app = FastAPI()
system = Freindj("cranfield", "vector")

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "Welcome to Freindj! To view an evaluation navigate to /evaluate. To search a query navigate to /search?qry=<msg>."


@app.get("/evaluate")
def evaluate():
    return system.evaluate()


@app.get("/search")
def search(qry: str):
    try:
        if qry == "": return []
        return system.doc_query(qry)
    except Exception:
        raise HTTPException(status_code=501, detail="Sorry! Unexpected error in execution of Freindj System.")