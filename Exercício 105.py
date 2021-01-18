def notas(*num, sit=False):
    '''
    -- Função para analisar notas e calcular suas situações
    :param num: uma ou várias notas dos alunos
    :param sit: valor opcional, em que se deve ou não adicionar a situação
    :return: retorna um dicionário com os valores representados
    '''
    dic = dict()
    média = sum(num)/len(num)
    if média >= 7:
        situação = 'Aprovado'
    elif média >= 5:
        situação = 'Razoável'
    elif média < 5:
        situação = 'Ruim'
    dic['total'] = len(num)
    dic['maior'] = max(num) 
    dic['menor'] = min(num)
    dic['média'] = sum(num)/len(num)
    if sit:
        dic['sit'] = situação
    return dic


resp = notas(5.5, 10, 5, 5, sit=True)
print (resp)