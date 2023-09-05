import socket
import json
import random

HOST = 'localhost'
PORTA = 37000
TAMANHO_BUFFER = 4096

def printarTurmas(turmas):
    for turma in turmas:
        print(f"- {turma['nome']} - {turma['id']} {turma['ano']}")
        for aluno in turma['alunos']:
            print(f"{aluno['nome']}, {aluno['idade']} anos, matricula {aluno['matricula']}")
        print("\n")




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORTA))
    dados = bytearray()
    while True:
        dado = s.recv(TAMANHO_BUFFER)
        print(dado)
        if not dado or dado == b'\n' or dado == b'\r':
            break
        dados += dado
    turmas_json = json.loads(dados.decode())
    printarTurmas(turmas_json)
    alunos_sorteados = [random.choice(turmas_json[0]["alunos"]), random.choice(turmas_json[1]["alunos"])]
    json_alunos_sorteados = json.dumps(alunos_sorteados, ensure_ascii=False)
    print(json_alunos_sorteados)
    s.send(json_alunos_sorteados.encode())














