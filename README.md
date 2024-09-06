# Sistema de Avaliação de Produtos

Este projeto é um sistema genérico de avaliação de produtos, projetado para ser flexível e utilizado em diferentes contextos, como competições, premiações de qualidade e avaliações de categorias específicas (como frutas, vegetais, entre outros).

## Funcionalidades

- Avaliação de produtos em diferentes categorias
- Coleta de notas de 0 a 10 para cada produto
- Determinação dos vencedores com base nas maiores notas por categoria
- Validação das notas inseridas para garantir que estejam no intervalo correto

## Como Usar

1. Informe o número total de participantes (ou categorias).
2. Para cada participante/categoria, insira o nome do produto e atribua uma nota de 0 a 10.
3. O sistema calculará e exibirá os produtos vencedores com as maiores notas em cada categoria.

## Exemplo de Uso

Utilizando uma premissa de que no Ceará, todo o ano tem a "Feira da Agricultura Familiar". Agricultores de toda a região competem para apresentar os melhores produtos. Você é um(a) jurado(a) da competição e precisa avaliar cada produto. 
Este programa permite ao usuário percorrer as barracas da Feira da Agricultura Familiar usando estrutura de repetição, para avaliar os produtos e escolher os vencedores.

```bash
Informe o número de participantes: 3

Avaliação para o Participante 1:
Nome do produto: Produto A
Avalie o produto Produto A (0-10): 8.5

Avaliação para o Participante 2:
Nome do produto: Produto B
Avalie o produto Produto B (0-10): 9.0

...

Vencedor:
Produto B com nota 9.0
