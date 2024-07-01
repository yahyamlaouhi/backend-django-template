FROM python:3.10-alpine
LABEL maintainer="django template"

# Environment settings
ENV PYTHONUNBUFFERED 1
ENV PATH="/scripts:${PATH}"
ENV PYTHONPATH=/app

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

# Install Poetry
RUN apk add curl
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy dependency files
COPY ./pyproject.toml ./poetry.lock* /app/

# Install Python dependencies
ARG INSTALL_DEV=false

RUN sh -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main ; fi"

# Clean up build dependencies
RUN apk del .tmp-build-deps

# Copy application code
COPY . /app

# Set up directories and permissions
RUN mkdir -p /vol/web/media /vol/web/static && \
    adduser -D user && \
    chown -R user:user /vol/ && \
    chmod -R 755 /vol/web


# Switch to non-root user
USER user


# Define volume
VOLUME /vol/web

