numeros = [1,2,3,4,5,5,5]

def duplicados(num):
    x = 0
    num.sort()
    dict = set(num)

    print("Há duplicados") if len(dict) != len(num) else print("Não há duplicados")

    for i in dict:
        print(f"{i}   -  {num.count(i)}")
        
duplicados(numeros)