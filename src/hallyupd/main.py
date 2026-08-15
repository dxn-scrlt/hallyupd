from fastapi import FastAPI

app = FastAPI(
    title="HallyuPD API",
    description="K-Pop RPD discovery API",
)

@app.get("/")
def root():
    return {"message": "Hello from hallyupd!"}