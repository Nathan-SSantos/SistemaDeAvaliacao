# Inicializando variáveis para armazenar os vencedores e as notas
vencedor_frutas_produto = ""
vencedor_frutas_nota = -1
vencedor_vegetais_produto = ""
vencedor_vegetais_nota = -1

# Solicita o número de barracas
num_barracas = int(input("Informe o número de barracas na feira: "))

# Percorre cada barraca
for i in range(1, num_barracas + 1):
    print(f"\nAvaliação para a Barraca {i}:")
    
    # Avaliando o produto da categoria Frutas
    fruta_nome = input("Nome do produto de Frutas: ")
    while True:
        fruta_nota = float(input(f"Avalie o produto {fruta_nome} (0-10): "))
        if 0 <= fruta_nota <= 10:
            break
        else:
            print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
    
    if fruta_nota > vencedor_frutas_nota:
        vencedor_frutas_produto = fruta_nome
        vencedor_frutas_nota = fruta_nota
    
    # Avaliando o produto da categoria Vegetais
    vegetal_nome = input("Nome do produto de Vegetais: ")
    while True:
        vegetal_nota = float(input(f"Avalie o produto {vegetal_nome} (0-10): "))
        if 0 <= vegetal_nota <= 10:
            break
        else:
            print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
    
    if vegetal_nota > vencedor_vegetais_nota:
        vencedor_vegetais_produto = vegetal_nome
        vencedor_vegetais_nota = vegetal_nota

# Exibindo os vencedores
print("\nVencedores da Feira da Agricultura Familiar:")
print(f"Categoria Frutas: {vencedor_frutas_produto} com nota {vencedor_frutas_nota}")
print(f"Categoria Vegetais: {vencedor_vegetais_produto} com nota {vencedor_vegetais_nota}")
