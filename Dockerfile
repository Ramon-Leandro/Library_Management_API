# 1. Start with a tiny version of Python
FROM python:3.11-slim

# 2. Set the "home" folder inside the container
WORKDIR /code

# 3. Copy the requirements file first (for faster building)
COPY requirements.txt .

# 4. Install the libraries inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your 'app' folder into the container
COPY ./app ./app

# 6. The command to start the API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]