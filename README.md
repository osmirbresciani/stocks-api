
# Stocks-API
> API que retorna os melhores dias de negociação visando o maior lucro.


# Pré-requisitos

* Docker
* docker-compose
* Python 3.7


## Instalação

Linux:

Acesse o diretório do projeto:
```$ cd stocks-api```

Monte a imagem:
```$ docker build .```

Rode a aplicação:
```$ docker-compose up```


## Como usar

###1. **GET** - Diretório Raíz:

```{{url}}/```

Onde a ```{{url}}``` é o IP interno mais a porta liberada, exemplo:

```192.168.0.1:5000/```

Exemplo utilizando o Postgres:

![gethome](https://user-images.githubusercontent.com/36646849/75824895-1bfebe00-5d83-11ea-8001-deb973b2a5eb.png)

Resposta:

![gethomeres](https://user-images.githubusercontent.com/36646849/75824969-389af600-5d83-11ea-8b44-e76a373a61a6.png)



###2. **POST** - Enviando as cotações:

```{{url}}/send_rates```

_**Headers**_

**Content-Type** application/json

_**BODY**_

```
{
  "rates": [
    x,
    y,
    z,
    a,
    b,
    c
  ]
}
```

Onde os elementos do array, ```x,y,z,a,b,c```, são as cotações nos diferentes dias. Não há limites de cotações a serem enviadas.

Exemplo utilizando o Postman:

![send_rates](https://user-images.githubusercontent.com/36646849/75824574-82371100-5d82-11ea-8c21-f7d98881ed3f.png)

###3. **GET** - Retornando o melhor trade e o lucro resultante:

```{{url}}/trade```

Exemplo:

```192.168.0.1:5000/trade```

Exemplo utilizando o Postgres:

![gettrade](https://user-images.githubusercontent.com/36646849/75825141-94657f00-5d83-11ea-9fc2-310a35c5451b.png)

Resposta:

![gettraderes](https://user-images.githubusercontent.com/36646849/75825172-a3e4c800-5d83-11ea-87ba-181825102848.png)


