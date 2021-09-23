# Some docker command for pg testing

Run new pg container
$ sudo docker run --rm -d --name pg-django -p 5433:5432  -e POSTGRES_PASSWORD=123pablo postgres

Connect by bash
$ sudo docker exec -it pg-django bash

