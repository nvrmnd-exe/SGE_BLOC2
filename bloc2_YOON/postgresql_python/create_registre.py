import connect

def create_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()
    sql_create = "INSERT INTO Clientes (nombre_cliente, dirección_cliente, teléfono_cliente, correo_electrónico_cliente, fecha_cumpleaños) VALUES (%s, %s, %s, %s, %s);"

    values=('Yoon', 'carrer el que sigui', '657893093', 'yoon@correu.com', '21_10_2002')

    cursor.execute(sql_create, values)
    conn.commit()

    conn.close()
    cursor.close()