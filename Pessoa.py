# classe endereco

from datetime import date

class Endereco:
    def __init__(self, logradouro="", numero="", endereco_comercial=False):
   #inicializar os nossos atributos com os valores padrao
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_comercial = endereco_comercial
  
# classe pessoa
class pessoa:
   def __init__(self, nome="", rendimento=0.0, endereco=None):
    self.nome = nome
    self.rendimento = rendimento
    self.endereco = endereco
  
def calcular_imposto(self, rendimento):
    return rendimento
  
      
# classe pessoa fisica
class pessoafisica(pessoa):
  #inicializar os atributos que foram herdados e proprios atributos da classe
    def __init__(self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=None):
        if endereco is None:
            #se nenhum endereco for fornecido cria um objeto endereco padrao
            endereco = Endereco()
        if dataNascimento is None:
            dataNascimento = date.today()
        super().__init__(nome, rendimento, endereco)
        
        #atributos da propria classe
        self.cpf = cpf
        self.dataNascimento = dataNascimento
    
  
def calcular_imposto(self, rendimento: float) -> float:
#sem imposto para rendimento ate 1500
    if rendimento <= 1500:
        return 0

    elif 1500 < rendimento <= 3500:
        #return (redimento / 100)* 2
        #2% de imposto para rendimento entre 1500 e 3500
        return rendimento * 0.2

    elif 3500 < rendimento <= 6000:
        return (rendimento / 100) * 3.5
       #3% de imposto para rendimento entre 3500 e 6000
    else:
        return (rendimento / 100)* 5
       #5% de imposto para rendimento acima 6000

# classe pessoa juridica
class pessoajuridica(pessoa):
    def __init__(self,nome="", cnpj="", rendimento=0.0, nomefantasia="",endereco=None):

      if endereco is None:
        endereco = Endereco()
        self.nomefantasia = nomefantasia
        self.cnpj = cnpj
        self.redimento = rendimento

      super().__init__(nome, rendimento)
    
def calcular_imposto(self, rendimento: float) -> float:
#sem imposto para rendimento ate 1500
    if rendimento <= 10500:
        return 0

    elif 1500 < rendimento <= 30500:
        #return (redimento / 100)* 2
        #2% de imposto para rendimento entre 1500 e 3500
        return rendimento * 5

    elif 3500 < rendimento <= 60000:
        return (rendimento / 100) * 8
       #3% de imposto para rendimento entre 3500 e 6000
    else:
        return (rendimento / 100)* 12
       #5% de imposto para rendimento acima 6000