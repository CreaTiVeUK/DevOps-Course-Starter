# -----Perform common operations-----
FROM python:3.7-slim-bullseye as base

ENV POETRY_VERSION=1.1.13

# System deps:
RUN pip install "poetry==$POETRY_VERSION"


# Copy across your application code
WORKDIR /appcode
COPY poetry.lock pyproject.toml ./

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY todo_app ./todo_app
COPY entrypoint.sh ./

# -----Configure for local test-----
FROM base as test
ENV FLASK_ENV development
ENV FLASK_DEBUG 1
# Define an entrypoint, and default launch command
ENTRYPOINT poetry run pytest; poetry run watchmedo shell-command \ 
    --patterns="*.py;*.html" \
    --recursive \
    --command='poetry run pytest' \
    .

# -----Configure for local test-----
FROM test as ci-test
# Define an entrypoint, and default launch command
ENTRYPOINT poetry run pytest

# -----Configure for local development-----
FROM base as development
ENV FLASK_ENV development
ENV FLASK_DEBUG 1
# Define an entrypoint, and default launch command
ENTRYPOINT poetry run flask run -h 0.0.0.0 -p 5000
EXPOSE 5000

# -----Configure for production-----
FROM base as production
ENV FLASK_ENV production
# Define an entrypoint, and default launch command
RUN chmod +x ./entrypoint.sh
ENV PORT=8000
ENTRYPOINT ["./entrypoint.sh"]
EXPOSE 8000
