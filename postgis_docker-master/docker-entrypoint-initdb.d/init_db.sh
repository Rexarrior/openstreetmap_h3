#!/bin/bash

set -e

# Perform all actions as $POSTGRES_USER
export PGUSER="$POSTGRES_USER"
echo "init OSM database"
"${psql[@]}" <<- 'EOSQL'
\i /input/static/database_init.sql
EOSQL

echo "parallel OSM data loading"
#https://github.com/docker-library/postgres/blob/master/docker-entrypoint.sh

# find /input/sql/ | grep "/.*sql$" | sort | PGHOST= PGHOSTADDR=  parallel psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --no-password --no-psqlrc  --dbname "osmworld" -f
# find /input/sql/ | grep "/.*sql$" | sort | PGHOST= PGHOSTADDR=  parallel (psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --no-password --no-psqlrc  --dbname "osmworld" -f {} \; && rm {})
input_dir="/input/sql/"
dbname="osmworld"
POSTGRES_USER="your_postgres_user_here"

for sql_file in "$input_dir"*.sql; do
    if [ -f "$sql_file" ]; then
        psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --no-password --no-psqlrc --dbname "$dbname" -f "$sql_file"
        python3 rm_connected_tsv.py $sql_file
    fi
done

echo "finish OSM database initialization"

"${psql[@]}" <<- 'EOSQL'
\i /input/static/database_after_init.sql
EOSQL

