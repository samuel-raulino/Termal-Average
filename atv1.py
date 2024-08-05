
import random,os,__random,SimpleFile as SF#importa os outros arquivos
from temps_calc import * # importa o temps_cal, arquivo criado para ajudar nos calculos
def create_doubleList(a,b):##cria uma função para declarar matrizes
    matriz = {}
    for x in range(a):
        matriz[x] = []
        for xx in range(b):
            matriz[x].append(xx)
    return matriz

def create_list(a):#cria uma função para simular os vetores do portugol
    vetor = []
    for x in range(a):
        vetor.append(x)
    return vetor
#declaração de variaveis,vetores e matrizes
conta = "an"

horas = 24 
dia = 8
mes = 12

mediadia = create_doubleList(dia,horas)

mediasmes = create_doubleList(mes,dia)
mediames = create_list(mes)
maior = 0
menor = 0
datad = 0
datam = 0
enter = ""

"""
def print_an(a):
    if conta == "an":
        print(a)
def print_log(a):
    if conta == "log":
        print(a)
def enter_an():
    if conta == "an":
        input()
def enter_log():
    if conta == "log":
        input()
def input_prem():
    if conta == "prem":
        return input()
def print_prem(a):
    if conta == "prem":
        print(a)
def enter_prem():
    if conta == "prem":
        input()
def input_log():
    if conta == "log":
        return input()
"""
def login():#faz o codigo do login
    os.system("cls")
    a = True 
    while(a):
        print("---Login---")
        email = input("Digite seu email: ")#pergunta email e senha
        senha = input("Digite sua senha: ")#pergunta a senha

        contas = SF.File("contas")
        contas.create()# faz a verificação do arquivo "contas.txt" 
        #obs: se ele for apagado, essa função faz ele ser criado novamente
        for x in range(len(contas.all_lines())):#verifica linha por linha do arquivo txt
            email_reg = contas.read_line(x)#amrazena cada linha numa variavel
            senha_reg = contas.read_line(x+1)#armazena a linha seguinte em outra variavel
            if email_reg.strip() == email.strip():#verifica se a linha verificada é igual ao email logado
                if senha_reg.strip() == senha.strip():
                    print("login feito com sucesso") 
                    conta = "log"
                    a = False
                
    
def registrar():#função que faz o registro de contas
    contas = SF.File("contas")
    contas.create()#encontra o arquivo
    os.system("cls") # apaga a tela
    print("---registro---")#exibe tela de registro
    prob = True
    premium = False
    while(prob):
        print("digite seu email: ")#pergunta email e armazena numa variavel
        email = input()
        print("digite sua senha: ")#pergunta senha e armazenha numa variavel
        senha = input()
        
        for x in range(len(contas.all_lines())):#verifica linha por linha do arquivo txt de contas
            a = contas.read_line(x)#armazena a linha do texto em uma variavel
            if a.strip() == email.strip():#se a linha for igual ao email
                print("conta já registrada") #a conta já foi registrada
        prob = False
    print("deseja virar premium? ")#pergunta ao usuario
    enter = input()

    if enter == "sim":
        cpf = input("Digite seu cpf:")# se a resposta por sim ele armazena o cpf da pessoa numa variavel
        conta_corrente = input("Digite sua conta corrente:")# e também a sua conta corrente
        premium = True
    else:
        cpf = ""
        conta_corrente = ""
    contas.append("-"*10)#adiciona uma separação no arquivo txt
    contas.append(email)#adiciona o email da pessoa
    contas.append(senha)#adiciona sua senha
    contas.append("cpf: "+ cpf)#adiciona seu cpf
    contas.append("conta corrente: "+conta_corrente)# adiciona sua conta corrente
    
            


os.system("cls")
print("Bem vindo ao Thermal Average!\n\n")
print("O Thermal Average é um programa que registra as temperaturas diárias de paises europeus\n ao longo dos meses.\n")
print("Você tem uma conta? ")#pergunta ao usuario se ele tem conta
enter = input()
if enter == "sim":# se sim ele vai para a tela de login
    login()
elif enter == "não":# se não é perguntado se ele quer ser registrado
    print("deseja registrar? ")
    enter = input()
    if enter == "sim": 
        registrar()#ele vai pra tela de registro
        login()#e depois para a tela de login


print("\n\nAperte enter para começar ")
enter = input()
os.system("cls")
    
for i in range(dia):#zera as variaveis para evitar bugs
    mediames[i] = 0

for i in range(mes):
    for ii in range(dia):
        mediasmes[i][ii] = 0
      


