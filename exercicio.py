import csv
import funcoes

regioes = funcoes.get_regiao()
reg_dict = dict.fromkeys(regioes)

for r in reg_dict:
    reg_dict[r] = dict()
    reg_dict[r]['process_time'] = funcoes.process_time()
    reg_dict[r]['region'] = r
    reg_dict[r]['crimes'] = list()

    arquivo = csv.reader(open('./_reccrimepfa-210901-151708.csv'), delimiter = ',')
    for [data, pfa, regiao, crime, total] in arquivo: 
        alerta = False  
        if regiao == r:
            if not reg_dict[r]['crimes'] and int(total) > 10:
                reg_dict[r]['crimes'].append(funcoes.add_dict(crime,total))    
            else:
                for c in reg_dict[r]['crimes']:
                    if c['crime'] == crime:
                        c['count'] = int(total) + int(c['count'])
                        alerta = True
                if alerta == False and int(total) > 10:
                    reg_dict[r]['crimes'].append(funcoes.add_dict(crime,total))

for item in list(dict(reg_dict)):
    if len(reg_dict[item]['crimes']) < 2:
        reg_dict.pop(item)

with open('.\saida.JSON', 'w+') as writer:
    for item in reg_dict:
        writer.write('\n' + str(reg_dict[item]))

print('Concluído!')