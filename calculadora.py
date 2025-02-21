# criando uma calculadora simples no python
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

# Função principal
def main():
    print("=== Calculadora Simples ===")
    print("Escolha uma operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    escolha = input("Digite o número da operação desejada: ")

    if escolha in ["1", "2", "3", "4"]:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        operacoes = {
            "1": ("Soma", somar),
            "2": ("Subtração", subtrair),
            "3": ("Multiplicação", multiplicar),
            "4": ("Divisão", dividir),
        }

        nome_operacao, funcao = operacoes[escolha]
        resultado = funcao(num1, num2)

        print(f"Resultado da {nome_operacao}: {resultado}")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
