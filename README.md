## Dev setup

```
docker-compose build --pull
docker-compose run web migrate
docker-compose run web createsuperuser
docker-compose up -d
```

### Migrations
```
docker-compose run web makemigrations
docker-compose run web migrate
```

### Stop everything
```
docker-compose stop
docker-compose rm -v
rm datetimefieldbroken/db.sqlite3
```
