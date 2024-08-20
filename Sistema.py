# 1 - pessoa fisica 
# 2 - pessoa jurida
# 3 - sair

# 1 cadastrar pessoa fisica
# 2 - listar pessoa fisica
# 3 - sair

# 1 - cadastrar pessoa juridica
# 2 - listar pessoa juridica
# 3 - sair


from datetime import date, datetime
from Pessoa import Endereco, pessoafisica


def main():
    lista_pf = []
    while True:
        opcao = int(input("escolha uma opcao: 1 - pessoa fisica / 2 - pessoa juridica / 0 - sair "))

        if opcao == 1:
            while True:
                opcao_pf = int(input("escolha uma opcao: 1 - cadastrar pessoa fisica / 2 - listar pessoa fisica / 3 - voltar ao menu anterior"))
                # 1 cadastrar uma pessoa fisica
                if opcao_pf == 1:
                    novapf = pessoafisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("digite o nome da pessoa fisica")
                    novapf.cpf = input("digite o cpf")
                    novapf.rendimento = float(input("digite o rendimento mensal (digite somente numero):"))
                    
                    data_nascimento = input("digite a data de nascimento (dd/mm/aaaa): ") # solicita a data de nascimento
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365 #calcula a idade da pessoa
                    
                    if idade >= 18:
                        print("a pessoa tem mais de 18 anos")
                    else:
                        print("a pessoa tem menos de 18 anos. Retorne ao menu")
                        continue # retorna ao inicio do loop

                    #cadastro do endereco
                    novo_end_pf.logradouro = input("digite o logradouro: ")
                    novo_end_pf.numero = input("digite um numero: ")
                    end_comercial = input("este endereco e comercial: S/N")
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == "S"

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("cadastro realizado com sucesso!! ")
                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"nome: {cada_pf.nome}")
                            print(f"CPF:{cada_pf.cpf}")
                            print(f"endereco: {cada_pf.endereco}")
                            print(f"Data de nascimento: {cada_pf.data_nascimento.strftime("%d/%m/%y")}")
                            print(f"imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("digite 0 para sair")
                            input()
                    else:
                        print("lista vazia")
                #sair do menu atual
                elif opcao_pf == 0:
                    print("voltando ao menu anterior")
                    break
                else:
                    print("opcao invalida, por favor digite uma das opcoes indicadas: ")

        elif opcao == 2:
            print("funcionalidade para pessoas juridicas nao implementadas")
            pass
        elif opcao == 0:
            print("obrigado por utilizar nosso sistema! valeu! ")
            break
        else:
            print("opcao invalida, por favor digite uma das opcoes validas! ")

if __name__ == "__main__":
    main() #chama a funcao principal 
    
