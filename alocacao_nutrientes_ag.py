import random
import matplotlib.pyplot as plt

# Definir os parâmetros do problema
ALIMENTOS = [["Peito de frango", 23, 5, 5], ["Batata doce", 24, 0, 2], ["Arroz integral", 2.6, 26, 1], ["Ovo", 13, 8.9, 1.5], ["Feijao", 9.5, 1.4, 29]]

LIMITES = [0.1, 2]

TAM_POPULACAO = 200
TAXA_MUTACAO = 0.1
NUM_GERACOES = 100
TAXA_CRUZAMENTO = 0.8

#Criar listas para o gráfico de convergência
geracoes = []
melhores_fitnesses=[]

# Definir as funções de avaliação e cruzamento
def avaliar_individuo(individuo):
    # Avaliar a qualidade do indivíduo
    proteina = 0
    carboidrato = 0
    gordura = 0
    for i in range(len(individuo)):
        proteina += individuo[i] * ALIMENTOS[i][1]
        carboidrato += individuo[i] * ALIMENTOS[i][2]
        gordura += individuo[i] * ALIMENTOS[i][3]

    nutrientes = proteina + carboidrato + gordura

    relacao_proteina = abs(((proteina/nutrientes) * 100) - 20)
    relacao_carboidrato = abs(((carboidrato/nutrientes) * 100) - 55)
    relacao_gordura = abs(((gordura/nutrientes) * 100) - 35)

    return relacao_proteina + relacao_carboidrato + relacao_gordura

def cruzar_individuos(individuo1, individuo2):
    # Realizar o cruzamento dos indivíduos
    filho = []
    for i in range(len(individuo1)):
        filho.append((individuo1[i] + individuo2[i]) / 2)

    return filho

def torneio(g1, g2):
    g1.sort(key=avaliar_individuo)
    g2.sort(key=avaliar_individuo)
    return cruzar_individuos(g1[0], g2[0])


# Gerar a população inicial
populacao = []
for i in range(TAM_POPULACAO):
    individuo = [random.uniform(LIMITES[0], LIMITES[1]) for i in range(len(ALIMENTOS))]
    populacao.append(individuo)

# Executar o algoritmo genético
for geracao in range(NUM_GERACOES):

#Variável geracao já inicializada no loop 
#O Python permite que as variáveis sejam definidas em diferentes partes do código, como em loops, funções ou condicionais. 
    # Avaliar a qualidade da população
    fitnesses = [avaliar_individuo(individuo) for individuo in populacao]
    nova_populacao = []

    for i in range(TAM_POPULACAO):

        gladiadores1 = []
        gladiadores2 = []
    
        for j in range(5):
            gladiadores1.append(random.choice(populacao))
            gladiadores2.append(random.choice(populacao))
        filho1 = torneio(gladiadores1, gladiadores2)
        nova_populacao.append(filho1)

    # Realizar a mutação na nova população
    for i in range(len(nova_populacao)):
        individuo = nova_populacao[i]
        for j in range(len(individuo)):
            if random.random() < TAXA_MUTACAO:
                individuo[j] = (individuo[j] + random.uniform(LIMITES[0], LIMITES[1])) / 2
                

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
#print(geracoes)
plt.plot(geracoes, melhores_fitnesses)
plt.xlabel('Geração')
plt.ylabel('Melhor fitness')
plt.title('Convergência do Algoritmo Genético')
plt.show()