pais = input("Qual o pais (Europeu) que você deseja escolher?")
#pergunta ao usuario qual pais europeu ele quer escolher
enter = input()
os.system("cls")
def mediadiaria(mininverno,maxinverno,minverao,maxverao,inverno,primavera,outono,verao):
    #cria uma função que faz a media de temperatura do pais escolhido
    r = __random.CustomRandom()
    for i in range(dia):#faz o calculo de 1 dia do ano
        for ii in range(horas):
            if m+1 in inverno:
                mediadia[i][ii] = r.randint(mininverno,maxinverno)
            elif m+1 in outono:
                mediadia[i][ii] = r.randint(minverao-10,maxverao-10)
            elif m+1 in primavera:
                mediadia[i][ii] = r.randint(mininverno+5,maxinverno+5)
            elif m+1 in verao:
                mediadia[i][ii] = r.randint(minverao,maxverao)
for m in range(mes):
    _pais = Avarage(pais)#Importa uma classe do arquivo temps_calc 
    #que verifica em um arquivo txt em que armazena todos as temperaturas de todos os paises
    #e verifica se o pais escolhido pelo usuario está nesse arquivo txt
    #se estiver, ele pega sua temperatura maior e menor
    #que é armazenado nas variaveis:
    #_pais.mininv - minimo no inverno, _pais.maxinv - maxima no inverno
    #_pais.minverao - minimo no verão _pais.maxverao - maximo no verão

    _pais.make_avarage()
    mediadiaria(_pais.mininv,_pais.maxinv,_pais.minverao,_pais.maxverao,[12,1,2],[3,4,5],[9,10,11],[6,7,8])
    #executa a função anterior em todos os dias do ano
    #todas as medias de todos os meses
    print(" Mês "+str(m+1)+":\n")#imprime na tela o mes
    for i in range(dia):
        for ii in range(horas):
            mediasmes[m][i]+= mediadia[i][ii]
        mediasmes[m][i]/= horas 
        print(" Dia "+str(i+1)+": "+str(int(mediasmes[m][i]))+"°C \n")
        #imprime na tela o dia e sua temperatura
      


print("(Aperte enter para continuar) ")
enter = input()
os.system("cls")
print(" Temperatura média de todos os meses: ")

    #separação
for i in range(mes):#faz a verificação de cada mes
    mediames[i] = 0
    for ii in range(dia):
        mediames[i] += mediasmes[i][ii]
        
    mediames[i]/=dia # faz a media de cada mes
    print("\n Mês: "+str(i+1)+" \n Média de temperatura: "+str(int(mediames[i]))+"°C")
    #mostra a media do mes
    print("\n (Aperte enter para continuar) ")
    enter = input()
    os.system("cls")
    
    #separação 2
print("\n Data do dia mais quente do ano: ")
for i in range(mes):# faz o calculo do dia mais quente do ano
    for ii in range(7):
        if maior < mediasmes[i][ii]:
            maior = mediasmes[i][ii]
            datad = ii+1
            datam = i+1
          

print("Dia: "+str(datad)+" Mes:"+str(datam)+"\n Média de temperatura no dia: "+str(int(maior))+"°C")
# mostra a data do dia mais quente do ano
enter = input()
os.system("cls")
#menor temperatura do ano
print("\n Data do dia mais frio do ano: ")
menor = maior
for i in range(mes):# faz o calculo do dia mais frio do ano
    for ii in range(7):
        if menor > mediasmes[i][ii]:
            menor = mediasmes[i][ii]
            datad = ii+1
            datam = i+1

print("Dia: "+str(datad)+" Mes: "+str(datam)+"\n Média de temperatura no dia: "+str(int(menor))+"°C")
# mostra a data do dia mais frio do ano
enter = input()

os.system("cls")
maior = 0

for i in range(mes):#faz o calculo do mes mais quente do ano
    if maior < mediames[i]:
        maior = mediames[i]
        datam = i+1
print(" Mês mais quente do ano: "+str(datam))#mostra na tela o mes mais quente
print( "\n Média de temperatura no mês: "+str(int(maior))+"°C\n")
enter = input()
os.system("cls")


menor = maior
for i in range(mes):# faz o calculo do mes mais frio
    if menor > mediames[i]:
        menor = mediames[i]
        datam = i+1
print("\n Mês mais frio do ano: ",datam)#mostra na tela o mes mais frio do ano
print("\n Média de temperatura no mês: ",int(menor),"°C\n")

enter = input()
os.system("cls")
print("Fim do programa!")
os.system("cls")
