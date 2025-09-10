#!/bin/sh
set -e

echo "Waiting for MYSQL..."
while ! nc -z db-mysql 3306; do
    sleep 1
done
echo "MySQL started - executing command"
echo "Running migrations..."
flask db upgrade
echo "Migrations complete."
exec "$@"