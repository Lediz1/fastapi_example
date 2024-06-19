
### Criando ambiente Virtual

```bash
python3 -m venv venv

source venv/bin/activate
```

### eliminando todas as imagens do docker exceto volumes(optional) 

``` bash
docker system prune -a --volumes
```

Antes de executar o microserviço de produtos, é necessario que os serviços estejam em execução.Para executar, utilize o comando a abaixo.Os camandos se encontarm no arquivo makefile

``` bash
make services
```

### Executando os fastapi

Depois que os serviços estiverem sendo executados, inicie o microserviço de produtos.

``` bash
make run_docker_prod_app
```

### Url do swagger

``` bash
http://127.0.0.1:80/docs#/

```

Com o fastapi executando, abra o swagger ,no link acima, para ver os endpoints com seus comentarios e exemplos de execução.
 Voce pode executar os endpoints diretamente do swagger , que retornará um id da task de execução no celery.

<img title="a title" alt="Alt text" src="img/Captura de tela de 2024-06-19 10-43-29.png">
 
 
 Utilizando os endpoints , voce receberá os curl para caso queira executar via outro microserviço,postman ou qualquer outra ferramenta de requisição.

 O endpoint abaixo retorna os valores da task bastando informar o id da task
<img title="a title" alt="Alt text" src="img/Captura de tela de 2024-06-19 10-35-26.png">



### Access Flower

Nao foi utilizado o kafka pois a performance do celery,redis e visualização com flower foram mais apropriados para o teste. Basta abrir o flower e voce verá as tarefas da mensageria. 
``` bash
http://localhost:5557/tasks
```

### Executando os testes

Foram criados apenas alguns testes para demonstrar a execução dos testes integrados.

Obs: execute o docker de serviços antes de executar os testes,pois o database deve estar sendo executado par tal fim.

``` bash
make integration-tests
