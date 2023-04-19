import requests
import concurrent.futures
import argparse
import json

parser = argparse.ArgumentParser(description='Send parallel HTTP requests.')
parser.add_argument('url', type=str, help='URL to send requests to')
parser.add_argument('--workers', type=int, default=4, help='Number of workers (default: 4)')
parser.add_argument('--requests', type=int, default=20, help='Number of requests (default: 20)')
args = parser.parse_args()

url = args.url
num_workers = args.workers
num_requests = args.requests

def send_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.content.decode('utf-8'))
    else:
        print(f"Error: {response.status_code}")

with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
    futures = []
    for i in range(num_requests):
        futures.append(executor.submit(send_request, url))



