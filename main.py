from fastapi import FastAPI
import sentry_sdk

sentry_sdk.init(
    dsn="https://c7545b3fcce64308b622f875ff9a7ba1@o4505059889315840.ingest.sentry.io/4505059892527104",

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
