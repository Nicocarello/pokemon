API REST Pokemon

-Este repositorio contiene un archivo .py que permite traer unos datos de la API de Pokemon (https://pokeapi.co/)
-Para ejecutar este programa necesita: 
-Descargar el archivo 'pokemon.py'
-Abrirlo en su editor de texto/IDE y ejecutar el código
-Luego entrar a su localhost.


-Lleva 2 metodos GET:

search_pokemon():
  Args:
  -q: Nombre del pokemon.
  -limit: Límite de cantidad de pokemones.
  -offset: Inicio de la lista de pokemones.
  
  Returns:
    -Devuelve una lista de pokemones por búsqueda de nombre.

get_pokemon():
  Args:
    -Nombre del pokemon.
  Returns:
    -Devuelve los atributos del pokemón requerido.
