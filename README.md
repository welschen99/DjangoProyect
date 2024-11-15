INSTALL ```bash django package```

CREATE
```bash
django-admin startproject mysite djangotutorial . #(EL PUNTO ES PARA QUE LO CREE DENTRO DE LA CARPETA EN LA QUE ESTAMOS)
```

START
```bash
py manage.py runserver 3000 #(PARA QUE CORRA EN EL PUERTO 3000)
```

CREATE MODULE IN DJANGO
```bash
py manage.py startapp blog
```

CREATE MIGRATE - bse usa al modificar la estructura del modelo(agregar/eliminar campos, modelos)
```bash
py manage.py makemigrations
```

EJECUTE MIGRATE - despues de ejecutar el makemigrations
```bash
py manage.py makemigrations
```


PARA CORRERLO EN PYCHARM SIN PONER COMANDOS
```bash
En PyCharm Community Edition, puedes configurar una Run Configuration para ejecutar tu proyecto Django. Sigue estos pasos:
Abre PyCharm y ve a Run > Edit Configurations... en el menú superior.
En la ventana de configuraciones, haz clic en el símbolo de + y selecciona Python para agregar una nueva configuración.
Completa los siguientes campos:
Name: Ponle un nombre a tu configuración, como Django Server.
Script path: Indica la ruta hacia manage.py en tu proyecto, por ejemplo: /ruta/al/proyecto/manage.py.
Parameters: Escribe runserver para que PyCharm ejecute el comando py manage.py runserver.
```

GITHUB COMMANDS
```bash
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/welschen99/DjangoProyect.git
git push -u origin main
```

CREAR EL REQUIREMENTS.TXT
```bash 
pip freeze > requirements.txt 
```


DJANGO SHELL
```bash 
python manage.py shell
>> exit()
```

CREATE SUPERUSER FOR ADMIN
```bash 
python manage.py createsuperuser
```



## Django Documents
 - [User Model](https://docs.djangoproject.com/en/2.2/ref/contrib/auth/)