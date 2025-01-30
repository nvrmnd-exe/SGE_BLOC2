# BLOC 2
Yoon López Luis - DAM 1B

## ACTIVITAT 5 - PYTHON + POSTGRESQL

### PREPARACIÓ DE L'ENTORN

El primer que fem és crear l'estrictura d'arxius corresponent.

En aquest cas, tindrem els directoris següents:
`bloc2_Yoon` > `postgresql_python`

Dins de `postgresql_python`, desarem els arxius següents:
- `connect.py`
- `create_registre.py`
- `delete_registre.py`
- `main.py`
- `read_registre.py`
- `update_registre.py`

![img001](img/001.jpg)

A continuació, indiquem al `connect.py` les dades de la connexió a la base de dades.

![img002](img/002.Connect.py.jpg)

I comprovem que funciona, executant el programa amb un print al final de la connexió `print(connection_db)`

![img003](img/003.ResultConnect.jpg))

Aquest arxiu que hem creat ens servirà per establir la connexió amb la base de dades.

A continuació, hem de configurar el docker, creant un arxiu anomenat `docker-compose.yml` amb el següent contingut:

![img004](img/004.Docker.jpg)!(img/004)

Amb aquesta configuració, hem creat els serveis de la base de dades i el pgadmin per poder utilitzar més tard.

### CREACIÓ DOCKER

Un cop fet, hem d'activar el docker. És molt important tenir en compte que, un cop activat, no podem modificar-lo.

```commandline
sudo docker compose up -d
```
Que ha de donar el següent resultat en cas de ser correcte:
```commandline
[+] Running 2/2
 ✔ Container pg_erp  Running
 ✔ Container db_erp  Started   
```

**En cas d'error**, si l'error menciona que no ha pogut utilitzar el port, hem d'eliminar el procés que està executant el port.

Primer averigüem quin procés està executant el port:
```commandline
sudo lsof -i:5432
```
Eliminem el procés que està utilitzant el port; en aquest cas, era el procés amb PID 1935.
```commandline
sudo kill 1935
```
Un cop eliminat, podem tornar a executar el `docker compose up`.

Quan ja s'ha executat correctament, podem **veure els contenidors** actius; si afegim l'opció -a, apareixen també els inactius.
```commandline
sudo docker ps
```
![img005](img/005.dockerps.jpg)

**Parar un contenidor**
```commandline
sudo docker stop <nom contenidor>
```

**Eliminar un contenidor**
```commandline
sudo docker rm <nom contenidor>
```

Per **comprovar que funciona correctament**, entrem a pgadmin posant `localhost` al navegador, i s'hauria de mostrar la pàgina de pgadmin.

![img006](img/006.%20pgadmin.jpg)

Led credencials per accedir son les indicades a les línies del pgadmin del document `docker-compose.yml`.