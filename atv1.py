
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
#anonimo: acesso apenas a media de cada estação
#conta registrada: acesso a media de cada estação e de todos os meses
#conta premium: acesso a todos os dias registrados
#conta premim extra: acesso ao código fonte e direito de uso
conta = "anonimo"

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

def login():
    pass
def registrar():
    a = True
    while(a):
        print("digite seu email: ")
        email = input()
        print("digite sua senha: ")
        senha = input()
        contas = SF.File("contas")
        contas.create()
        for x in range(len(contas.all_lines())):
            a = contas.read_line(x)
            if a == email.strip():
                print("conta já registrada") 
            elif x == len(contas.all_lines()):
                contas.read_line()
                contas.append("-"*10)
                contas.append(email)
                contas.append(senha)
                a = False
            


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


print("\n\nAperte enter para começar ")
enter = input()
os.system("cls")
    
for i in range(dia):
    mediames[i] = 0

for i in range(mes):
    for ii in range(dia):
        mediasmes[i][ii] = 0
      

print("Temperatura de todos os meses:\n")
print("(Aperte enter para continuar) ")
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
    print(_pais.maxverao)
    mediaanual(_pais.mininv,_pais.maxinv,_pais.minverao,_pais.maxverao,[12,1,2],[3,4,5],[9,10,11],[6,7,8])
    
    #todas as medias de todos os meses
    print(" Mês ",m+1,":\n")
    for i in range(dia):
        for ii in range(horas):
            mediasmes[m][i]+= mediadia[i][ii]
        mediasmes[m][i]/= horas 
        print(" Dia ",i+1,": ",int(mediasmes[m][i]),"°C \n")
      
print(" (Aperte enter para continuar) ")
enter = input()
os.system("cls")
print("\n")

print("(Aperte enter para continuar) ")
enter = input()
os.system("cls")
print(" Temperatura média de todos os meses: ")

    #separação
for i in range(mes):
    mediames[i] = 0
    for ii in range(dia):
        mediames[i] += mediasmes[i][ii]
        
    mediames[i]/=dia 
    print("\n Mês: ",i+1," \n Média de temperatura: ",int(mediames[i]),"°C")
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
          

print("Dia: ",datad," Mes:",datam,"\n Média de temperatura no dia: ",int(maior),"°C")
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

print("Dia: ",datad," Mes: ",datam,"\n Média de temperatura no dia: ",int(menor),"°C")
enter = input()

os.system("cls")
maior = 0

for i in range(mes):
    if maior < mediames[i]:
        maior = mediames[i]
        datam = i+1
print(" Mês mais quente do ano: ",datam)
print( "\n Média de temperatura no mês: ",int(maior),"°C\n")
enter = input()
os.system("cls")


menor = maior
for i in range(mes):
    if menor > mediames[i]:
        menor = mediames[i]
        datam = i+1
print("\n Mês mais frio do ano: ",datam)
print("\n Média de temperatura no mês: ",int(menor),"°C\n")

enter = input()
os.system("cls")
print("Fim do programa!")
enter = input()
os.system("cls")
