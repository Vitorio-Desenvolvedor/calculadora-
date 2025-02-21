#--> calculadora simples em python
def somar(a, b):
    return a + b #--> função de somar 

def subtrair(a, b):
    return a - b #--> função de subtrair

def multiplicar(a, b):
    return a * b #--> função de multiplicar

def dividir(a, b):
    if b == 0: #--> gerar um erro quando (b) for igual a zero(0)
        return "Erro: Divisão por zero!"
    return a / b #--> função de dividir

# Função principal
def main():
    print("=== Calculadora Simples ===") #--> ondem de operação
    print("Escolha uma operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    escolha = input("Digite o número da operação desejada: ") #--> escolher qual operação vai ser

    if escolha in ["1", "2", "3", "4"]:
        num1 = int(input("Digite o primeiro número: ")) #--> função de digitar primeiro número
        num2 = int(input("Digite o segundo número: ")) #--> função de digitar segundo número

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
