from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
async def read_root():
    return {"status": "ok"}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
