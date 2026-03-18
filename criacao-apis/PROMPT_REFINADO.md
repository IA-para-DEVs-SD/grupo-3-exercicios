# Prompt Refinado — criacao-apis

## Prompt único otimizado

> Crie uma API REST com Spring Boot na pasta `criacao-apis` contendo os endpoints GET, POST e DELETE para um recurso chamado `Item`. Use Spring Data JPA com banco H2 em memória, popule 5 registros mockados via `data.sql` (Notebook, Mouse, Teclado, Monitor, Headset), habilite o console H2 em `/h2-console` e empacote tudo em um Dockerfile multi-stage (Maven + JRE 17) expondo a porta 8080.

---

## Resultado esperado

```
criacao-apis/
├── Dockerfile
├── pom.xml
└── src/main/
    ├── java/com/api/
    │   ├── ApiApplication.java
    │   ├── controller/ItemController.java
    │   ├── model/Item.java
    │   └── repository/ItemRepository.java
    └── resources/
        ├── application.properties
        └── data.sql
```

## Endpoints

| Método | Rota        | Descrição            |
|--------|-------------|----------------------|
| GET    | /itens      | Lista todos os itens |
| POST   | /itens      | Cria um novo item    |
| DELETE | /itens/{id} | Remove pelo id       |

