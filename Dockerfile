FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set working directory
WORKDIR /code

COPY . /code

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt


# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]