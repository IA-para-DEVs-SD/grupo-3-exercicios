numeros = [1,2,3,4,5,5,5]

def duplicados(num):
    x = 0
    num.sort()
    dict = set(num)

    if len(dict) != len(num):
        for i in dict:
            print(f"{i}   -  {num.count(i)}")
    else: 
        print("Não há duplicados")
        return
        
duplicados(numeros)

from collections import Counter


def duplicados_com_ia(numeros):
    """Versão otimizada usando Counter - O(n) ao invés de O(n²)."""
    contagem = Counter(numeros)
    duplicados = {num: vezes for num, vezes in contagem.items() if vezes > 1}

    if duplicados:
        print("Há duplicados")
    else:
        print("Não há duplicados")

    for num, vezes in contagem.items():
        print(f"{num}   -  {vezes}")

    return duplicados


duplicados_com_ia(numeros)

