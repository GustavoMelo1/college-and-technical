# Trabalho de Algoritmos - Divisores de Numeros Inteiros

Este projeto foi desenvolvido para a disciplina de Algoritmos e foca em logica de programacao, manipulacao de arquivos e otimizacao de busca.

## Objetivo
O script recebe numeros inteiros maiores que 1 e identifica o primeiro par de divisores (a, b) tal que a * b = n. Caso o numero seja primo, o par retornado sera (1, n). Ao final da execucao, os resultados sao exportados para um arquivo .txt formatado como CSV.

## Estrutura do Projeto
O repositorio contem duas versoes da mesma logica, demonstrando diferentes abordagens de performance:

1. **app.py (Versao Otimizada):**
   - Utiliza a busca de divisores ate a raiz quadrada do numero (sqrt(n)).
   - Mais eficiente para numeros grandes, pois reduz drasticamente o numero de iteracoes necessarias.

2. **app2.py (Versao Didatica):**
   - Realiza a busca ate a metade do numero (n / 2).
   - Focado em clareza logica para fins academicos.

## Tecnologias e Conceitos
- Linguagem: Python 3
- Persistencia: Manipulacao de arquivos de texto (.txt / .csv)
- Tratamento de Erros: Blocos try/except para validar entradas do usuario.
- Otimizacao: Uso de logica matematica para reduzir complexidade de busca.

## Como executar
1. Execute o script: `python app.py`
2. Insira os numeros desejados conforme solicitado no terminal.
3. Digite -1 para encerrar e gerar o relatorio 'atividade-gustavomelooliveira.txt'.