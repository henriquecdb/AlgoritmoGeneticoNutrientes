import random
import matplotlib.pyplot as plt

# INDIVIDUO = [[[3, Quant], [9, Quant], [1, Quant]], [[2, Quant], [3, Quant], [7, Quant], [1, Quant], [2, Quant]], ...]
# O individuo é composto de 4 partes. O primeiro array representa o café da manhã, o segundo almoço, o terceiro café da tarde e o quarto, a janta
# O café da manhã e da tarde é composto de alimentos de 3 categorias: cereal, fruta e bebida
# O almoço e janta é composto de alimentos de 4 categorias: 2 cereais, 2 verduras/hortaliças, carne(almoço) ou peixe(janta) e bebida
# O array [[3, Quant], [9, Quant], [1, Quant]] por exemplo, pode representar o café da manhã, sendo que os arrays [3, Quant], [9, Quant], [1, Quant] representam a posição do alimento na base de dados, exemplo CAFE_CEREAIS[3] e Quant a porção de 100g do alimento, sendo que Quant * 100 representa a quantidade em gramas



# Mínimo e máximo de porções de 100g para cada tipo de alimento.
LIMITE_CEREAIS = [0.5, 1]
LIMITE_FRUTAS = [2, 5]
LIMITE_BEBIDAS = [1, 2]
LIMITE_CARNES = [0.8, 1.5]
LIMITE_PEIXES = [0.5, 2]
LIMITE_VERDURAS = [0.05, 0.2]

# Parâmetros do algoritmos genético
TAM_POPULACAO = 1000
TAXA_MUTACAO = 0.1
NUM_GERACOES = 150
TAXA_CRUZAMENTO = 0.8


# Quantidades baseadas em 100g do alimento
# Ordem dos dados: Nome, Proteinas, Carboidratos, Gordura, Caloria

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

# Criar listas para o gráfico de convergência
geracoes = []
melhores_fitnesses=[]


# Função que retorna a quantidade de proteina, carboidrato, gordura e caloria totais de determinado individuo

