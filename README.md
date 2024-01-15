# Frida CodeShare Search


![image](https://github.com/phrantom/fridasearch/assets/52974841/c8094f13-9939-4602-8517-1aec2058404f)


Este script de Python proporciona una interfaz de línea de comandos para buscar y explorar códigos compartidos en Frida CodeShare. Puedes buscar códigos por palabra clave, ver detalles como el nombre, cantidad de "me gusta" y descripción, y obtener enlaces para ejecutar el código con Frida.

## Instalacion

```bash
git clone https://github.com/phrantom/fridasearch.git
cd fridasearch
pip3 install -r requirements.txt
```


## Uso

```bash
python3 fridaSearch.py
```

![image](https://github.com/phrantom/fridasearch/assets/52974841/e115e0d8-08af-4114-81aa-aa6d11eb1b9b)



### Busqueda por palabra clave

```bash
python3 fridaSearch.py -s root
```

![image](https://github.com/phrantom/fridasearch/assets/52974841/9eb2f275-9979-4410-8893-b84eb16b8a64)



### Todos los codeshares disponibles

```bash
python3 fridaSearch.py -a 
```
![image](https://github.com/phrantom/fridasearch/assets/52974841/fe9cdd41-7b1d-4383-915b-67a46f377f46)




### Guardar resultados en un archivo json
```bash
# Guardar los que contengan una palabra clave
python3 fridaSearch.py -s root -o root_codeshares.json
```

```bash
# Guardar todos
python3 fridaSearch.py -a -o all_codeshares.json
```




### Ver los datos json con jq

Todos los datos del json 
```bash
jq '.[]' root_codeshares.json
```

![image](https://github.com/phrantom/fridasearch/assets/52974841/62d05788-4921-42b0-8d0f-3632a3e3a5c9)



Solo el primer dato
```bash
jq '.[0]' all_codeshares.json
```

![image](https://github.com/phrantom/fridasearch/assets/52974841/c7602886-5d0d-4724-8434-b3aa4c774f66)



Los primeros 3 datos 
```bash
jq '.[:3]' all_codeshares.json
```

![image](https://github.com/phrantom/fridasearch/assets/52974841/479de1d6-900d-4530-ab25-4be1945573a2)


