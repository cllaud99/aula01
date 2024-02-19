name = input('Insira seu nome: ')

salario = float( input('Digite seu salario: ') )

bonus = float(input('Digite o seu bonus: '))

BONUS_BASE = 1000

kpi = BONUS_BASE + salario * bonus


print(f"Olá, {name} seu bonus é: {kpi}")