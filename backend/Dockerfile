# https://racum.blog/articles/minimal-docker-geodjango-postgis/
FROM ghcr.io/osgeo/gdal:alpine-small-latest

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

RUN apk add --no-cache python3 py3-pip postgresql-client geos

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Run server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
