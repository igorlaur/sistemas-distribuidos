# -*- coding: utf-8 -*-
import json
'''
Nessa atividade, vamos usar dados do campeonato brasileiro 2018
(brasileirao) para estudar como acessar listas, dicionarios,
e estruturas encadeadas (listas dentro de dicionários dentro de listas)

Os dados estão fornecidos em um arquivo (ano2018.json) que você 
pode abrir no firefox, para tentar entender melhor

Se quiser ver os dados dentro do python, pode chamar a funcao
pega_dados


'''

'''
Crie uma funcao datas_de_jogo, que procura nos dados do brasileirao 
e devolve uma lista de todas as datas em que houve jogo.

As datas devem ter o mesmo formato que tinham nos dados do brasileirao

dica: busque em dados['fases']

Observe que essa funcao (e todas as demais!) recebem os dados dos
jogos numa variavel dados. Essa variavel 
contem todas as informacoes do arquivo
json que acompanha essa atividade 
'''
def datas_de_jogo(dados):
    return dados['fases']['2700']['jogos']['data'].keys()

'''
Crie uma funcao data_de_um_jogo, que recebe a id numérica de um jogo
e devolve a data em que ele ocorreu. 

Se essa nao é uma id valida, voce deve devolver a string 'nao encontrado'.
Cuidado! Se você devolver uma string ligeiramente diferente, o teste
vai falhar

(você provavelmente vai querer testar sua funcao no braço e nao
somente fazer os meus testes. Para isso, note que muitos numeros
nesse arquivo estao representados nao como números, mas como strings)
'''
def data_de_um_jogo(dados,id_jogo):
    x = dados['fases']['2700']['jogos']['id']
    if id_jogo not in x:
        return 'nao encontrado'
    return x[id_jogo]['data']

'''
Nos nossos dados, cada time tem um id, uma identificacao numerica.
(voce pode consultar as identificacoes numericas em dados['equipes'])

Essas id também aparecem nos jogos (onde? dê uma procurada!)

A proxima função recebe a id numerica de um jogo, e devolve as
ids numéricas dos dois times envolvidos

vou deixar um codigo pra vc lembrar como retornar duas ids em
um unico return

def ids_dos_times_de_um_jogo(dados,id_jogo):
    time1 = 12
    time2 = 13
    return time1,time2 #assim a gente retorna as duas respostas em um unico return
'''
def ids_dos_times_de_um_jogo(dados,id_jogo):
    x = dados['fases']['2700']['jogos']['id']
    if id_jogo not in x:
        return 'nao encontrado'
    return x[id_jogo]['time1'],x[id_jogo]['time2']

'''
A proxima funcao recebe a id_numerica de um time e deve retornar 
seu 'nome-comum'
'''

def nome_do_time(dados,id_time):

    x = dados['equipes']
    if id_time not in x:
        return 'nao encontrado'
    return x[id_time]['nome-comum']

'''
A proxima funcao "cruza" as duas anteriores. Recebe uma id de um jogo
e retorna os "nome-comum" dos dois times
'''
def nomes_dos_times_de_um_jogo(dados,id_jogo):
    a,b = ids_dos_times_de_um_jogo(dados, id_jogo)
    x = nome_do_time(dados, a)
    y = nome_do_time(dados, b)
    return y, x

'''
Façamos agora a busca "ao contrário". Conhecendo
o nome-comum de um time, queremos saber sua id.

Se o nome comum nao existir, retorne 'nao encontrado'
'''
def id_do_time(dados,nome_time):
    x = dados['equipes']    
    for eq in x:
        if nome_time == x[eq]['nome-comum']:
            return eq
    return 'nao encontrado'


'''
Agora, façamos uma busca "fuzzy". Queremos procurar por 'Fla'
e achar o flamengo. Ou por 'Paulo' e achar o são paulo.

Nessa busca, você recebe um nome, e verifica os campos
        'nome-comum', 'nome-slug', 'sigla' e 'nome',
        tomando o cuidado de aceitar times se a string
        buscada aparece dentro do nome (A string "Paulo"
        aparece dentro de 'Sao Paulo')

Sua resposta deve ser uma lista de ids de times que "batem"
com a pesquisa (e pode ser vazia, se não achar ninguém)
'''

def busca_imprecisa_por_nome_de_time(dados,nome_time):
    lista = []
    x = dados['equipes']    
    for eq in x:
        if nome_time in x[eq]['nome-comum']:
            lista.append(eq)
        elif nome_time in x[eq]['nome-slug']:
            lista.append(eq)
        elif nome_time in x[eq]['nome']:
            lista.append(eq)
        elif nome_time in x[eq]['sigla']:
            lista.append(eq)     
    return lista

#ids dos jogos de um time

'''
Agora, a idéia é receber a id de um time
e retornar as ids de todos os jogos em que ele participou
'''
def ids_de_jogos_de_um_time(dados,time_id):
    lista = []
    x = dados['fases']['2700']['jogos']['id']
    for eq in x:
        if time_id in [x[eq]['time1'], x[eq]['time2']]:
            lista.append(eq)
    return lista

