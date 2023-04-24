import requests
import concurrent.futures
import argparse
import json
import time
from datetime import datetime

parser = argparse.ArgumentParser(description='Send parallel HTTP requests.')
parser.add_argument('url', type=str, help='URL to send requests to')
parser.add_argument('--workers', type=int, default=4, help='Number of workers (default: 4)')
parser.add_argument('--requests', type=int, default=20, help='Number of requests (default: 20)')
parser.add_argument('--delay', type=float, default=0, help='Delay between requests in seconds (default: 0)')
args = parser.parse_args()

url = args.url
num_workers = args.workers
num_requests = args.requests
delay = args.delay

def send_request(url):
    time.sleep(delay)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    response = requests.get(url)
    if response.status_code == 200:
        print(f"[{timestamp}] {response.content.decode('utf-8')}")
    else:
        print(f"[{timestamp}] Error: {response.status_code}")

with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
    futures = []
    for i in range(num_requests):
        futures.append(executor.submit(send_request, url))
        