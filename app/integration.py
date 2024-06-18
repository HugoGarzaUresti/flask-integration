import requests
import schedule
import time
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)

def fetch_data():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/data')
def get_data():
    data = fetch_data()
    if data:
        return jsonify(data)
    else:
        return "Failed to fetch data", 500

def scheduled_task():
    print("Running scheduled task")

def run_scheduler():
    schedule.every(10).seconds.do(scheduled_task)
    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    # Start the scheduler in a separate thread
    scheduler_thread = Thread(target=run_scheduler)
    scheduler_thread.start()
    # Run the Flask app
    app.run(debug=True)

if __name__ == "__main__":
    main()
