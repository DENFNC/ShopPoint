FROM python:3.12.9-alpine3.21

WORKDIR /home/
COPY . .

RUN apk add --no-cache file
RUN pip install uv
RUN uv sync

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "main:app"]