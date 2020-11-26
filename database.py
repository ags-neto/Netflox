import psycopg2
conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")

CREATE_USER = "INSERT INTO users (adminid, clientid, name, email, password, balance) VALUES (?, ?, ?, ?, ?, ?);"

adminid = 0
clientid = 0

def create_user(conn, adminid, clientid, name, email, password):
    with conn:
        conn.execute(CREATE_USER, (adminid, clientid, name, email, password, 20))


conn.close()
