FROM python:3.8-alpine

ARG BUILD_VERSION="1.0.0-snapshot"
ARG PROJECT_NAME=

ENV APP_VERSION=${BUILD_VERSION}

LABEL VERSION="${BUILD_VERSION}"

COPY ./ /app/
RUN \
	apk update && \
	apk add --update git curl build-base tcl tk && \
	mkdir -p /app && \
	pip install --upgrade pip && \
	apk del git build-base && \
	rm -rf /app/setup && \
	rm -rf /var/cache/apk/*

WORKDIR /app

CMD ["python", "-u", "/app/main.py"]
