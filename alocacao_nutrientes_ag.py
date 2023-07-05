import random
import matplotlib.pyplot as plt

# Definir os parâmetros do problema
# Baseado em 100g
# Nome, Proteinas, Carboidratos, Gordura, Caloria


CAFE_CEREAIS = [["Biscoito Recheado Chocolate", 6, 71, 20, 472], ["Biscoito Salgado Cream Cracker", 10, 69, 14, 432],
["Cereal Matinal", 7, 84, 1, 382], ["Pao Frances", 8, 59, 3, 300]]

CAFE_FRUTAS = [["Abacate", 1, 6, 8, 96], ["Abacaxi", 1, 12, 0, 48], ["Banana prata", 1, 26, 0, 98],
["Coco", 4, 10, 0, 402], ["Goiaba vermelha", 1, 13, 0, 54], ["Laranja Pera", 1, 9, 0, 37], ["Maça Fuji", 0, 15, 0, 56],
["Maracujá", 2, 12, 2, 68], ["Melao", 1, 8, 0, 29], ["Morango", 1, 7, 0, 30]]

CAFE_BEBIDAS = [["Cafe", 15, 66, 12, 419], ["Agua de coco", 0, 5.3, 0, 21.5], ["Suco Laranja Pera", 0.7, 7.6, 0.1, 32.7], ["Suco de uva nectar", 0, 29, 0, 115], 
                      ["Leite UHT integral", 6, 8.8, 4, 113], ["Iogurte natural", 4, 2, 3, 51]]

REFEICAO_CEREAIS = [["Arroz integral cozido", 2.6, 25.8, 0.3, 123.5], ["Arroz tipo 1", 2.5, 28.1, 0.2, 128.3], ["Macarrao Instantaneo", 9, 62, 17, 432],
                  ["Feijao carioca", 20, 63, 1, 336], ["Lentilha", 23, 64, 1, 347]]

REFEICAO_VERDURAS_HORTALICAS = [["Abobrinha Italiana Refogada", 1.1, 4.2, 0.1, 24.4], ["Alface Lisa", 2, 2, 0, 14],
["Alho cru", 7, 24, 0, 113], ["Batata Doce Cozida", 0.6, 18.4, 0, 76.8], ["Beterraba Crua", 2, 11, 0, 49],
["Cará", 1.5, 18.9, 0, 77.6], ["Cenoura Cozida", 0.9, 6.7, 0.1, 29.9], ["Couve Crua", 3, 4, 1, 27],
["Espinafre Nova Zelândia Refogado", 2.7, 4.2, 0.9, 67.3], ["Mandioca Frita", 1.4, 50.3, 1.7, 300.1], 
["Nabo cru", 1, 4, 0, 18], ["Tomate com semente cru", 1, 3, 0, 15], ["Vagem crua", 2, 5, 0, 25]]

REFEICAO_PESCADOS = [["Corimbata Assado", 19, 0, 4.8, 261.5], ["Pintado Grelhado", 30.8, 0, 1.1, 152.2],
["File de Merluza Frito", 26.9, 0, 1.4, 191.6], ["Atum conserva em oleo", 26.2, 0, 1, 165.9]]

REFEICAO_CARNES = [["Carne bovina acem moida cozida", 26.7, 0, 10.9, 212.4], ["Carne bovina contra file sem gordura grelhado", 35.9, 0, 4.5, 193.7],
["Carne bovina costela assada", 28.8, 0, 27.7, 373], ["File mignon sem gordura grelhado", 33, 0, 9, 220],
["Carne bovina fraldinha com gordura cozida", 24, 0, 26, 338], ["Carne bovina lagarto cozida", 33, 0, 9, 221]]

