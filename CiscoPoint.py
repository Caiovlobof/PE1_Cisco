year = int(input("Type a year: "))

if year < 1582:
    print("Não dentro do período do calendário gregoriano")
else:
    if year % 4 != 0:
        print("Ano comum")
    elif year % 100 != 0:
        print("Ano bissexto")
    elif year % 400 != 0:
        print("Ano comum")
    else:
        print("Ano bissexto")