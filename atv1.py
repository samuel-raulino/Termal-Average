
import random,os,__random,SimpleFile as SF
from temps_calc import *
def create_doubleList(a,b):
    matriz = {}
    for x in range(a):
        matriz[x] = []
        for xx in range(b):
            matriz[x].append(xx)
    return matriz

def create_list(a):
    vetor = []
    for x in range(a):
        vetor.append(x)
    return vetor
#anonimo: acesso a media de cada estação e de todos os meses
#conta premium: acesso a todos os dias registrados
#conta premim extra: acesso ao código fonte e direito de uso
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
def login():
    os.system("cls")
    a = True 
    while(a):
        print("---Login---")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        contas = SF.File("contas")
        contas.create()
        for x in range(len(contas.all_lines())):
            email_reg = contas.read_line(x)
            senha_reg = contas.read_line(x+1)
            if email_reg.strip() == email.strip():
                if senha_reg.strip() == senha.strip():
                    print("login feito com sucesso") 
                    conta = "log"
                    a = False
            elif x == len(contas.all_lines()):
                print("erro conta não encontrada\nTente novamente")
                
    
def registrar():
    contas = SF.File("contas")
    contas.create()
    os.system("cls")
    print("---registro---")
    prob = True
    while(prob):
        print("digite seu email: ")
        email = input()
        print("digite sua senha: ")
        senha = input()
        
        for x in range(len(contas.all_lines())):
            a = contas.read_line(x)
            if a.strip() == email.strip():
                print("conta já registrada") 
        prob = False
    contas.append("-"*10)
    contas.append(email)
    contas.append(senha)
    contas.append("premium: False")
    contas.append("cpf: ")
    contas.append("conta corrente: ")
    
            


os.system("cls")
print("Bem vindo ao Thermal Average!\n\n")
print("O Thermal Average é um programa que registra as temperaturas diárias de um pais ao longo dos meses.\n")
print("Você tem uma conta? ")
enter = input()
if enter == "sim":
    login()
elif enter == "não":
    print("deseja registrar? ")
    enter = input()
    if enter == "sim": 
        registrar()
        login()


print("\n\nAperte enter para começar ")
enter = input()
os.system("cls")
    
for i in range(dia):
    mediames[i] = 0

for i in range(mes):
    for ii in range(dia):
        mediasmes[i][ii] = 0
      


pais = input("Qual o pais que você deseja escolher?")
enter = input()
os.system("cls")
def mediaanual(mininverno,maxinverno,minverao,maxverao,inverno,primavera,outono,verao):
    r = __random.CustomRandom()
    for i in range(dia):
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
    _pais = Avarage(pais)
    _pais.make_avarage()
    mediaanual(_pais.mininv,_pais.maxinv,_pais.minverao,_pais.maxverao,[12,1,2],[3,4,5],[9,10,11],[6,7,8])
    
    #todas as medias de todos os meses
    print_log(" Mês "+str(m+1)+":\n")
    for i in range(dia):
        for ii in range(horas):
            mediasmes[m][i]+= mediadia[i][ii]
        mediasmes[m][i]/= horas 
        print_log(" Dia "+str(i+1)+": "+str(int(mediasmes[m][i]))+"°C \n")
      
print_log(" (Aperte enter para continuar) ")
enter_log()
os.system("cls")
print("\n")

print_log("(Aperte enter para continuar) ")
enter = input()
os.system("cls")
print(" Temperatura média de todos os meses: ")

    #separação
for i in range(mes):
    mediames[i] = 0
    for ii in range(dia):
        mediames[i] += mediasmes[i][ii]
        
    mediames[i]/=dia 
    print("\n Mês: "+str(i+1)+" \n Média de temperatura: "+str(int(mediames[i]))+"°C")
    print("\n (Aperte enter para continuar) ")
    enter = input()
    os.system("cls")
    
    #separação 2
print("\n Data do dia mais quente do ano: ")
for i in range(mes):
    for ii in range(7):
        if maior < mediasmes[i][ii]:
            maior = mediasmes[i][ii]
            datad = ii+1
            datam = i+1
          

print_log("Dia: "+str(datad)+" Mes:"+str(datam)+"\n Média de temperatura no dia: "+str(int(maior))+"°C")
enter = input()
os.system("cls")
#menor temperatura do ano
print("\n Data do dia mais frio do ano: ")
menor = maior
for i in range(mes):
    for ii in range(7):
        if menor > mediasmes[i][ii]:
            menor = mediasmes[i][ii]
            datad = ii+1
            datam = i+1

print("Dia: "+str(datad)+" Mes: "+str(datam)+"\n Média de temperatura no dia: "+str(int(menor))+"°C")
enter = input()

os.system("cls")
maior = 0

for i in range(mes):
    if maior < mediames[i]:
        maior = mediames[i]
        datam = i+1
print_prem(" Mês mais quente do ano: "+str(datam))
print_prem( "\n Média de temperatura no mês: "+str(int(maior))+"°C\n")
input_prem()
os.system("cls")


menor = maior
for i in range(mes):
    if menor > mediames[i]:
        menor = mediames[i]
        datam = i+1
print_prem("\n Mês mais frio do ano: ",datam)
print_prem("\n Média de temperatura no mês: ",int(menor),"°C\n")

input_prem()
os.system("cls")
print_log("Você deseja atualizar pra premium? ")
enter = input_log()
if enter == "sim":
    while(True):
        email = input("Digite seu email: ")
        contas = SF.File("contas")
        contas.create()
        for x in range(len(contas.all_lines())):
            email_reg = contas.read_line(x)
            if email_reg.strip() == email.strip():
                cpf = input("Digite seu cpf: ")
                conta_corrente = input("Digite sua conta: ")
                cpf = "cpf: "+cpf 
                conta_corrente = "conta corrente: "+conta_corrente
                contas.replace(x+3,cpf)
                contas.replace(x+4,conta_corrente)
                break
            elif x == len(contas.all_lines()):
                print("erro conta não encontrada\nTente novamente")
print("Fim do programa!")
os.system("cls")
