# 1 - pessoa fisica 
# 2 - pessoa jurida
# 3 - sair

# 1 cadastrar pessoa fisica
# 2 - listar pessoa fisica
# 3 - sair

# 1 - cadastrar pessoa juridica
# 2 - listar pessoa juridica
# 3 - sair


from ast import And
from datetime import date, datetime
from os import remove
from Pessoa import Endereco, pessoafisica, pessoajuridica


def main():
    lista_pf = []
    lista_pj = []

    while True:
        opcao = int(input("escolha uma opcao: 1 - pessoa fisica / 2 - pessoa juridica / 0 - sair "))

        if opcao == 1:
            while True:
                opcao_pf = int(input("escolha uma opcao: 1 - cadastrar pessoa fisica / 2 - listar pessoa fisica / 3 - remover cpf / 4 - Atualizar lista / 0 - sair"))
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

                    #cadastro do endereco pessoa fisica
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

                #remover pessoa fisica
                elif opcao_pf == 3:
                    remover_cpf = input("digite o CPF a ser removido ")
                    
                    pessoa_encontrada = False

                    for cada_pf in lista_pf:
                        if cada_pf.cpf == remover_cpf:
                            lista_pf.remove(cada_pf)
                            pessoa_encontrada = True
                            print("pessoa fisica removida")

                            break
                    if not pessoa_encontrada:
                        print("Nenhuma pessoa encontrada")

                    #ATUALIZAR CADASTRO pessoa fisica
                elif opcao_pf == 4:
                    atualizar_pf = input("o que deseja atualizar: 1 - nome / 2 - endereco / 3 - rendimento / 4 - CPF / 5 - Data de Nascimento").strip().upper()
                                                                                                                                               #usado para aceitar tudo letra maiuscula e minuscula
                    if atualizar_pf == 1:
                        novo_nome = input(f"o nome atual e {novapf.nome}, digite o novo nome: ")
                        novapf.nome = novo_nome
                        print(f"o nome foi atualizado com sucesso: {novo_nome}")
                    
                    elif atualizar_pf == 2:
                        novo_endereco = input(f"o endereco atual {novapf.endereco}, digite seu novo endereco: ")
                        novapf.endereco = novo_endereco
                        print(f"endereco atualizado com sucesso: {novo_endereco}")
                    
                    elif atualizar_pf == 3:
                        novo_rendimento = input(f"o rendimento atual e {novapf.rendimento}, digite seu novo rendimento para ser atualizado: ")
                        novapf.rendimento = novo_rendimento
                        print(f"o rendimento foi atualizado com sucesso: {novo_rendimento}")
                    
                    elif atualizar_pf == 4:
                        novo_cpf = input(f"o CPF atual e {novapf.cpf}, digite o seu novo CPF para atualizacao: ")
                        novapf.cpf = novo_cpf
                        print(f"o cpf foi atualizado com sucesso: {novo_cpf}")
                    
                    elif atualizar_pf == 5:
                        novo_datanascimento = input("digite sua nova data de nascimento: ")
                        novapf.dataNascimento = novo_datanascimento
                        print(f"data de nascimento atualizada com sucesso: {novo_datanascimento}")
                    else:
                        print("opcao invalida")
                        break
                if not pessoa_encontrada:
                    print("nenhuma pessoa encontrada com esse CPF!! ")

                #sair do menu atual
                elif opcao_pf == 0:
                    print("voltando ao menu anterior")
                
                    break
                else:
                    print("opcao invalida, por favor digite uma das opcoes indicadas: ")

        elif opcao == 2:

             #OPCAO PESSOA JURIDICA
            if opcao == 2:
                while True:
                    opcao_juridica = int(input("escolha uma opcao: 1 - cadastrar pessoa juridica / 2 - listar pessoa juridica / 3 - remover cnpj / 4 - atualizar lista"))
                    #cadastrar pessoa juridica
                    if opcao_juridica == 1:
                      novapj = pessoajuridica()
                      nova_end_pj = Endereco()
                    

                      novapj.nome = input("digite seu nome ")
                      novapj.cnpj = input("digite o seu cnpj ")
                      novapj.rendimento = float(input("digite o seu rendimento mensal: "))

                     #cadastro do endereco da empresa
                      nova_end_pj.endereco_comercial = input("digite seu endereco")
                      nova_end_pj.numero = input("qual o numero: ")
                      nova_end_pj.nomefantasia = input("digite o nome fantasia: ")
                      end_comercial = input("esse endereco e comercial? S/N")
                      nova_end_pj.endreco_comercial = end_comercial.strip.upper() == "S"
 
                      novapj.endereco = nova_end_pj

                      lista_pj.append(novapj)

                      print("cadastro realizado com sucesso !!")

                    #listar pessoa juridica
                    elif opcao == 2:
                      if lista_pj:
                        for cada_pj in lista_pj:
                         print(f"nome da pessoa juridica: {cada_pj.nome}")
                         print(f"CNPJ: {cada_pj.cnpj}")
                         print(f"endereco: {cada_pj.endereco}")
                         print(f"calcular imposto: {cada_pj.calcular_imposto(cada_pj.rendimento)}")

                         print("digite 0 para sair")
                         input()
                      else:
                        print("lista vazia")

                    #remover Cnpj:
            elif opcao == 3:
                remover_cnpj = input("digite o cnpj da empresa que deseja excluir: ")

                pessoa_encontrada = False

                for cada_pj in lista_pj:
                    if cada_pj.cnpj == remover_cnpj:
                        lista_pj.remove(remover_cnpj)
                        print(f"cnpj foi removido {remover_cnpj}")
                        empresa_encontrada = True
                        break

                if not empresa_encontrada:
                    print("nenhum cnpj encontrado")
            #ATUALIZAR PESSOA JURIDICA
            elif opcao == 4:
                nova_pej = input("o que deseja atualizar: 1 ")

            elif opcao == 0:
                print("voltando ao menu anterior")
                
                break
            else:
                print("opcao invalida, por favor digite uma das opcoes indicadas: ")

        elif opcao == 0:
            print("obrigado por utilizar nosso sistema! valeu! ")
            break
        else:
            print("opcao invalida, por favor digite uma das opcoes validas! ")

if __name__ == "__main__":
    main() #chama a funcao principal 
    
