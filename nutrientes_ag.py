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
