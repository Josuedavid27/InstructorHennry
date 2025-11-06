# ¿Que es un entorno virtual en python?

*permite tener tu propio espacio donde instalas librerías sin afectar las del sistema.*

*Ejemplo: un proyecto puede usar Flask 2.0 y otro Django 4.2 sin problema.*

python --version **( Verificar la version de python instalada )**

python -m venv venv **( Para crear el entono virtual venv es el nombre del entorno que se va a crear pero se puede cambiar )**

* se crea una carpeta con todos los archivos necesarios


venv\Scripts\activate **( Para activar el entorno virtaul )**

pip install flask **( Para instalar dependencias )**

es opcional crear el archivo donde se guarden las dependencias

pip freeze > requirements.txt ( Para crear el archivo donde se guardaran las dependencias )

pip install -r requirements.txt ( Para actualizar en caso de haber nuevas dependencias )
