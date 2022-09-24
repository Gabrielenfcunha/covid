d_covid = {}
### gggggg
class Estado:
  def __init__(self , nome_estado, sigla_estado):
    self.nome_estado = nome_estado
    self.sigla_estado = sigla_estado
    self.cidade = []

#jhygh
################################################### 
def add_nome_estado_est():
  nome_estado = input("Nome do Estado: ").upper()
  sigla_estado = input("Digite a sigla do Estado: ").upper()
  estado = Estado(nome_estado, sigla_estado)
  if nome_estado not in d_covid:
    d_covid[estado.nome_estado] = estado
  # d_codiv[estado].append(estado)
################################################### 
class Cidade:
  def __init__(self, nome_cidade, qt_casos_cidade):
    self.nome_cidade = nome_cidade
    self.qt_casos_cidade = qt_casos_cidade
###################################################
def add_nome_cidade():
  try:
    nome_estado = input("Digite estado: ").upper()
    nome_cidade = input("Digite Nome da cidade: ").upper()
    qt_casos_cidade = int(input("Digite Quantos casos tem essa cidade: "))
    cidade = Cidade(nome_cidade,qt_casos_cidade)
    if nome_estado not in d_covid:
      print("Primeiro cadastre o estado...")
      pass
    # d_codid[nome_estado].cidade.append(cidade)
    if nome_cidade not in d_covid[nome_estado].cidade:
      d_covid[nome_estado].cidade.append(cidade)
    # d_codid[nome_estado].append(cidade)
  except:
      return
###################################################
def Relatório_de_esdado():
  # para cada estado (ex: rs, sc...)
  for uf in d_covid.keys():
      # uf agora é a string com a sigla do estado
      objestado = d_covid[uf]
      # objestado é a instancia de estado
      contador = 0
      for c in objestado.cidade:
        # c é uma cidade do estado
        contador = contador + int(c.qt_casos_cidade) 
      print(f'--->{uf}....-Total de casos:{contador} ')
###################################################
def Relatório_de_Cidades():
  for ci in d_covid.keys():
    objEstado = d_covid[ci]
    # objcidade = d_covid[ci]
    for city in objEstado.cidade:
      print(f'Cidade: {city.nome_cidade}.....-Casos Registrados: {city.qt_casos_cidade}')
###################################################
def alterar_dado():
  try:
    nome_estado = input("Digite o estado: ").upper()
    nome_cidade = input("Digite a cidade: ").upper()
    caso_alterar = input("Qual a quantidade de casos: ")
    for umaCidade in d_covid[nome_estado].cidade:
      if umaCidade.nome_cidade == nome_cidade:
        umaCidade.qt_casos_cidade = caso_alterar
  except:
    print("Nome não localizado. ")
###################################################
def executar_menu():
    menu_principal ="""
            Menu
          0- Finalizar o Programa
          1- Cadastrar Estados
          2- Cadastrar Cidades
          3- Relatório de Estados
          4- Relatório de Cidades
          5- Atualizar números de casos Escolha: """

    while True:
        escolha = input(menu_principal)
        if escolha == '0': break
        if escolha == '1': add_nome_estado_est()
        if escolha == '2': add_nome_cidade()
        if escolha == '3': Relatório_de_esdado()
        if escolha == '4': Relatório_de_Cidades()
        if escolha == '5': alterar_dado()
        print('=-'*30)
#### Programa Principal
executar_menu()