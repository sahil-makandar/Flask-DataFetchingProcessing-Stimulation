# Flask Data Retrieval and Processing System

This Flask application simulates a simplified version of a data retrieval and processing system. It includes features such as data fetching, processing, storage, and error handling.

## Features

- **/fetch-data**: Simulates fetching data from an external service and processes the data.
- **/get-processed-data**: Retrieves all processed data stored in memory.
- **Error Handling**: Handles various errors, including missing keys and internal server errors.

## Setup Instructions

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/sahil-makandar/Flask-DataFetchingProcessing-Stimulation.git
    cd Flask-DataFetchingProcessing-Stimulation
    ```

2. **Set Up Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask Application:**
    ```bash
    python app.py
    ```

5. **Access the API:**

- **Fetch Data**: Open your browser or use a tool like Postman to make a GET request to `http://127.0.0.1:5000/fetch-data`.

- **Get Processed Data**: Make a GET request to `http://127.0.0.1:5000/get-processed-data`.
    
## Dependencies

- Flask
