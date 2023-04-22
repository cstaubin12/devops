from fastapi import FastAPI
import sentry_sdk

sentry_sdk.init(
    dsn="https://74fce9d42db2443fb8e70a351c91cc8b@o4504980167524352.ingest.sentry.io/4505033051996160",

    traces_sample_rate=1.0,
)

app = FastAPI()

#route that creates and logs a sample error in sentry 
@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0


# creates a hello world message when uvicorn main:app --reload is run
@app.get("/")
async def root():
    return {"message": "Hello World"}