'''
Usando as ids dos jogos em que um time participou, podemos descobrir
em que dias ele jogou.

Note que essa função recebe o nome-comum do time, nao sua id.

Ela retorna uma lista das datas em que o time jogou
'''
def datas_de_jogos_de_um_time(dados,nome_time):
    id_time = id_do_time(dados,nome_time)
    if id_time == 'nao encontrado':
        return 'nao encontrado'
    ids = ids_de_jogos_de_um_time(dados, id_time)
    lista = []
    x = dados['fases']['2700']['jogos']['id']
    for id in ids:
        lista.append(x[id]['data'])
    return lista



'''
A proxima funcao recebe apenas o dicionario dos dados do brasileirao

Ela devolve um dicionário, com quantos gols cada time fez
'''

def dicionario_de_gols(dados):
    pass

'''
A proxima funcao recebe apenas o dicionario dos dados do brasileirao

Ela devolve a id do time que fez mais gols no campeonato
'''
def time_que_fez_mais_gols(dados):
    pass


'''
A proxima funcao recebe apenas o dicionario dos dados do brasileirao

ela devolve um dicionário. Esse dicionário conta, para cada estádio,
quantas vezes ocorreu um jogo nele.

Ou seja, as chaves sao ids de estádios e os valores associados,
o número de vezes que um jogo ocorreu no estádio
'''
def dicionario_id_estadio_e_nro_jogos(dados):
    pass

'''
A proxima funcao recebe apenas o dicionario dos dados do brasileirao

Ela retorna o nro de times que o brasileirao qualifica para a libertadores

Note. Esse numero está nos dados que eu forneci. Voce deve pegar dos
dados. Nao basta retornar o valor correto, tem que acessar os dados
fornecidos.
'''
#devolve quantos times sao classificados para a libertadores (consultando dicionario
#de faixas)
def qtos_libertadores(dados):
    pass

'''
A proxima funcao recebe um tamanho, e retorna uma lista
com len(lista)=tamanho, com as ids dos times melhor classificados
'''
def ids_dos_melhor_classificados(dados,numero):
    pass

'''
A proxima funcao usa as duas anteriores para retornar uma 
lista de todos os times classificados para a libertadores em
virtude do campeonato brasileiro

Lembre-se de consultar a estrutura, tanto para obter a classificacao, quanto
para obter o nro correto de times a retornar

A funcao so recebe os dados do brasileirao

'''
def classificados_libertadores(dados):
    pass

'''
Da mesma forma que podemos obter a informacao dos times classificados
para a libertadores, também podemos obter os times na zona de rebaixamento

A proxima funcao recebe apenas o dicionário de dados do brasileirao,
e retorna uma lista com as ids dos times rebaixados.

Consulte a zona de rebaixamento do dicionário de dados, nao deixe
ela chumbada da função
'''
def rebaixados(dados):
    pass

'''
A proxima função recebe (alem do dicionario de dados do brasileirao) uma id de time

Ela retorna a classificacao desse time no campeonato.

Se a id nao for valida, ela retorna a string 'nao encontrado'
'''
def classificacao_do_time_por_id(dados,time_id):
    pass


import unittest

