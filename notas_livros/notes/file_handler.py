import io

def handle_txt_file(f):
    arquivo = f.file.read()        
    texto = arquivo.decode("utf-8")        
    anotacoes = texto.split("==========\r")
    
    total_notas = []
    total_destaques = []
    total = []
    for a in anotacoes:        
        linhas = a.split('\n')
        print(linhas)
        if len(linhas) > 2:
            is_nota = linhas[2].find("nota") > -1
            is_destaque = linhas[2].find("destaque") > -1

            if linhas[1].find('|'):
                posicoes = linhas[1].split('|')[0].split(' ')[4]
                if posicoes.find('-') > -1:
                    posicao_inicial, posicao_final = map(int, posicoes.split('-'))
                else:
                    posicao_inicial = int(posicoes) 
                    posicao_final = int(posicoes)
                
                date = ' '.join(linhas[1].split('|')[1].split(' ')[2:])            
            else:
                posicoes = linhas[2].split('|')[0].split(' ')[4]
                if posicoes.find('-') > -1:
                    posicao_inicial, posicao_final = map(int, posicoes.split('-'))
                else:
                    posicao_inicial = int(posicoes) 
                    posicao_final = int(posicoes)
                
                date = ' '.join(linhas[2].split('|')[1].split(' ')[2:])            

            txt = linhas[4]

            data = {
                'posicao_inicial': posicao_inicial,
                'posicao_final': posicao_final,
                'data': date,
                'txt': txt
            }

            if is_nota:
                total_notas.append(data)
            elif is_destaque:
                total_destaques.append(data)
    

    i = 0  # contador de destaque
    j = 0  # contador de notas
    while i < len(total_destaques):
        if j < len(total_notas) - 1:            
            if total_notas[j]["posicao_inicial"] == total_destaques[i]["posicao_inicial"] or total_notas[j]["posicao_inicial"] == total_destaques[i]["posicao_final"]:
                data = total_notas[j]
                data['nota'] = total_notas[j]['txt']
                data['destaque'] = total_destaques[i]['txt']
                del data['txt']                
                i += 1
                j += 1
            else:
                data = total_destaques[i]
                data['nota'] = 'Esse destaque não possui nota'
                data['destaque'] = total_destaques[i]['txt']
                del data['txt']
                i += 1
        else:
            data = total_destaques[i]
            data['nota'] = 'Esse destaque não possui nota'
            data['destaque'] = total_destaques[i]['txt']
            del data['txt']
            i += 1        
        total.append(data)    
    return total