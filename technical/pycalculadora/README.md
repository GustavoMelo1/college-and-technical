# Calculadora Simples em Python

Este projeto consiste em uma calculadora basica desenvolvida para praticar conceitos fundamentais de logica de programacao e estruturas de controle em Python.

## Objetivo
O script permite que o usuario realize operacoes matematicas basicas entre dois valores numericos de forma continua ate que a execucao seja interrompida manualmente.

## Operacoes Disponiveis
O sistema oferece quatro opcoes de calculo:
1. Soma
2. Divisao (com verificacao para evitar divisao por zero)
3. Multiplicacao
4. Subtracao

## Detalhes Tecnicos
- Estrutura de Repeticao: Utiliza um laco `while True` para permitir multiplos calculos em uma mesma sessao.
- Tratamento de Dados: Implementa uma verificacao de seguranca na operacao de divisao para evitar erros de execucao caso o segundo valor seja zero.
- Interatividade: Recebe entradas do usuario via terminal para definicao dos valores e escolha da operacao.

## Como executar
1. Execute o script: `python pycalculadora.py`
2. Digite o primeiro e o segundo valor conforme solicitado.
3. Escolha o numero correspondente a operacao desejada (1, 2, 3 ou 4).
4. O resultado sera exibido diretamente no terminal.