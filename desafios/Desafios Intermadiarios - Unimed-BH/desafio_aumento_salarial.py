# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
import locale

salario = int(input()) 

if (salario > 2000):
    reajuste = 0.05

elif (salario > 1500.01):
    reajuste = 0.1

elif (salario > 900.01):
    reajuste = 0.12

elif (salario > 600.01):
    reajuste = 0.13

else:
    reajuste = 0.17


# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e o índice reajustado (em porcentagem)

novo_salario = salario * (1 + reajuste)
ganho_salario = novo_salario - salario

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {ganho_salario:.2f}")
print(f"Em percentual: {(reajuste * 100):.0f} %")