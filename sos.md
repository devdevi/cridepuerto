docker-compose -f local.yml ps
docker-compose -f local.yml down
export COMPOSE_FILE=local.yml

docker-compose build
docker-compose up
docker-compose ps
docker-compose down


docker-compose run --rm django

docker-compose run --rm django python manage.py createsuperuser



docker-compose up
docker-compose ps

docker rm -f ID
docker rm -f cride-platzi_django_1
docker-compose run --rm service-port


docker container
docker images
docker volume
docker network


ls lista
rm remover
prune quitar
-m
-q


· Proxy models nos permite crear modelos sin crear una tabla,
Herencia multitabla



docker-compose run --rm --service-ports django
docker-compose run  --rm django python manage.py makemigrations

docker-compose ps
docker-compose down

docker volume ls
docker volume -rm


Processes : docker-compose -f local.yml ps
Stop app: docker-compose -f local.yml down
Enviroment var: export COMPOSE_FILE = local.yml
Build: docker-compose -f local.yml build
Run app: docker-compose -f local.yml up
Run service command: docker-compose run --rm SERVICE COMMAND
Stop service: docker rm -f SERVICE
Remove volume: docker volume rm -f <ID>
Run one service: docker-compose run --rm --service-ports SERVICE
Borrar_bd: docker volume rm cride_local_postgress_data
docker-compose run --rm django python manage.py migrate

"""
Borrar la migracion
"""


# Como correr un shell de python
docker-compose run --rm django python  manage.py shell_plus
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
https://www.techiediaries.com/resetting-django-migrations/
