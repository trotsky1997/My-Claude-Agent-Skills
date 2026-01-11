# Using UV in Docker

## Table of Contents
- Base Images
- Basic Dockerfile
- Multi-stage Builds
- Caching Strategies
- Production Optimizations
- Common Patterns

## Base Images

### Official UV Images

**Distroless (minimal):**
```dockerfile
FROM ghcr.io/astral-sh/uv:debian-distroless
```

**Debian-based (full OS):**
```dockerfile
FROM ghcr.io/astral-sh/uv:debian
```

**Alpine-based:**
```dockerfile
FROM ghcr.io/astral-sh/uv:alpine
```

### Using in Custom Images
```dockerfile
# Copy uv binary from distroless image
FROM ghcr.io/astral-sh/uv:debian-distroless AS uv
FROM python:3.12-slim
COPY --from=uv /uv /usr/local/bin/uv
```

## Basic Dockerfile

### Simple Python Application
```dockerfile
FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy application code
COPY . .

# Run application
CMD ["uv", "run", "main.py"]
```

### With Requirements File
```dockerfile
FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

# Copy requirements
COPY requirements.txt ./

# Install dependencies
RUN uv pip install --system -r requirements.txt

# Copy application
COPY . .

CMD ["python", "main.py"]
```

## Multi-stage Builds

### Optimized Production Build
```dockerfile
# Build stage
FROM ghcr.io/astral-sh/uv:debian AS builder

WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy source code
COPY . .

# Build application (if needed)
RUN uv build

# Runtime stage
FROM python:3.12-slim

WORKDIR /app

# Copy uv from builder
COPY --from=builder /usr/local/bin/uv /usr/local/bin/uv

# Copy installed packages
COPY --from=builder /app/.venv /app/.venv

# Copy application
COPY --from=builder /app/dist /app/dist

# Use virtual environment
ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "-m", "my_app"]
```

## Caching Strategies

### Layer Caching
```dockerfile
FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

# Copy only dependency files first (for better caching)
COPY pyproject.toml uv.lock ./

# Install dependencies (this layer is cached if deps don't change)
RUN uv sync --frozen

# Copy application code last (changes most frequently)
COPY . .

CMD ["uv", "run", "main.py"]
```

### BuildKit Cache Mount
```dockerfile
# syntax=docker/dockerfile:1.4
FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

COPY pyproject.toml uv.lock ./

# Mount cache for uv's global cache
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

COPY . .

CMD ["uv", "run", "main.py"]
```

## Production Optimizations

### Minimal Image Size
```dockerfile
# Use distroless base
FROM ghcr.io/astral-sh/uv:debian-distroless AS uv

# Use slim Python image
FROM python:3.12-slim

# Copy only uv binary
COPY --from=uv /uv /usr/local/bin/uv

WORKDIR /app

# Copy only necessary files
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY src/ ./src/

# Use system Python (no venv overhead)
ENV UV_SYSTEM_PYTHON=1

CMD ["uv", "run", "main.py"]
```

### Security Hardening
```dockerfile
FROM ghcr.io/astral-sh/uv:debian

# Create non-root user
RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

COPY . .

# Switch to non-root user
USER appuser

CMD ["uv", "run", "main.py"]
```

## Common Patterns

### Development Dockerfile
```dockerfile
FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

# Install dependencies including dev
COPY pyproject.toml uv.lock ./
RUN uv sync

# Copy code
COPY . .

# Expose port
EXPOSE 8000

# Run with hot-reload
CMD ["uv", "run", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
```

### Testing in Docker
```dockerfile
FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --all-groups

COPY . .

# Run tests
RUN uv run pytest

# Or as separate stage
FROM ghcr.io/astral-sh/uv:debian AS test
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --all-groups
COPY . .
RUN uv run pytest
```

### Docker Compose Example
```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
      - uv-cache:/root/.cache/uv
    environment:
      - UV_INDEX_URL=https://pypi.org/simple/
    ports:
      - "8000:8000"

volumes:
  uv-cache:
```

## Environment Variables

### Configuring UV in Docker
```dockerfile
ENV UV_INDEX_URL="https://pypi.org/simple/"
ENV UV_EXTRA_INDEX_URL="https://custom-index.com/"
ENV UV_CACHE_DIR="/cache/uv"
ENV UV_OFFLINE=0
```

### Using .env Files
```dockerfile
# Copy .env file
COPY .env .env

# Load in runtime
ENV $(cat .env | xargs)
```

## Troubleshooting

### Common Issues

**Issue**: Slow builds
- **Solution**: Use BuildKit cache mounts, layer dependencies separately

**Issue**: Large image size
- **Solution**: Use multi-stage builds, distroless images, remove dev dependencies

**Issue**: Permission errors
- **Solution**: Create non-root user, set proper file permissions

**Issue**: Cache not working
- **Solution**: Use BuildKit, mount cache volumes, check cache directory permissions

## Best Practices

1. **Separate dependency installation**: Copy dependency files before source code
2. **Use frozen lockfiles**: Always use `--frozen` flag in production
3. **Multi-stage builds**: Reduce final image size
4. **Cache optimization**: Use BuildKit cache mounts for faster rebuilds
5. **Security**: Run as non-root user, scan images for vulnerabilities
6. **Minimal base images**: Use distroless or slim images when possible
