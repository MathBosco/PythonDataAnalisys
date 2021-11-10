import csv
import datetime

#Adiciona dados em um dicionário
def add_dict(crime,total):
    dicionario = dict()
    dicionario['crime'] = str(crime)
    dicionario['count'] = int(total)
    return dicionario

#Retorna as regiões 
def get_regiao():
    regioes = list()
    arquivo = csv.reader(open('13.exercicio\_reccrimepfa-210901-151708.csv'), delimiter = ',')
    for [data, pfa, regiao, crime, total] in arquivo: 
        igual = False        
        if not regioes:
            regioes.append(regiao)
        else:
            for r in regioes:
                if r == regiao:
                    igual = True
                    break
            if igual == False:
                regioes.append(regiao)

    regioes.remove('Region')
    return regioes

#Retorna data
def process_time():
    data = datetime.datetime.now()
    data = data.strftime('%d/%m/%Y %H:%M')
    return data


