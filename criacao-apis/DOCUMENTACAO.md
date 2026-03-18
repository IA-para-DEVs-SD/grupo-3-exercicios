# Documentação — criacao-apis

Registro de todos os prompts utilizados para construção desta API.

---

## Prompts

**1.** crie uma api, na pasta criacao-apis, com os endpoints get, post e delete.

**2.** stack: springboot

**3.** agora suba o projeto

**4.** crie um dockerfile, e dentro deste container faça todas as configurações necessárias para que a minha api funcione.

**5.** crie dados mockados com o h2, para efeito de teste. faça também o curl dos endpoints.

**6.** crie um .md com todos prompts usados até o momento. esse .md será a nossa documentação.

---

## Estrutura do Projeto

```
criacao-apis/
├── Dockerfile
├── pom.xml
├── DOCUMENTACAO.md
└── src/
    └── main/
        ├── java/com/api/
        │   ├── ApiApplication.java
        │   ├── controller/
        │   │   └── ItemController.java
        │   ├── model/
        │   │   └── Item.java
        │   └── repository/
        │       └── ItemRepository.java
        └── resources/
            ├── application.properties
            └── data.sql
```

---

## Como rodar

```bash
docker build -t criacao-apis .
docker run -p 8080:8080 criacao-apis
```

---

## Endpoints

| Método | Rota          | Descrição              |
|--------|---------------|------------------------|
| GET    | /itens        | Lista todos os itens   |
| POST   | /itens        | Cria um novo item      |
| DELETE | /itens/{id}   | Remove um item pelo id |

---

## Exemplos de uso (curl)

```bash
# GET
curl http://localhost:8080/itens

# POST
curl -X POST http://localhost:8080/itens \
  -H "Content-Type: application/json" \
  -d '{"nome": "Webcam"}'

# DELETE
curl -X DELETE http://localhost:8080/itens/1
```

---

## Dados mockados (H2)

Inseridos via `data.sql` na inicialização:

| id | nome     |
|----|----------|
| 1  | Notebook |
| 2  | Mouse    |
| 3  | Teclado  |
| 4  | Monitor  |
| 5  | Headset  |

Console H2: `http://localhost:8080/h2-console`
- JDBC URL: `jdbc:h2:mem:testdb`
- Usuário: `sa`
- Senha: _(em branco)_
