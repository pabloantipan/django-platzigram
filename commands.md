# Some useful command as I work on this

python manage.py runserver

python manage.py makemigrations
python manage.py migrate

python manage.py shell


# Insert data 
from datetime import date

users = [
    {
        'email': 'cvander@platzi.com',
        'first_name': 'Christian',
        'last_name': 'Van der Henst',
        'password': '1234567',
        'is_admin': True
    },
    {
        'email': 'freddier@platzi.com',
        'first_name': 'Freddy',
        'last_name': 'Vega',
        'password': '987654321'
    },
    {
        'email': 'yesica@platzi.com',
        'first_name': 'Yésica',
        'last_name': 'Cortés',
        'password': 'qwerty',
        'birthdate': date(1990, 12,19)
    },
    {
        'email': 'arturo@platzi.com',
        'first_name': 'Arturo',
        'last_name': 'Martínez',
        'password': 'msicomputer',
        'is_admin': True,
        'birthdate': date(1981, 11, 6),
        'bio': "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
    }
]

from posts.models import User

for user in users:
    obj = User(**user)
    obj.save()
    print(obj.pk, ':', obj.email)

# Get Data
from posts.models import User
user = User.objects.get(email='freddier@platzi.com')
user
type(user)

platzi_users = User.objects.filter(email__endswith='@platzi.com')
platzi_users

for u in platzi_users:
    print(u.email, ':', u.is_admin)

platzi_users_updated = User.objects.filter(email__endswith='@platzi.com').update(is_admin=True)
platzi_users_updated

platzi_users = User.objects.filter(email__endswith='@platzi.com')
for u in platzi_users:
    print(u.email, ':', u.is_admin)


users = User.objects.all()
users


# Glosary
    ORM: Object-relational mapping. Es el encargado de permitir
    el acceso y control de una base de datos relacional a través de
    una abstracción a clases y objetos.

    Templates: Archivos HTML que permiten la inclusión y ejecución
    de lógica especial para la presentación de datos.

    Modelo: Parte de un proyecto de Django que se encarga de estructurar
    las tablas y propiedades de la base de datos a través de clases de Python.x

    Vista: Parte de un proyecto de Django que se encarga de la
    lógica de negocio y es la conexión entre el template y el modelo.

    App: Conjunto de código que se encarga de resolver una parte
    muy específica del proyecto, contiene sus modelos, vistas, urls, etc.

    Patrón de diseño: Solución común a un problema particular.

# Session 14
Building user with auth

from django.contrib.auth.models import User
u = User.objects.create_user(username='yesika', password='admin123')

# Superuser
python manage.py createsuperuser

# About app design
Separar las aplicaciones es cuestion de experiencia, pero unos tips que te puedo dar son:

    Trata de no tener aplicaciones con mas de 6 modelos, si tienes mas significa que tienes una app muy grande, que hace demasiadas cosas y tiene demasiadas responsabilidades.

    Trata de pensar en como separar las aplicaciones de tal modo que sean reutilizables, incluso piensa si la puedes reusar para otros proyectos.

    Puedes guiarte de otros proyectos, pero cada proyecto esta hecho para resolver un problema especifico, puede que no se ajuste a lo que tu quieres construir.

    Es mejor tener muchas apps pequeñas que tener una app mounstrosamente grande.

Divide apps is a matter of experience. Some tips are:
    Try apps with no more than 6 models. More than that, could mean
    that your do too many things, it takes a lot of resposabilites,
    so It's big

    Think apps in a way you could reuse them latetly. Even, think
    about using them in other projects

    You can take other projects as a model. Think again about each 
    app solves an specific problem. Take a too distributed model, 
    could implies more code and not necesary solve THE problem

    A lot of little apps is much better than a giant one



