FROM ghcr.io/astral-sh/uv:python3.12-alpine

WORKDIR /api

COPY ./pyproject.toml ./uv.lock ./README.md ./

RUN uv sync

COPY ./ ./

ENTRYPOINT [ "uv", "run", "uvicorn", "--app-dir", "./src", "--host", "0.0.0.0", "--port", "3000"]
CMD [ "main:app" ]