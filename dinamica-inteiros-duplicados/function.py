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