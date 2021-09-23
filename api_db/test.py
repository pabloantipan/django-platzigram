import psycopg2

try:
    connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="123pablo",
        host="127.0.0.1",
        port="5433",
    )

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

# import subprocess

# connection = psycopg2.connect(
#     dbname="postgres",
#     user="postgres",
#     password="123pablo",
#     host="127.0.0.1",
#     port="5433",
# )

# print(connection.closed)  # 0

# # restart the db externally
# # subprocess.check_call("sudo /etc/init.d/postgresql restart", shell=True)

# # this query will fail because the db is no longer connected
# try:
#     cur = connection.cursor()
#     cur.execute("SELECT 1")
# except psycopg2.OperationalError:
#     pass

# print(connection.closed)  # 2