def calcular_proteina_carboidrato_gordura_caloria(individuo):
    proteina = 0
    carboidrato = 0
    gordura = 0
    calorias = 0
    
    for i in range(len(individuo)):
        if i % 2 == 0: # Verdadeiro quando a refeição é café da manhã ou da tarde
            
            # Recebe a lista com o id e quantidade dos alimentos
            alimentos = individuo[i]
            
            # Percorre a lista com os alimentos, multiplicando a quantidade do alimento pela coluna do nutriente na base de dados e somando ao total de cada nutriente
            proteina += (alimentos[0][1] * CAFE_CEREAIS[alimentos[0][0]][1] + alimentos[1][1] * CAFE_FRUTAS[alimentos[1][0]][1] + 
                        alimentos[2][1] * CAFE_BEBIDAS[alimentos[2][0]][1])
            carboidrato += (alimentos[0][1] * CAFE_CEREAIS[alimentos[0][0]][2] + alimentos[1][1] * CAFE_FRUTAS[alimentos[1][0]][2] + 
                        alimentos[2][1] * CAFE_BEBIDAS[alimentos[2][0]][2])
            gordura += (alimentos[0][1] * CAFE_CEREAIS[alimentos[0][0]][3] + alimentos[1][1] * CAFE_FRUTAS[alimentos[1][0]][3] + 
                        alimentos[2][1] * CAFE_BEBIDAS[alimentos[2][0]][3])
            calorias += (alimentos[0][1] * CAFE_CEREAIS[alimentos[0][0]][4] + alimentos[1][1] * CAFE_FRUTAS[alimentos[1][0]][4] + 
                        alimentos[2][1] * CAFE_BEBIDAS[alimentos[2][0]][4])

        else:
            if i == 1: # Verdadeiro quando a refeição é o almoço
                carne = REFEICAO_CARNES
            elif i == 3: # Verdadeiro quando a refeição é a janta
                carne = REFEICAO_PESCADOS

            alimentos = individuo[i]

            proteina += (alimentos[0][1] * REFEICAO_CEREAIS[alimentos[0][0]][1] + alimentos[1][1] * REFEICAO_CEREAIS[alimentos[1][0]][1] + alimentos[2][1] * REFEICAO_VERDURAS_HORTALICAS[alimentos[2][0]][1] + 
                        alimentos[3][1] * REFEICAO_VERDURAS_HORTALICAS[alimentos[3][0]][1] + alimentos[4][1] * carne[alimentos[4][0]][1] + alimentos[5][1] * REFEICAO_BEBIDAS[alimentos[5][0]][1])
            carboidrato += (alimentos[0][1] * REFEICAO_CEREAIS[alimentos[0][0]][2] + alimentos[1][1] * REFEICAO_CEREAIS[alimentos[1][0]][2] + alimentos[2][1] * REFEICAO_VERDURAS_HORTALICAS[alimentos[2][0]][2] + 
                        alimentos[3][1] * REFEICAO_VERDURAS_HORTALICAS[alimentos[3][0]][2] + alimentos[4][1] * carne[alimentos[4][0]][2] + alimentos[5][1] * REFEICAO_BEBIDAS[alimentos[5][0]][2])
            gordura += (alimentos[0][1] * REFEICAO_CEREAIS[alimentos[0][0]][3] + alimentos[1][1] * REFEICAO_CEREAIS[alimentos[1][0]][3] + alimentos[2][1] * REFEICAO_VERDURAS_HORTALICAS[alimentos[2][0]][3] + 
                        alimentos[3][1] * REFEICAO_VERDURAS_HORTALICAS[alimentos[3][0]][3] + alimentos[4][1] * carne[alimentos[4][0]][3] + alimentos[5][1] * REFEICAO_BEBIDAS[alimentos[5][0]][3])
            calorias += (alimentos[0][1] * REFEICAO_CEREAIS[alimentos[0][0]][4] + alimentos[1][1] * REFEICAO_CEREAIS[alimentos[1][0]][4] + alimentos[2][1] * REFEICAO_VERDURAS_HORTALICAS[alimentos[2][0]][4] + 
                        alimentos[3][1] * REFEICAO_VERDURAS_HORTALICAS[alimentos[3][0]][4] + alimentos[4][1] * carne[alimentos[4][0]][4] + alimentos[5][1] * REFEICAO_BEBIDAS[alimentos[5][0]][4])

    return proteina, carboidrato, gordura, calorias




# Avalia o individuo com base nas restrições e valores desejados de nutrientes e calorias
def avaliar_individuo(individuo):
    proteina, carboidrato, gordura, caloria = calcular_proteina_carboidrato_gordura_caloria(individuo)
    nutrientes = proteina + carboidrato + gordura
    

    # Calcula a porcentagem de proteina, carboidrato e gordura do individuo
    relacao_proteina = abs(((proteina/nutrientes) * 100) - 20)
    relacao_carboidrato = abs(((carboidrato/nutrientes) * 100) - 55)
    relacao_gordura = abs(((gordura/nutrientes) * 100) - 35)

    fitness = relacao_proteina + relacao_carboidrato + relacao_gordura
    
    # Se caloria ultrapassar 2500kcal penaliza o individuo
    if caloria > 2500:
        fitness *= 10

    return fitness

def cruzar_individuos(individuo1, individuo2):
    # O filho recebe o café da manhã e da tarde do individuo1 e almoço e janta do individuo2
    filho = [individuo1[0], individuo2[1], individuo1[2], individuo2[3]]
    return filho

def torneio(g1, g2):
    g1.sort(key=avaliar_individuo)
    g2.sort(key=avaliar_individuo)
    return cruzar_individuos(g1[0], g2[0])

