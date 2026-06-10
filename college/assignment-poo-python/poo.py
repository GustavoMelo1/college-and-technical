class Veiculo:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
        self.__combustivel = 100

    def exibir_status(self):
        print(f"Veículo: {self.modelo} | Marca: {self.marca} | Combustível: {self.__combustivel}%")

    def viagem(self, distancia):
        custo = distancia / 10
        if self.__combustivel >= custo:
            self.__combustivel -= custo
            print(f"Viagem realizada. Combustível restante: {self.__combustivel}%")
        else:
            print("Combustível insuficiente para a viagem.")

    def abastecer(self, quantidade):
        if quantidade > 0:
            self.__combustivel += quantidade
            if self.__combustivel > 100:
                self.__combustivel = 100
            print(f"Veículo abastecido. Combustível atual: {self.__combustivel}%")
        else:
            print("Quantidade inválida.")

carro1 = Veiculo("Sedan", "Toyota")
caminhao1 = Veiculo("FH 540", "Volvo")

while True:
    print("\n1-Status | 2-Viajar | 3-Abastecer | 4-Sair")
    opcao = input("Escolha: ")

    if opcao == '1':
        carro1.exibir_status()
        caminhao1.exibir_status()

    elif opcao == '2':
        d = float(input("Distância: "))
        carro1.viagem(d)
        caminhao1.viagem(d)

    elif opcao == '3':
        q = float(input("Quantidade para abastecer (%): "))
        carro1.abastecer(q)
        caminhao1.abastecer(q)

    elif opcao == '4':
        break

    else:
        print("Opção inválida.")