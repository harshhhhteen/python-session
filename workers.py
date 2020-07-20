import requests
import redis
from concurrent.futures import ThreadPoolExecutor
import time

def worker(msg):
    while True:
        r = requests.get('http://localhost:8000/', params={'message': msg})
        print(str(r.status_code) + " " + msg)


def main():
    r = redis.Redis(host='localhost', port=6379)
    executor = ThreadPoolExecutor(max_workers=50)
    i = 0
    while True:
        ms = r.zpopmax('queue', 1)
        msg = ms[0][0].decode('utf-8')
        i = i+1
        msg = msg + " worker " + str(i)
        executor.submit(worker, msg)


if __name__ == "__main__":
    main()
