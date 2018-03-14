from prometheus_client import start_http_server, Summary, Counter, Gauge, Histogram
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('myfake_request_processing_seconds', 'Description of summary, Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8111)

    # examples for counter/gauge/summary/histogram
    c = Counter('myfake_failures_total', 'Description of counter')
    g = Gauge('myfake_inprogress_requests', 'Description of gauge')
    s = Summary('myfake_summary_request_latency_seconds', 'Description of summary')
    h = Histogram('myfake_histogram_request_latency_seconds', 'Description of histogram')
    while True:
        # counter example
        c.inc()  # Increment by 1
        # c.inc(random.random())  # Increment by given value

        # gauge example
        g.inc()  # Increment by 1
        # g.dec(10)  # Decrement by given value
        # g.set(4.2)  # Set to a given value

        # summary example
        s.observe(1.1)  # Observe 1.1 (seconds in this case)
        # Generate some requests.
        process_request(random.random())

        # histogram example
        h.observe(4.7)  # Observe 4.7 (seconds in this case)
