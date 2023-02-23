FROM alpine:latest

RUN apk add --no-cache python3
COPY src/ /app

EXPOSE 8080
WORKDIR /app
CMD ["python3", "/app/jagacha.py"]