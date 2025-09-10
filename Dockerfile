FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat-openbsd \
    libmariadb-dev-compat \
    gcc
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
COPY . .
EXPOSE 5000
ENTRYPOINT ["entrypoint.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]