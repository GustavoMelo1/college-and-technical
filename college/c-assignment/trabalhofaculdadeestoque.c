#include <stdio.h>
#include <stdlib.h>

// Definição da estrutura conforme solicitado na tarefa
typedef struct {
    char nome[50];
    int codigo;
    float preco;
} Produto;


// Função que utiliza ponteiros para aplicar desconto (Passagem por Referência)
// O uso do operador '->' é essencial para acessar membros via ponteiro
void aplicarDesconto(Produto *p, float percentual) {
p->preco = p->preco - (p->preco * percentual / 100);
printf("\nDesconto de %.2f%% aplicado com sucesso!", percentual);
 }


int main() {
Produto prod; // Declaração da variável do tipo Produto
float desc;
printf("--- Cadastro de Produto ---\n");
printf("Nome do produto: ");
scanf(" %49[^\n]", prod.nome); // Leitura de string com espaços
printf("Código: ");
scanf("%d", &prod.codigo);
printf("Preço original: R$ ");
scanf("%f", &prod.preco);


// Solicita o percentual de desconto
printf("\nDigite o percentual de desconto: ");
scanf("%f", &desc);


// Chamada da função passando o endereço de memória da struct
aplicarDesconto(&prod, desc);

// Exibição dos dados atualizados [cite: 414, 467]
printf("\n\n--- Dados Atualizados ---");
printf("\nNome: %s", prod.nome);
printf("\nCódigo: %d", prod.codigo);
printf("\nNovo Preço: R$ %.2f\n", prod.preco);
return 0;
}