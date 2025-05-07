import random

numero_secreto = random.randint(1, 100)
tentativas = 10  

print("Bem-vindo ao jogo: Adivinha o Número Secreto!")
print("Regras: Tente adivinhar o número entre 1 e 100.")
print(f"Você tem {tentativas} tentativas.\n")

for i in range(tentativas):
    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break
    elif palpite < numero_secreto:
        print("Dica: O número secreto é MAIOR.\n")
    else:
        print("Dica: O número secreto é MENOR.\n")

if palpite != numero_secreto:
    print(f"Fim de jogo! O número secreto era {numero_secreto}.")
