FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml poetry.lock* README.md ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi \
    && pip install torch --index-url https://download.pytorch.org/whl/cpu

COPY ./src /app/src
COPY ./models /app/models
COPY ./data /app/data

ENV QT_QPA_PLATFORM=offscreen

ENTRYPOINT ["python", "-m", "src.cli"]
CMD ["--help"]