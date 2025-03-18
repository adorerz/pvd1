FROM python:3.10-slim

# Prevent Python from writing .pyc files and use unbuffered output.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies.
# The libraries below include essential build tools and packages needed for
# packages like WeasyPrint (requires Cairo, Pango, GDK-Pixbuf) and others.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    libcairo2 \
    libpango1.0-0 \
    libgdk-pixbuf2.0-0 \
    pkg-config \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the requirements file.
COPY requirements.txt .

# Upgrade pip and install Python dependencies.
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir gunicorn

# Copy the rest of your application code.
COPY . .

# If this is a Django app, collect static files.
RUN python manage.py collectstatic --noinput

# Expose port 8000.
EXPOSE 8000

# Run the application using Gunicorn.
CMD ["gunicorn", "pvd.wsgi:application", "--bind", "0.0.0.0:8000"]
