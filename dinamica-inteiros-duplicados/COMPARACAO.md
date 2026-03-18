# Comparação: `duplicados` vs `duplicados_com_ia`

## O que mudou?

A função original `duplicados` usa `set()` + `.count()` para contar as ocorrências de cada número. O problema é que `.count()` percorre a lista inteira para cada elemento do set, resultando em complexidade **O(n²)**.

A nova função `duplicados_com_ia` usa `Counter` do módulo `collections`, que percorre a lista uma única vez e já monta o dicionário de contagens. Isso reduz a complexidade para **O(n)**.

## Resumo das diferenças

| Aspecto | `duplicados` | `duplicados_com_ia` |
|---|---|---|
| Contagem | `set()` + `.count()` | `Counter()` |
| Complexidade | O(n²) | O(n) |
| Modifica a lista? | Sim (`num.sort()`) | Não |
| Retorna resultado? | Não | Sim (dicionário com duplicados) |

## Exemplo

```python
numeros = [1, 2, 3, 4, 5, 5, 5]

duplicados(numeros)        # O(n²)
duplicados_com_ia(numeros)  # O(n)
```

Ambas produzem a mesma saída, mas `duplicados_com_ia` é mais eficiente em listas grandes.
