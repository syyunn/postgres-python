import os
from dotenv import dotenv_values
from sshtunnel import SSHTunnelForwarder, create_logger

import psycopg2


def connectDB(dotenv_dict):
    import psycopg2 as pg
    # connect to db
    try:
        # this connection available after establish:
        #   ssh -L 65432:localhost:[postgres-port] lobby-dev@[mit-network-ip]
        conn = pg.connect(
            host="localhost",
            dbname=dotenv_dict["DB_NAME"],
            user=dotenv_dict["DB_USER_NAME"],
            password=dotenv_dict["DB_PASSWORD"],
            port='65432',
        )

        c = conn.cursor()
        c.execute("select * from lobby_refactored.information_schema.tables")
        rows = c.fetchall()
        for r in rows:
            print(r)

    except ConnectionError:
        print("failed")

    return conn


# DB_HOST=localhost
# DB_HOST_PORT=5432
# DB_NAME=lobby_refactored
# DB_USER=lobby-dev
# DB_PASS=acnLYEh-S&AnBm2J

if __name__ == "__main__":
    env_vars = dotenv_values()
    connectDB(env_vars)
    pass
