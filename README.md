# Hallucination-Identification
It is an API that takes in a user query and AI response, then processes it to verify if this is a hallucination. It has set of documents that are the ground truth.

## Setup

1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Load your environment variables: `cp .env.example .env` (Linux/Mac) or `copy .env.example .env` (Windows)

## Usage

1. Fill in the required API keys in the code.
2. Add your txt file in '/Data' folder.
3. Run the FastAPI application: `uvicorn main:app --reload`
4. Visit `http://127.0.0.1:8000/docs` in your browser to interact with the API using Swagger documentation.
