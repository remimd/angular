ARG PYTHON_VERSION="3.11.5"

# Python
FROM python:${PYTHON_VERSION}-slim

ARG WORK_DIR="/app"

# Working directory
WORKDIR ${WORK_DIR}
COPY . .

# Setup system
RUN apt-get upgrade -y
RUN apt-get update

RUN apt-get install build-essential -y

RUN apt-get autoremove
RUN apt-get clean

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE ${UVICORN_PORT}

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir poetry

# Setup Poetry
RUN poetry config installer.modern-installation true
RUN poetry config virtualenvs.create false
RUN poetry install --compile --no-cache --without dev
RUN poetry cache clear pypi --all

ENTRYPOINT ["uvicorn", "app:app"]
CMD ["--use-colors"]
