import psycopg2


def create_user(name, email, password):
    conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
    c = conn.cursor()

    c.execute("INSERT INTO users (nome, email, password, balance) VALUES ('"+name+"','"+email+"','"+password+"',20)")

    conn.commit()
    conn.close()


def log_in(email, password):
    conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE email = '"+email+"' AND password = '"+password+"'")
    results = c.fetchall()

    conn.commit()
    conn.close()

    if results:
        for i in results:
            print("Welcome" + i[1])
        return 1
    else:
        print("Email and password not recognised")
        return 0


def delete_user(userid):
    conn = psycopg2.connect("host=localhost dbname=Netflox user=postgres password=postgres")
    c = conn.cursor()

    c.execute("DELETE FROM users WHERE userid = (" + userid + ")")

    conn.commit()
    conn.close()
