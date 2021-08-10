import time
from app import app

@app.template_filter("duration")
def duration_filter(seconds):
    if (seconds >= 3600):
        pattern = "%H:%M:%S"
    else:
        pattern = "%M:%S"
    return time.strftime(pattern, time.gmtime(seconds))

app.jinja_env.filters["duration"] = duration_filter

@app.template_filter("size")
def size_filter(bytes):
    megabytes = bytes / 1000000
    return "{:.2f}MB".format(megabytes)

app.jinja_env.filters["size"] = size_filter