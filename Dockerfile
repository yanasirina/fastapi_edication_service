ARG BASE_IMAGE=python:3.9-slim-buster
FROM $BASE_IMAGE

# system update & package install
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    openssl \
    libssl-dev \
    libpq-dev \
    postgresql-client \
    python-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .
WORKDIR .

# pip
RUN python3 -m pip install --user --upgrade pip && \
    python3 -m pip install -r requirements.txt

# Execute
CMD ["python", "main.py"]