def gerar_individuo():

    # Cria os arrays contendo o id do alimento e quantidade de forma aleatória, respeitando os limites impostos
    CMC = [random.randint(0, len(CAFE_CEREAIS) - 1), random.uniform(LIMITE_CEREAIS[0], LIMITE_CEREAIS[1])]
    CMF = [random.randint(0, len(CAFE_FRUTAS) - 1), random.uniform(LIMITE_FRUTAS[0], LIMITE_FRUTAS[1])]
    CMB = [random.randint(0, len(CAFE_BEBIDAS) - 1), random.uniform(LIMITE_BEBIDAS[0], LIMITE_BEBIDAS[1])]
    ACE = [random.randint(0, len(REFEICAO_CEREAIS) - 1), random.uniform(LIMITE_CEREAIS[0], LIMITE_CEREAIS[1])]
    ACE2 = [random.randint(0, len(REFEICAO_CEREAIS) - 1), random.uniform(LIMITE_CEREAIS[0], LIMITE_CEREAIS[1])]
    AVH = [random.randint(0, len(REFEICAO_VERDURAS_HORTALICAS) - 1), random.uniform(LIMITE_VERDURAS[0], LIMITE_VERDURAS[1])]
    AVH2 = [random.randint(0, len(REFEICAO_VERDURAS_HORTALICAS) - 1), random.uniform(LIMITE_VERDURAS[0], LIMITE_VERDURAS[1])]
    ACA = [random.randint(0, len(REFEICAO_CARNES) - 1), random.uniform(LIMITE_CARNES[0], LIMITE_CARNES[1])]
    ABE = [random.randint(0, len(REFEICAO_BEBIDAS) - 1), random.uniform(LIMITE_BEBIDAS[0], LIMITE_BEBIDAS[1])]
    CTC = [random.randint(0, len(CAFE_CEREAIS) - 1), random.uniform(LIMITE_CEREAIS[0], LIMITE_CEREAIS[1])]
    CTF = [random.randint(0, len(CAFE_FRUTAS) - 1), random.uniform(LIMITE_FRUTAS[0], LIMITE_FRUTAS[1])]
    CTB = [random.randint(0, len(CAFE_BEBIDAS) - 1), random.uniform(LIMITE_BEBIDAS[0], LIMITE_BEBIDAS[1])]
    JCE = [random.randint(0, len(REFEICAO_CEREAIS) - 1), random.uniform(LIMITE_CEREAIS[0], LIMITE_CEREAIS[1])]
    JCE2 = [random.randint(0, len(REFEICAO_CEREAIS) - 1), random.uniform(LIMITE_CEREAIS[0], LIMITE_CEREAIS[1])]
    JVH = [random.randint(0, len(REFEICAO_VERDURAS_HORTALICAS) - 1), random.uniform(LIMITE_VERDURAS[0], LIMITE_VERDURAS[1])]
    JVH2 = [random.randint(0, len(REFEICAO_VERDURAS_HORTALICAS) - 1), random.uniform(LIMITE_VERDURAS[0], LIMITE_VERDURAS[1])]
    JPE = [random.randint(0, len(REFEICAO_PESCADOS) - 1), random.uniform(LIMITE_PEIXES[0], LIMITE_PEIXES[1])]
    JBE = [random.randint(0, len(REFEICAO_BEBIDAS) - 1), random.uniform(LIMITE_BEBIDAS[0], LIMITE_BEBIDAS[1])]

    individuo = [[CMC, CMF, CMB], [ACE, ACE2, AVH, AVH2, ACA, ABE], [CTC, CTF, CTB], [JCE, JCE2, JVH, JVH2, JPE, JBE]]
    return individuo


