import uvicorn
import prometheus_client
from fastapi import FastAPI, Response


app = FastAPI()

hello_world_count = prometheus_client.Counter(
    "hello_world_count", "Number of hello world operations :)"
)


@app.get("/hello-word")
def hello_word():
    hello_world_count.inc()
    return "Hello World!"


@app.get("/metrics")
def get_metrics():
    return Response(
        content=prometheus_client.generate_latest(),
        media_type="text/plain",
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
