secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

number = int(input("Enter a number: "))

while number != secret_number:
    print("Ha ha! Você está preso no meu loop!")
    number = int(input("Enter a number: "))
    if number == secret_number:
        print("Muito bem, trouxa! Você está livre agora")