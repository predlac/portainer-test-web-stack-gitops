import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host="redis")

@app.route("/")
def hello():
    try:
        visits = r.incr("counter")
    except:
        visits = "Cannot connect to Redis."
    return f"Hello World! This is an update. This page has been viewed {visits} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
