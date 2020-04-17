import os
from dotenv import dotenv_values
from sshtunnel import SSHTunnelForwarder, create_logger

import psycopg2


def connectDB(dotenv_dict):
    import psycopg2 as pg

    # connect to db
    try:
        with SSHTunnelForwarder(
            (dotenv_dict["HOST"], 22),
            ssh_username=dotenv_dict["SSH_USER_NAME"],
            ssh_password=dotenv_dict["SSH_PASSWORD"],
            remote_bind_address=(dotenv_dict["DB_HOST"], 5432),
            logger=create_logger(loglevel=1),
        ) as server:
            server.start()
            conn = pg.connect(
                dbname=dotenv_dict["DB_NAME"],
                user=dotenv_dict["DB_USER_NAME"],
                host=dotenv_dict["DB_HOST"],
                password=dotenv_dict["DB_PASSWORD"],
                port=server.local_bind_port,
            )
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
