rowSize = 50
sizeMarginLeft = 2
calc = True
tab = f'#{" " * sizeMarginLeft}'
resultDescription = "Resultado: "

def myPrint(text):
    aditionalSize = rowSize - len(text)
    print(f'#{" " * sizeMarginLeft}{text}{" " * aditionalSize}#')

def rowPrint(Fill = False):
    if Fill:
        row = "#"*(rowSize + sizeMarginLeft + 2)
    else:
        row = f'#{" " * (rowSize + sizeMarginLeft)}#'
    print(row)


rowPrint(True)
rowPrint()
while calc:
    operationType = str(input(f"{tab}Digite o tipo da operação [ + - / x ]: "))
    alpha = float(input(f"{tab}Digite o primeiro número da operação: "))
    omega = float(input(f"{tab}Digite o segundo  número da operação: "))

    if operationType == "+":
        result = resultDescription + str(alpha + omega)

    elif operationType == "-":
        result = resultDescription + str(alpha - omega)

    elif operationType == "x":
        result = resultDescription + str(alpha * omega)

    elif operationType == "/":
        result = resultDescription + str(alpha / omega)

    else:
        result = "Operador não definido!"

    myPrint(result)

    calcAnswer = str(input(f"{tab}Gostaria de continuar fazendo contas? [S/N]: "))

    if calcAnswer.upper() == "S":
        calc = True
    else:
        calc = False

rowPrint()
rowPrint(True)