class TestClientes(unittest.TestCase):
    def test_01_datas_de_jogo(self):
        dados = pega_dados()
        datas = datas_de_jogo(dados)
        self.assertEqual(len(datas), 107)
        self.assertTrue('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)

    def test_02_datas_de_jogo(self):
        dados = pega_dados()
        del dados['fases']['2700']['jogos']['data']['2018-04-14']
        datas = datas_de_jogo(dados)
        self.assertEqual(len(datas), 106)
        self.assertFalse('2018-04-14' in datas)
        self.assertTrue('2018-07-26' in datas)
        self.assertTrue('2018-10-26' in datas)

    def test_03_data_de_um_jogo(self):
        dados = pega_dados()
        self.assertEqual(data_de_um_jogo(dados,'102132'),'2018-05-06')
        self.assertEqual(data_de_um_jogo(dados,'102187'),'2018-06-06')
        self.assertEqual(data_de_um_jogo(dados,'102540'),'nao encontrado')

    def test_04_ids_dos_times_de_um_jogo(self):
        dados = pega_dados()
        t1,t2 = ids_dos_times_de_um_jogo(dados,'102099')
        self.assertTrue(t1 in ['5','17'])
        self.assertTrue(t2 in ['5','17'])
        t1,t2 = ids_dos_times_de_um_jogo(dados,'102109')
        self.assertTrue(t1 in ['1','26'])
        self.assertTrue(t2 in ['1','26'])
    
    def test_05_nome_do_time(self):
        dados = pega_dados()
        self.assertEqual(nome_do_time(dados,'1'),'Flamengo')
        self.assertEqual(nome_do_time(dados,'695'),'Chapecoense')
    
    def test_06_nomes_dos_times_de_um_jogo(self):
        dados = pega_dados()
        t1,t2 = nomes_dos_times_de_um_jogo(dados,'102099')
        self.assertTrue(t1 in ['Botafogo','Palmeiras'])
        self.assertTrue(t2 in ['Botafogo','Palmeiras'])
        t1,t2 = nomes_dos_times_de_um_jogo(dados,'102109')
        self.assertTrue(t1 in ['Flamengo','América-MG'])
        self.assertTrue(t2 in ['Flamengo','América-MG'])

    def test_07_id_do_time(self):
        dados = pega_dados()
        self.assertEqual(id_do_time(dados,'Cruzeiro'),'9')
        self.assertEqual(id_do_time(dados,'Athletico'),'3')

    def test_08_busca_imprecisa_por_nome_de_time(self):
        dados = pega_dados()
        ids_times = busca_imprecisa_por_nome_de_time(dados,'Paulo')
        self.assertTrue('24' in ids_times)
        ids_times = busca_imprecisa_por_nome_de_time(dados,'SPA')
        self.assertTrue('24' in ids_times)
        ids_times = busca_imprecisa_por_nome_de_time(dados,'anto')
        self.assertTrue('22' in ids_times)
    
    def test_09_ids_de_jogos_de_um_time(self):
        dados = pega_dados()
        jogos_chapeco = ids_de_jogos_de_um_time(dados,'695')
        self.assertEqual(len(jogos_chapeco),38)
        self.assertTrue('102330' in jogos_chapeco)
        self.assertTrue('102422' in jogos_chapeco)
        jogos_santos = ids_de_jogos_de_um_time(dados,'22')
        self.assertEqual(len(jogos_santos),38)
        self.assertTrue('102208' in jogos_santos)
        self.assertTrue('102259' in jogos_santos)
    
    def test_10_datas_de_jogos_de_um_time(self):
        dados = pega_dados()
        datas_santos = datas_de_jogos_de_um_time(dados,'Santos')
        self.assertEqual(len(datas_santos),38)
        self.assertTrue('2018-04-21' in datas_santos)
        self.assertTrue('2018-10-13' in datas_santos)
        datas_chapeco = datas_de_jogos_de_um_time(dados,'Chapecoense')
        self.assertEqual(len(datas_chapeco),38)
        self.assertTrue('2018-11-25' in datas_chapeco)
        self.assertTrue('2018-12-02' in datas_chapeco)
    
    def test_11_dicionario_de_gols(self):
        dados = pega_dados()
        dic_gols = dicionario_de_gols(dados)

        self.assertEqual(dic_gols['695'],34)
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102330']['placar2']=1
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'],35)
        dados['fases']['2700']['jogos']['id']['102422']['placar2']=2
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'],36)
        dados['fases']['2700']['jogos']['id']['102422']['placar2']=12
        dic_gols = dicionario_de_gols(dados)
        self.assertEqual(dic_gols['695'],46)
    
    def test_12_time_que_fez_mais_gols(self):
        dados = pega_dados()
        time = time_que_fez_mais_gols(dados)
        self.assertEqual(time,'17')
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102422']['placar2']=120
        time = time_que_fez_mais_gols(dados)
        self.assertEqual(time,'695')

    def test_13_dicionario_id_estadio_e_nro_jogos(self):
        dados = pega_dados()
        estadios = dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'],16)
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['jogos']['id']['102097']['estadio_id']='72'
        estadios = dicionario_id_estadio_e_nro_jogos(dados)
        self.assertEqual(estadios['72'],17)

    def test_14_qtos_libertadores(self):
        dados = pega_dados()
        self.assertEqual(qtos_libertadores(dados),6)
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']='1-8'
        self.assertEqual(qtos_libertadores(dados),8)


    def test_15_ids_dos_melhor_classificados(self):
        dados = pega_dados()
        self.assertEqual(ids_dos_melhor_classificados(dados,10),["17","1","15","13","24","4","3","9","5","22"])
        self.assertEqual(ids_dos_melhor_classificados(dados,5),["17","1","15","13","24"])
        self.assertEqual(ids_dos_melhor_classificados(dados,3),["17","1","15"])

    def test_16_classificados_libertadores(self):
        dados = pega_dados()
        self.assertEqual(classificados_libertadores(dados),["17","1","15","13","24","4"])
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica1']['faixa']='1-8'
        self.assertEqual(classificados_libertadores(dados),["17","1","15","13","24","4","3","9"])
    
    def test_17_rebaixados(self):
        dados = pega_dados()
        self.assertEqual(rebaixados(dados),['76', '26', '21', '18'])
        #vou falsificar os dados pra testar se vc esta lendo direito da estrutura
        dados['fases']['2700']['faixas-classificacao']['classifica3']['faixa']='15-20'
        self.assertEqual(rebaixados(dados),['33','25','76', '26', '21', '18'])

    def test_18_classificacao_do_time_por_id(self):
        dados = pega_dados()
        self.assertEqual(classificacao_do_time_por_id(dados,'17'),1)
        self.assertEqual(classificacao_do_time_por_id(dados,'30'),11)
        self.assertEqual(classificacao_do_time_por_id(dados,'695'),14)
        self.assertEqual(classificacao_do_time_por_id(dados,'1313'),'nao encontrado')



def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestClientes)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

def pega_dados():
    with open('ano2018.json') as f:
        dados = json.load(f)
    return dados

dados2018 = pega_dados()

if __name__ == '__main__':
    runTests()
