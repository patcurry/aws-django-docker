#!/bin/bash
# wait-for-postgres.sh
echo "wait for postgres to accept connections"
set -e

host="$1"
shift
cmd="$@"

postgres

until psql -h "$host" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
