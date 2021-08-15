# This python file serves as a template for connecting to a Redshift cluster via Python

import psycopg2

try:
    conn = psycopg2.connect("dbname=dev host=sample-redshift-endpoint.amazonaws.com port=5439 user=awsuser password=...")
    cur = conn.cursor()
    print("Connected to Redshift")
except psycopg2.Error as e:
    print("ERROR:", e)

print("End of program")
# conn.close()