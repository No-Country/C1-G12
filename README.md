# Cohorte1-Grupo12
## Medical Appointment React-Django-Graphql App

### Tecnologias Usadas:
#### Frontend
- React
- Bootstrap
- React Apollo Client
- Helmet
- Iconify
- React Router
- Formik
#### Backend
- Django
- GraphQl
- JWT Auth
- Postgres


## Instalar aplicación
<br>

### Front End: 
<br>
Para arrancarlo debes moverte a la carpeta "frontend" y ejecutar el siguiente comando:

```sh
$ npm start 
```
Esta aplicación fue creada con:

```sh
$ create-react-app
``` 
<br>

### Back End:
<br>

### Configuración del entorno virtual
Se configura el entorno virtual para aislar la aplicación, el uso de la herramienta `virtualenv` nos ayuda a manejar las versiones de las dependencias de forma eficiente:

```sh
$ python3.8 -m venv .ENV/medicalenv
$ source .ENV/medicalenv/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

### Configuración de la base de datos:
<br>

Debemos configurar nuestro motor de base de datos para realizar las conexiones.

Después de la instalación, debemos asignar permisos de superusuario para configurar nuestras credenciales para la base de datos:
```sh
$ sudo su - postgres
```
Ahora debería estar en una sesión de shell para el usuario de postgres. Se inicia sesión en Postgres escribiendo:
```sh
$ psql
```
Primero, crearemos una base de datos para nuestra aplicación en Django.
```sh 
$ CREATE DATABASE Medical_Store;
```

A continuación, crearemos un usuario de base de datos que usaremos para conectarnos e interactuar con la base de datos. Se debe establecer una contraseña larga y segura:
```sh
$ CREATE USER medicaluser WITH PASSWORD 'password';
```
Luego, modificaremos algunos de los parámetros de conexión para el usuario que acabamos de crear. Esto acelerará las operaciones de la base de datos para que no sea necesario consultar y configurar los valores correctos cada vez que se establece una conexión.

Estamos configurando la codificación predeterminada en UTF-8, que espera Django. También estamos configurando el esquema de aislamiento de transacciones predeterminado en "lectura confirmada", que bloquea las lecturas de las transacciones no confirmadas. Por último, estamos configurando la zona horaria. De forma predeterminada, nuestro proyectos de Django estarán configurados para usar UTC:
```sh
$ ALTER ROLE medicaluser SET client_encoding TO 'utf8';
$ ALTER ROLE medicaluser SET default_transaction_isolation TO 'read committed';
$ ALTER ROLE medicaluser SET timezone TO 'UTC';'UTC';
```

Ahora, para finalizar las preparaciones de nuestra base de datos tenemos que otorgar a nuestra derechos de acceso de usuario a la base de datos que creamos:
```sh
$ GRANT ALL PRIVILEGES ON DATABASE Medical_Store TO medicaluser;
```

Es importante configurar las variables de entorno para realizar una conexión segura con la base de datos.

Para finalizar e iniciar la instancia del servidor de Django debemos migrar las configuraciones de los modelos para la base de datos y correr

This is an example Django app that uses
[MemCachier](http://www.memcachier.com) to cache algebraic
computations. 

**This example is written with Django 1.8.16. Unless you specifically
need an old Django version you should check out a newer 
[example](https://github.com/memcachier/examples-django-tasklist).**

You can view a working version of this app
[here](http://memcachier-examples-django.herokuapp.com) that uses
[MemCachier on Heroku](https://addons.heroku.com/memcachier).
Running this app on your local machine in development will work as
well, although then you won't be using MemCachier -- you'll be using a
local dummy cache. MemCachier is currently only available with various
cloud providers.

Setting up MemCachier to work in Django is very easy. You need to
make changes to requirements.txt, settings.py, and any app code that
you want cached. These changes are covered in detail below.

## Deploy to Heroku

You can deploy this app yourself to Heroku to play with.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv-2.7 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. Alternatively you
can use foreman and gunicorn to run the server locally (after copying
`dev.env` to `.env`):

```sh
$ foreman start
```

## Deploy to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/memcachier/examples-django.git
$ cd examples-django
$ heroku create
$ heroku addons:add memcachier:dev
$ git push heroku master:master
$ heroku open
```

## requirements.txt

MemCachier has been tested with the pylibmc memcache client, but the
default client doesn't support SASL authentication. Run the following
commands to install the necessary pips:

```sh
$ sudo brew install libmemcached
$ pip install django-pylibmc pylibmc
```

Don't forget to update your requirements.txt file with these new pips.
requirements.txt should have the following two lines:

```
django-pylibmc==0.6.1
pylibmc==1.5.1
```

## Configuring MemCachier (settings.py)

To configure Django to use pylibmc with SASL authentication. You'll also need
to setup your environment, because pylibmc expects different environment
variables than MemCachier provides. Somewhere in your `settings.py` file you
should have the following lines:

```python
os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

CACHES = {
    'default': {
        # Use pylibmc
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',

        # Use binary memcache protocol (needed for authentication)
        'BINARY': True,

        # TIMEOUT is not the connection timeout! It's the default expiration
        # timeout that should be applied to keys! Setting it to `None`
        # disables expiration.
        'TIMEOUT': None,
        'OPTIONS': {
            # Enable faster IO
            'tcp_nodelay': True,

            # Keep connection alive
            'tcp_keepalive': True,

            # Timeout settings
            'connect_timeout': 2000, # ms
            'send_timeout': 750 * 1000, # us
            'receive_timeout': 750 * 1000, # us
            '_poll_timeout': 2000, # ms

            # Better failover
            'ketama': True,
            'remove_failed': 1,
            'retry_timeout': 2,
            'dead_timeout': 30,
        }
    }
}
```

## Persistent Connections

By default, Django doesn't use persistent connections with memcached. This is a
huge performance problem, especially when using SASL authentication as the
connection setup is even more expensive than normal.

You can fix this by putting the following code in your `wsgi.py` file:

```python
# Fix django closing connection to MemCachier after every request (#11331)
from django.core.cache.backends.memcached import BaseMemcachedCache
BaseMemcachedCache.close = lambda self, **kwargs: None
```

There is a bug file against Django for this issue
([#11331](https://code.djangoproject.com/ticket/11331)).

## Application Code

In your application, use django.core.cache methods to access
MemCachier. A description of the low-level caching API can be found
[here](https://docs.djangoproject.com/en/1.8/topics/cache/#the-low-level-cache-api).
All the built-in Django caching tools will work, too.

Take a look at
[memcachier_algebra/views.py](https://github.com/memcachier/examples-django/blob/master/memcachier_algebra/views.py)
in this repository for an example.

## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](http://github.com/memcachier/examples-django/issues).

Master [git repository](http://github.com/memcachier/examples-django):

* `git clone git://github.com/memcachier/examples-django.git`

## Licensing

This library is BSD-licensed.