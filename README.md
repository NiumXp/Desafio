
## Executando

Execute os seguintes comandos para rodar o projeo
```
docker-compose up -d
```

### Primeira vez
Caso seja a primeira vez executando o projeto, execute este comando também:
```
docker container exec django_api python manage.py migrate
```
Após isso, acesse [localhost:8080/table/dump](localhost:8080/table/dump) para preencher o banco de dados com as informações.

> Acesse [localhost:8080/table](localhost:8080/table) assim que o projeto estiver rodando.
