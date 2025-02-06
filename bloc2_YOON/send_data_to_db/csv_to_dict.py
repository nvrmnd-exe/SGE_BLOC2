import dict_to_db as d_t_db
import pandas as pd

def csv_to_dict():
    print(data)
    conn = psycopg2.connect(
        database="the_bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()
    sql = "INSERT INTO Clientes (nombre_cliente, dirección_cliente, teléfono_cliente, correo_electrónico_cliente, fecha_cumpleaños) VALUES (%s, %s, %s, %s, %s);"
    values = (data["Nombre_cliente"][pos], data["Dirección_Cliente"][pos], data["Teléfono_Cliente"][pos], data["Correo_Electrónico_Cliente"][pos], data["Fecha_Cumpleaños"][pos])

    cur.execute(sql,values)
    conn.commit()

    cur.close()
    conn.commit()

    return {"M"}