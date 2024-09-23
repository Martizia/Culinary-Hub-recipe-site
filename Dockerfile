# Use an official Python runtime as the base image
FROM python:3.12


# Set the working directory in the container
WORKDIR /app

# Install the project dependencies
RUN pip install poetry

# Copy the project code into the container
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .


# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]