notas = [7, 8, 6, 10, 5]

s = 0

for i in range(0, len(notas)):
    s = s + notas[i]

media = s / len(notas)

print("Média final:", media)

# Sugestão: renomear a variável s para soma, pois o nome atual
# não deixa claro o que ela representa. Também seria importante
# verificar se a lista está vazia antes de calcular a média,
# evitando uma divisão por zero