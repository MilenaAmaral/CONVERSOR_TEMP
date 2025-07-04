import time


def celsius_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_celsius(f):
    return (f - 32) * 5/9


print("Conversor de temperatura")
print("Digite 1 para converter Celsius para Fahrenheit")
print("Ou digite 2 para converter Fahrenheit para Celsius")

time.sleep(3)

opcao = input("Escolha a opção (1 ou 2): ")

if opcao == "1":
    c = float(input("Digite a temperatura em Celsius:  "))
    f = celsius_fahrenheit(c)
    print(f"{c:2f}°C é igual á {f:.2f}°F ")

elif opcao == "2":
    f = float(input("Digite a temperatura em Fahrenheit: "))
    c = fahrenheit_celsius(f)
    print(f"{f:.2f}°F é igual á {c:.2f}°C ")

else:
    print("Opção inválida, tente digitando 1 ou 2!")
