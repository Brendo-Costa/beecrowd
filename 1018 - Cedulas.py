"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.
Entrada

O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).
Saída

Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido.
Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
"""
#dividir por % retorna o resto da operação.
#dividir por / retorna a divisão com ponto flutuante.
#dividir por // retorna o valor inteiro da divisão.


n = int(input())
print(n)
divisao_100 = n//100
resto_100 = n%100
n = resto_100
print(f'{divisao_100} nota(s) de R$ 100,00')
divisao_50 = n//50
resto_50 = n%50
n = resto_50
print(f'{divisao_50} nota(s) de R$ 50,00')
divisao_20 = n//20
resto_20 = n%20
n = resto_20
print(f'{divisao_20} nota(s) de R$ 20,00')
divisao_10 = n//10
resto_10 = n%10
n = resto_10
print(f'{divisao_10} nota(s) de R$ 10,00')
divisao_5 = n//5
resto_5 = n%5
n = resto_5
print(f'{divisao_5} nota(s) de R$ 5,00')
divisao_2 = n//2
resto_2 = n%2
n = resto_2
print(f'{divisao_2} nota(s) de R$ 2,00')
divisao_1 = n//1
resto_1 = n%1
n = resto_1
print(f'{divisao_1} nota(s) de R$ 1,00')
    
