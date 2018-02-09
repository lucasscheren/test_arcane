# test_arcane
API using Flask framework in Python


Le fichier server.py contient le code de l'api.
Le fichier arcane.db est la base donnée SQL avec laquelle l'api est en interaction.

La base de données contient les tables suivent l'architecture suivante :

```sql
CREATE TABLE users(
   id_user 		        INTEGER PRIMARY KEY     AUTOINCREMENT,
   first_name          CHAR(50)    NOT NULL,
   last_name           CHAR(50)    NOT NULL,
   birthday		        DATE
);
```

```sql
CREATE TABLE properties(
   id_property 		 INTEGER PRIMARY KEY     AUTOINCREMENT,
   name          	    CHAR(50)    NOT NULL,
   description        TEXT    NOT NULL,
   property_type	    CHAR(20),
   city			       CHAR(20),
   room			       INT,
   room_desc		    TEXT,
   owner              INT, 
   FOREIGN KEY(owner) REFERENCES users(id_user)  
);
```

On peut ajouter un user avec une requête POST http://127.0.0.1:5002/user 
et un json qui prend la forme de l'exemple suivant :
```json
{ 
 "first_name":"Lucas", 
 "last_name":"Scheren", 
 "birthday":"1993-07-15" 
}
```
On peut modifier un user avec une requête PUT http://127.0.0.1:5002/user 
et un json qui prend la forme de l'exemple suivant :
```json
{ 
 "column":"first_name", 
 "value":"Pocpoc", 
 "id_user":1
}
```
On peut ajouter une propriété avec une requête POST http://127.0.0.1:5002/property 
et un json qui prend la forme de l'exemple suivant :
```json
{ 
 "name":"La mer", 
 "description":"Pas loin de la mer", 
 "city":"Lacanau",
 "room":"9",
 "room_desc":"Une description",
 "owner":2
 "property_type":"Maison de plage"
}
```

On peut modifier une propriété avec une requête PUT http://127.0.0.1:5002/property
et un json qui prend la forme de l'exemple suivant :
```json
{ 
 "column":"name", 
 "value":"Pocpocs house", 
 "id_property":1
}
```
Enfin on peut consulter les propriétés d'une ville avec une requête GET http://127.0.0.1:5002/property/"Nomdelaville"
