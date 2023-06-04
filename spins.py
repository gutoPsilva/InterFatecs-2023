qntd = int(input())
while qntd != 0:
    resultado = ""
    spin = 1
    soma = 3
    while spin <= qntd:
        resultado += (str(spin) if resultado == "" else (" " + str(spin)))
        spin = spin + soma
        soma += 2
    print(resultado)
    qntd = int(input())
