FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim

WORKDIR /app

COPY uv.lock pyproject.toml ./

RUN uv sync --frozen --no-install-project

COPY src/ ./src/
COPY tests/ ./tests/
COPY README.md ./

RUN uv sync --frozen

EXPOSE 8000

CMD ["uv","run","--no-sync","uvicorn","labops.server:app","--host","0.0.0.0","--port","8000"]