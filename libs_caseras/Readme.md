# Para hacer una libreria en Python... 

Se utiliza **from** indicando la carpeta y el archivo, seguido de **import** donde decimos que vamos a importar de la libreria

#### Ejemplo 


##### procesos/Menu.py
```
	class Menu():
	def __init__(self):
		print('Existo')
		pass 

```

##### ./main.py
```
from procesos.Menu import *

y = Menu()

```