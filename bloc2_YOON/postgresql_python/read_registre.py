import connect

def read_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_red = "SELECT * FROM Clientes"

    cursor.execute(sql_red)
    conn.commit()

    results = cursor.fetchall()
    print(results)
    print(results[4])
    return results

read_reg()