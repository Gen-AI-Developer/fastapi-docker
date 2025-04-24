from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    main()
    return {"/": "Hello from fastapi-docker!"}

def main() -> str:
    return "Hello from fastapi-docker!"
