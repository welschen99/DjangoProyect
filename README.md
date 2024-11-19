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
py manage.py startapp tasks
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


Estructura Base de un Proyecto Django
```bash 
my_project/               # Carpeta raíz del proyecto
│
├── manage.py             # Script para ejecutar comandos Django
├── requirements.txt      # Dependencias del proyecto (si no usas Pipfile)
├── .env                  # Variables de entorno (configuración sensible)
├── static/               # Archivos estáticos globales (CSS, JS, imágenes icons)
├── templates/            # Plantillas HTML globales como base.html donde van los menus y eso
│
├── my_project/           # Configuración principal del proyecto
│   ├── __init__.py       
│   ├── asgi.py           # Configuración de ASGI
│   ├── settings.py       # Configuración principal
│   ├── urls.py           # Enrutamiento principal
│   ├── wsgi.py           # Configuración de WSGI
│   └── middleware/       # Middleware personalizado (opcional)
│
└── apps/                 # Aplicaciones modulares
    │
    ├── inventory/        # Ejemplo de módulo: Inventarios
    │   ├── migrations/   # Migraciones de base de datos
    │   ├── templates/    # Plantillas específicas de esta app
    │   ├── static/       # Archivos estáticos específicos de esta app
    │   ├── tests/        # Pruebas unitarias
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py     # Define modelos relacionados con esta app.
    │   ├── views.py      # Lógica de vistas.
    │   └── urls.py       # Enrutamiento específico de esta app.
```

## Django Documents
 - [Django Tutorial](https://cosasdedevs.com/django/)
 - [Doc Tutorial](https://www.w3schools.com/django/django_intro.php)
 - [User Model](https://docs.djangoproject.com/en/2.2/ref/contrib/auth/)