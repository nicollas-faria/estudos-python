atleta1 = input('Digite o nome do atleta, a distancia percorrida(km) e o tempo que levou.: ').split()
nome1 = (atleta1[0])
distancia1 = float(atleta1[1])
tempo1 = int(atleta1[2])

atleta2 = input('Digite o nome do atleta, a distancia percorrida(km) e o tempo que levou.: ').split()
nome2 = (atleta2[0])
distancia2 = float(atleta2[1])
tempo2 = int(atleta2[2])

media_distancia = (distancia1 + distancia2) / 2
diferenca_tempo = abs(tempo1 - tempo2)

print(f'Atleta 1: {nome1}\n Tempo: {tempo1}min\n Distancia: {distancia1}km\n')
print(f'Atleta 2: {nome2}\n Tempo: {tempo2}min\n Distancia: {distancia2}km\n')
print(f'Média de distância percorrida: {media_distancia}km\nDiferença de tempo: {diferenca_tempo} minutos')
