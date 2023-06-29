import random
import matplotlib.pyplot as plt

# CALORIAS = 3
TAM_POPULACAO = 100 # 50
TAXA_MUTACAO = 0.05
TAXA_CRUZAMENTO = 0.1
NUM_GERACOES = 150 # 100
TAXA_ELITISMO = 0.1
TAM = TAXA_ELITISMO * TAM_POPULACAO
TAM = int(TAM)
F = 0.8

# Baseado em 100g
# Nome, Proteinas, Carboidratos, Gordura, Caloria
CEREAIS_DERIVADOS = [["Arroz integral cozido", 2.6, 25.8, 0.3, 123.5], ["Arroz tipo 1", 2.5, 28.1, 0.2, 128.3],
["Biscoito Recheado Chocolate", 6, 71, 20, 472], ["Biscoito Salgado Cream Cracker", 10, 69, 14, 432],
["Cereal Matinal", 7, 84, 1, 382], ["Macarrao Instantaneo", 9, 62, 17, 432], ["Pao Frances", 8, 59, 3, 300]]

VERDURAS_HORTALIÇAS_DERIVADOS = [["Abobrinha Italiana Refogada", 1.1, 4.2, 0.1, 24.4], ["Alface Lisa", 2, 2, 0, 14],
["Alho cru", 7, 24, 0, 113], ["Batata Doce Cozida", 0.6, 18.4, 0, 76.8], ["Beterraba Crua", 2, 11, 0, 49],
["Cará", 1.5, 18.9, 0, 77.6], ["Cenoura Cozida", 0.9, 6.7, 0.1, 29.9], ["Couve Crua", 3, 4, 1, 27],
["Espinafre Nova Zelândia Refogado", 2.7, 4.2, 0.9, 67.3], ["Mandioca Frita", 1.4, 50.3, 1.7, 300.1], 
["Nabo cru", 1, 4, 0, 18], ["Tomate com semente cru", 1, 3, 0, 15], ["Vagem crua", 2, 5, 0, 25]]

FRUTAS_DERIVADOS = [["Abacate", 1, 6, 8, 96], ["Abacaxi", 1, 12, 0, 48], ["Banana prata", 1, 26, 0, 98],
["Coco", 4, 10, 0, 402], ["Goiaba vermelha", 1, 13, 0, 54], ["Laranja Pera", 1, 9, 0, 37], ["Maça Fuji", 0, 15, 0, 56],
["Maracujá", 2, 12, 2, 68], ["Melao", 1, 8, 0, 29], ["Morango", 1, 7, 0, 30]]

PESCADOS = [["Corimbata Assado", 19, 0, 4.8, 261.5], ["Pintado Grelhado", 30.8, 0, 1.1, 152.2],
["File de Merluza Frito", 26.9, 0, 1.4, 191.6], ["Atum conserva em oleo", 26.2, 0, 1, 165.9]]

CARNES_DERIVADOS = []

#Criar listas para o gráfico de convergência
geracoes = []
melhores_fitnesses=[]

def steady_state(populacao, nova_populacao):
    populacao.sort(key=avaliar_individuo)
    for i in populacao:
        individuo_aux = random.choice(nova_populacao)
        if avaliar_individuo(i) < avaliar_individuo(individuo_aux):
            i = individuo_aux
        
def elitismo(populacao):
    elite = []
    populacao.sort(reverse=True, key=avaliar_individuo)
    for i in range(TAM):
        elite.append(populacao[i])
        populacao.remove(populacao[i])
    return elite

def torneio(populacao):
    s = random.sample(populacao, 4)
    return min(s, key=avaliar_individuo)   

def avaliar_individuo(individuo):
    sum_prot = individuo[0]*0.23 + individuo[1]*0.24 + individuo[2]*0.026 + individuo[3]*0.13 + individuo[4]*0.095
    sum_gord = individuo[0]*0.05 + individuo[1]*0 + individuo[2]*0.26 + individuo[3]*0.089 + individuo[4]*0.014
    sum_carb = individuo[0]*0.05 + individuo[1]*0.02 + individuo[2]*0.01 + individuo[3]*0.015 + individuo[4]*0.29

    total_sum = sum_carb + sum_prot + sum_gord

    porcProt = (sum_prot/total_sum) * 100
    porcGord = (sum_gord/total_sum) * 100
    porcCarb = (sum_carb/total_sum) * 100

    difProt = abs(porcProt-30)
    difGord = abs(porcGord-15)
    difCarb = abs(porcCarb-55)

    return difProt + difGord + difCarb


def cruzar_individuos(individuo1, individuo2):
    # Realizar o cruzamento dos indivíduos
    ponto_corte = random.randint(1, len(individuo1) - 1)
    filho1 = individuo1[:ponto_corte] + individuo2[ponto_corte:]
    filho2 = individuo2[:ponto_corte] + individuo1[ponto_corte:]
    return filho1, filho2

def gerar_aleatorios(parental):
    vetor_aux = []
    while (len(vetor_aux) < 3):
        aleat = random.choice(populacao)
        if aleat not in vetor_aux and aleat != parental:
            vetor_aux.append(aleat)
    return vetor_aux

# Gerar a população inicial
populacao = []
for i in range(TAM_POPULACAO):
    individuo = []
    for j in range(5):
        valor = random.randint(0, 200) + random.random()
        individuo.append(valor)
    populacao.append(individuo)

# Executar o algoritmo genético
for geracao in range(NUM_GERACOES):
#Variável geracao já inicializada no loop 
#O Python permite que as variáveis sejam definidas em diferentes partes do código, como em loops, funções ou condicionais. 
    # Avaliar a qualidade da população
    fitnesses = [avaliar_individuo(individuo) for individuo in populacao]

    # Selecionar dois indivíduos aleatoriamente e cruzá-los
    nova_populacao = []
    for i in range(TAM_POPULACAO):
        pai1 = torneio(populacao)
        pai2 = torneio(populacao)
        filho1, filho2 = cruzar_individuos(pai1, pai2)
        nova_populacao.append(filho1)
        nova_populacao.append(filho2)

    # Realizar a mutação na nova população
    for i in range(len(nova_populacao)):
        individuo = nova_populacao[i]
        for j in range(len(individuo)):
            if random.random() < TAXA_MUTACAO:
                valor = random.randint(0, 200) + random.random()
                individuo[j] = valor

    # Substituir a população anterior pela nova população
    populacao = nova_populacao
    # Imprimir a melhor solução encontrada até o momento
    melhor_individuo = min(populacao, key=avaliar_individuo)
    melhor_fitness = avaliar_individuo(melhor_individuo)
    geracoes = list(range(NUM_GERACOES))
    #geracoes.append(geracao)
    melhores_fitnesses.append(melhor_fitness)
    print(f"Melhor solução na geração {geracao}: {melhor_individuo} (fitness = {melhor_fitness})")


# Plotar o gráfico de convergência
# print(geracoes)
plt.plot(geracoes, melhores_fitnesses)
plt.xlabel('Geração')
plt.ylabel('Melhor fitness')
plt.title('Convergência do Algoritmo Genético')
plt.show()
