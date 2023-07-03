import psycopg2
from psycopg2 import Error
from dotenv import dotenv_values

def dbsave(df):

    env_vars = dotenv_values()
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(
            user=env_vars.get('PG_DB_USERNAME'),
            password=env_vars.get('PG_DB_PASSWORD'),
            host=env_vars.get('PG_DB_SERVER'),
            port=env_vars.get('PG_DB_PORT'),
            database=env_vars.get('PG_DB_DATABASE')
        )
        cursor = connection.cursor()

        values = df.values.tolist()
        table_name = env_vars.get('PG_DB_TABLE')
        columns = ', '.join(df.columns)

        for value in values:
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({', '.join(['%s']*len(value))})"
            cursor.execute(sql, value)

        connection.commit()
        print("Data appended successfully")
    except (Exception, Error) as error:
        if connection is not None:
            connection.rollback()
        print("Error while appending data to the table:", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()