def imprimir_dieta(individuo):
    cafe_manha = individuo[0]
    almoco = individuo[1]
    cafe_tarde = individuo[2]
    janta = individuo[3]
    

    # Armazena o nome do alimento e a sua quantidade em gramas
    cereal = CAFE_CEREAIS[cafe_manha[0][0]][0]
    porcao_cereal = cafe_manha[0][1] * 100
    fruta = CAFE_FRUTAS[cafe_manha[1][0]][0]
    porcao_fruta = cafe_manha[1][1] * 100
    bebida = CAFE_BEBIDAS[cafe_manha[2][0]][0]
    porcao_bebida = cafe_manha[2][1] * 100

    print(cereal, " -> ", porcao_cereal, "g\n", fruta, " -> ", porcao_fruta,"g\n", bebida, " -> ", porcao_bebida, "g")

    cereal = [REFEICAO_CEREAIS[almoco[0][0]][0], REFEICAO_CEREAIS[almoco[1][0]][0]]
    porcao_cereal = [almoco[0][1] * 100, almoco[1][1] * 100]
    verdura = [REFEICAO_VERDURAS_HORTALICAS[almoco[2][0]][0], REFEICAO_VERDURAS_HORTALICAS[almoco[3][0]][0]]
    porcao_verdura = [almoco[2][1] * 100, almoco[3][1] * 100]
    carne = REFEICAO_CARNES[almoco[4][0]][0]
    porcao_carne = almoco[4][1] * 100
    bebida = REFEICAO_BEBIDAS[almoco[5][0]][0]
    porcao_bebida = almoco[5][1] * 100

    print(cereal, " -> ", porcao_cereal, "g\n", verdura, " -> ", porcao_verdura,"g\n", carne, " -> ", porcao_carne, "g\n", bebida, " -> ", porcao_bebida, "g")

    cereal = CAFE_CEREAIS[cafe_tarde[0][0]][0]
    porcao_cereal = cafe_tarde[0][1] * 100
    fruta = CAFE_FRUTAS[cafe_tarde[1][0]][0]
    porcao_fruta = cafe_tarde[1][1] * 100
    bebida = CAFE_BEBIDAS[cafe_tarde[2][0]][0]
    porcao_bebida = cafe_tarde[2][1] * 100

    print(cereal, " -> ", porcao_cereal, "g\n", fruta, " -> ", porcao_fruta,"g\n", bebida, " -> ", porcao_bebida, "g")

    cereal = [REFEICAO_CEREAIS[janta[0][0]][0], REFEICAO_CEREAIS[janta[1][0]][0]]
    porcao_cereal = [janta[0][1] * 100, janta[1][1] * 100]
    verdura = [REFEICAO_VERDURAS_HORTALICAS[janta[2][0]][0], REFEICAO_VERDURAS_HORTALICAS[janta[3][0]][0]]
    porcao_verdura = [janta[2][1] * 100, janta[3][1] * 100]
    carne = REFEICAO_PESCADOS[janta[4][0]][0]
    porcao_carne = janta[4][1] * 100
    bebida = REFEICAO_BEBIDAS[janta[5][0]][0]
    porcao_bebida = janta[5][1] * 100

    print(cereal, " -> ", porcao_cereal, "g\n", verdura, " -> ", porcao_verdura,"g\n", carne, " -> ", porcao_carne, "g\n", bebida, " -> ", porcao_bebida, "g")

    proteina, carboidrato, gordura, caloria = calcular_proteina_carboidrato_gordura_caloria(individuo)
    
    print("Proteina total: ", proteina, "g\nCarboidrato total: ", carboidrato, "g\nGordura total: ", gordura, "g\nCaloria total: ", caloria, "kcal")
    print(avaliar_individuo(individuo))

# Gerar a população inicial
populacao = []
for i in range(TAM_POPULACAO):
    individuo = gerar_individuo()
    populacao.append(individuo)
    
# CAFE, REFEICAO, LANCHE, REFEICAO
#INDIVIDUO = [[[3, Quant], [9, Quant], [1, Quant]], [5, 9, 2, 1, 4], [3, 9, 1], [5, 9, 2, 1, 4]]

melhores_individuos = []
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
        if random.random() < TAXA_MUTACAO:
            nova_populacao[i] = gerar_individuo()
                

    # Substituir a população anterior pela nova população
    populacao = nova_populacao

    # Imprimir a melhor solução encontrada até o momento
    melhor_individuo = min(populacao, key=avaliar_individuo)
    melhores_individuos.append(melhor_individuo)
    melhor_fitness = avaliar_individuo(melhor_individuo)
    geracoes = list(range(NUM_GERACOES))
    #geracoes.append(geracao)
    melhores_fitnesses.append(melhor_fitness)
    #print(f"Melhor solução na geração {geracao}: {melhor_individuo} (fitness = {melhor_fitness})")



melhor_individuo = min(melhores_individuos, key=avaliar_individuo)
print("MELHOR INDIVIDUO -> ", melhor_individuo)
imprimir_dieta(melhor_individuo)




# Plotar o gráfico de convergência
#print(geracoes)
plt.plot(geracoes, melhores_fitnesses)
plt.xlabel('Geração')
plt.ylabel('Melhor fitness')
plt.title('Convergência do Algoritmo Genético')
plt.show()
