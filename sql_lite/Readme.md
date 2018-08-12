# Uso de base de datos SQLite3

## Antes que nada debemos crear la base de datos con sqlite3 

```
sqlite3 CREATE TABLE agenda (ident INTEGER PRIMARY KEY, nombre VARCHAR(30) UNIQUE, ecorreo VARCHAR(40), telefono INT(9));
```

## Debemos importar la libreria 

``` import sqlite3 ```

## Links de la fuente...

https://python-para-impacientes.blogspot.com/2014/02/bases-de-datos-sqlite3.html

http://www.pythondiario.com/2013/12/python-y-sqlite3-como-base-de-datos.html