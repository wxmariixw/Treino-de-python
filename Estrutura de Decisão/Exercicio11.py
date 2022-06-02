salario = float(input('Oba, Aumento! Quer descobrir de quanto será o seu? Digite aqui seu salário atual: '))

if salario <= 280:
    aumento = (salario * 0.2)
    salarioAumento = salario + aumento
    print (f'Seu salário era: R${salario:.2f}\nTeve um aumento de: 20%\nNo valor de: R${aumento:.2f}\nValor final: R${salarioAumento:.2f}')
elif salario < 700:
    aumento = (salario * 0.15)
    salarioAumento = salario + aumento
    print (f'Seu salário era: R${salario:.2f}\nTeve um aumento de: 15%\nNo valor de: R${aumento:.2f}\nValor final: R${salarioAumento:.2f}')
elif salario < 1500:
    aumento = (salario * 0.1)
    salarioAumento = salario + aumento
    print (f'Seu salário era: R${salario:.2f}\nTeve um aumento de: 10%\nNo valor de: R${aumento:.2f}\nValor final: R${salarioAumento:.2f}')
else:
    aumento = (salario * 0.5)
    salarioAumento = salario + aumento
    print (f'Seu salário era: R${salario:.2f}\nTeve um aumento de: 5%\nNo valor de: R${aumento:.2f}\nValor final: R${salarioAumento:.2f}')