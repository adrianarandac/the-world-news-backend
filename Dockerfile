# Use the official Python 3.11.2 image as a parent image
FROM python:3.11.2

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install the dependencies
RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Expose the port the app runs on
EXPOSE 8000

# Define environment variable
ENV MODULE_NAME="the_world_news_backend.main"
ENV VARIABLE_NAME="app"
ENV PORT=8000

# Run the application
CMD ["poetry", "run", "start"]