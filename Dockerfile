FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

LABEL maintainer="shivam23rawat <shivamrawat2000@gmail.com>"

WORKDIR /app

COPY pyproject.toml .

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

COPY src/ /app/src

EXPOSE 8000

CMD ["fastapi", "run", "src/app.py", "--host", "0.0.0.0", "--port", "8000"]