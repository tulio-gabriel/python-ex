from cadastro import leiaint,linha,cabeca,menu
from cadastro import arquivo
arq='curso.txt'
if not arquivo.arquivoexiste(arq):
    arquivo.criararquivo(arq)
while True:
    resposta=menu(['ver pessoas cadastradas', 'cadastrar novas pessoas' , 'finalizar'])
    if resposta==1:
        arquivo.lerarquivo(arq)
    elif resposta==2:
        cabeca('\033[34mNOVO CADASTRO:\033[m')
        new=str(input('\033[32mdigite o nome a ser cadastrado:\033[m'))
        newi=str(input(f'\033[32mdigite a idade de {new} a ser cadastrada:\033[m'))
        while newi.isnumeric()<=0 or newi.isalpha()==True or newi.strip()=='':
            newi = str(input(f'\033[31mERRO, digite a idade de {new} a ser cadastrada:\033[m'))
        arquivo.addtext(new,newi)
        print(f'\033[32m{new}-{newi} cadastrado(a) com sucesso\033[m')
    elif resposta==3:
        cabeca('\033[33mfinalizando o programa\033[m')
        break    else:
        print('\033[31merro, digite um valor valido:\033[m')