REFEICAO_BEBIDAS = [["Refrigerante Guarana", 0, 10, 0, 38.7], ["Suco Laranja Pera", 0.7, 7.6, 0.1, 32.7], ["Suco de uva nectar", 0, 29, 0, 115]]



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
    calorias = 0
    
    for i in range(len(individuo)):
        #INDIVIDUO = [[[3, Quant], [9, Quant], [1, Quant]], [5, 9, 2, 1, 4], [3, 9, 1], [5, 9, 2, 1, 4]]
        # Nome, Proteinas, Carboidratos, Gordura, Caloria
        if i % 2 == 0:
            cafe = individuo[i]

            proteina += (cafe[0][1] * CAFE_CEREAIS[cafe[0][0]][1] + cafe[1][1] * CAFE_FRUTAS[cafe[1][0]][1] + 
                        cafe[2][1] * CAFE_BEBIDAS[cafe[2][0]][1])
            carboidrato += (cafe[0][1] * CAFE_CEREAIS[cafe[0][0]][2] + cafe[1][1] * CAFE_FRUTAS[cafe[1][0]][2] + 
                        cafe[2][1] * CAFE_BEBIDAS[cafe[2][0]][2])
            gordura += (cafe[0][1] * CAFE_CEREAIS[cafe[0][0]][3] + cafe[1][1] * CAFE_FRUTAS[cafe[1][0]][3] + 
                        cafe[2][1] * CAFE_BEBIDAS[cafe[2][0]][3])
            calorias += (cafe[0][1] * CAFE_CEREAIS[cafe[0][0]][4] + cafe[1][1] * CAFE_FRUTAS[cafe[1][0]][4] + 
                        cafe[2][1] * CAFE_BEBIDAS[cafe[2][0]][4])

        else:
            if i == 1:
                carne = REFEICAO_CARNES
            elif i == 3:
                carne = REFEICAO_PESCADOS

            cafe = individuo[i]

            proteina += (cafe[0][1] * REFEICAO_CEREAIS[cafe[0][0]][1] + cafe[1][1] * REFEICAO_VERDURAS_HORTALICAS[cafe[1][0]][1] + 
                        cafe[2][1] * carne[cafe[2][0]][1] + cafe[3][1] * REFEICAO_BEBIDAS[cafe[3][0]][1])
            carboidrato += (cafe[0][1] * REFEICAO_CEREAIS[cafe[0][0]][2] + cafe[1][1] * REFEICAO_VERDURAS_HORTALICAS[cafe[1][0]][2] + 
                        cafe[2][1] * carne[cafe[2][0]][2] + cafe[3][1] * REFEICAO_BEBIDAS[cafe[3][0]][2])
            gordura += (cafe[0][1] * REFEICAO_CEREAIS[cafe[0][0]][3] + cafe[1][1] * REFEICAO_VERDURAS_HORTALICAS[cafe[1][0]][3] + 
                        cafe[2][1] * carne[cafe[2][0]][3] + cafe[3][1] * REFEICAO_BEBIDAS[cafe[3][0]][3])
            calorias += (cafe[0][1] * REFEICAO_CEREAIS[cafe[0][0]][4] + cafe[1][1] * REFEICAO_VERDURAS_HORTALICAS[cafe[1][0]][4] + 
                        cafe[2][1] * carne[cafe[2][0]][4] + cafe[3][1] * REFEICAO_BEBIDAS[cafe[3][0]][4])




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
    CMC = [random.randint(0, len(CAFE_CEREAIS)), random.uniform(LIMITES[0], LIMITES[1])]
    CMF = [random.randint(0, len(CAFE_FRUTAS)), random.uniform(LIMITES[0], LIMITES[1])]
    CMB = [random.randint(0, len(CAFE_BEBIDAS)), random.uniform(LIMITES[0], LIMITES[1])]
    ACE = [random.randint(0, len(REFEICAO_CEREAIS)), random.uniform(LIMITES[0], LIMITES[1])]
    AVH = [random.randint(0, len(REFEICAO_VERDURAS_HORTALICAS)), random.uniform(LIMITES[0], LIMITES[1])]
    ACA = [random.randint(0, len(REFEICAO_CARNES)), random.uniform(LIMITES[0], LIMITES[1])]
    ABE = [random.randint(0, len(REFEICAO_BEBIDAS)), random.uniform(LIMITES[0], LIMITES[1])]
    CTC = [random.randint(0, len(CAFE_CEREAIS)), random.uniform(LIMITES[0], LIMITES[1])]
    CTF = [random.randint(0, len(CAFE_FRUTAS)), random.uniform(LIMITES[0], LIMITES[1])]
    CTB = [random.randint(0, len(CAFE_BEBIDAS)), random.uniform(LIMITES[0], LIMITES[1])]
    JCE = [random.randint(0, len(REFEICAO_CEREAIS)), random.uniform(LIMITES[0], LIMITES[1])]
    JVH = [random.randint(0, len(REFEICAO_VERDURAS_HORTALICAS)), random.uniform(LIMITES[0], LIMITES[1])]
    JPE = [random.randint(0, len(REFEICAO_PESCADOS)), random.uniform(LIMITES[0], LIMITES[1])]
    JBE = [random.randint(0, len(REFEICAO_BEBIDAS)), random.uniform(LIMITES[0], LIMITES[1])]

    individuo = [[CMC, CMF, CMB], [ACE, AVH, ACA, ABE], [CTC, CTF, CTB], [JCE, JVH, JPE, JBE]]
    populacao.append(individuo)
    
# CAFE, REFEICAO, LANCHE, REFEICAO
#INDIVIDUO = [[[3, Quant], [9, Quant], [1, Quant]], [5, 9, 2, 1, 4], [3, 9, 1], [5, 9, 2, 1, 4]]

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
