aluno = []
while True:
    nome_aluno = input('nome do aluno: ')
    if nome_aluno == "fim":
       break
    aluno_parcial = int(input('parcal: '))
    aluno_bimestral = int(input('bimestral: '))
    media = (aluno_parcial+aluno_bimestral)/2
    aluno.append({'nome' : nome_aluno, "parcial" : aluno_parcial, "bimestral" : aluno_bimestral, "media" : media})
    print(aluno)
    
