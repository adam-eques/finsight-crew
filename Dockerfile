FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml requirements.txt ./
COPY src ./src
COPY config ./config
RUN pip install --no-cache-dir -e .

ENTRYPOINT ["finsight"]
CMD ["--help"]
