# Integration

This guide demonstrates how to integrate multiple functionalities in Python using Flask, `requests`, and `schedule` libraries. We will create a web service that fetches data from an external API and schedule a periodic task.

## Requirements

- Python 3.x
- `Flask` library
- `requests` library
- `schedule` library

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the application:
    ```sh
    python run.py
    ```

3. Access the application:
    - Fetch data: `http://127.0.0.1:5000/data`
    - The scheduled task runs every 10 seconds and prints a message to the console.

## Code Explanation

### `app/integration.py`

This module contains the Flask application, scheduled task, and data fetching logic.

- **`fetch_data`**: Fetches data from an external API.
- **`get_data`**: A Flask route that returns the fetched data.
- **`scheduled_task`**: A function that runs periodically.
- **`run_scheduler`**: Runs the scheduler in a separate thread.
- **`main`**: Starts the scheduler and runs the Flask app.

### `run.py`

This script serves as the entry point for the application. It calls the `main` function to start the scheduler and Flask server.

## Additional Information

- The `schedule` library is used to run periodic tasks.
- The `requests` library is used to fetch data from an external API.
- The `Flask` library is used to create a web service.
