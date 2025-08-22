FROM python:3.13-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add --no-cache gcc musl-dev libpq-dev

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY ./ ./

RUN chmod +x /app/entrypoint.sh

CMD ["sh", "entrypoint.sh"]