# Dockerfile for Scientific Project Manager Documentation
# Uses MkDocs with Material theme for beautiful, searchable documentation

FROM python:3.11-slim

LABEL maintainer="Scientific Project Manager Team"
LABEL description="MkDocs documentation server for Scientific Project Manager"

# Set working directory
WORKDIR /docs

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy documentation source
COPY mkdocs.yml /docs/
COPY docs/ /docs/docs/

# Expose MkDocs development server port
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV MKDOCS_LIVE_RELOAD=true

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://localhost:8000 || exit 1

# Default command: serve documentation with live reload
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
