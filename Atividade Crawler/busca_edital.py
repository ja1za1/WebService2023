import pickle
import time

NOTICES_FILE = 'editais.pickle'

with open(NOTICES_FILE, 'rb') as arquivo:
    editais = pickle.load(arquivo)

def buscar_editais(termos, filtro_modalidade=None, filtro_numero=None, filtro_ano=None, filtro_situacao=None):
    resultados = []

    for edital in editais:
        if all(termo.lower() in edital['titulo'].lower() for termo in termos):
            if (filtro_modalidade is None or edital['modalidade'] == filtro_modalidade) and \
               (filtro_numero is None or int(edital['numero']) == filtro_numero) and \
               (filtro_ano is None or int(edital['ano'].replace('.', "")) == filtro_ano) and \
               (filtro_situacao is None or edital['situacao'] == filtro_situacao):
                resultados.append(edital)
    return resultados


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Buscar editais')
    parser.add_argument('termos', nargs='+', help='Termos de busca')
    parser.add_argument('-modalidade', help='Filtro de modalidade')
    parser.add_argument('-numero', type=int, help='Filtro de número')
    parser.add_argument('-ano', type=int, help='Filtro de ano')
    parser.add_argument('-situacao', help='Filtro de situação')
    args = parser.parse_args()

    termos_busca = args.termos
    filtro_modalidade = args.modalidade
    filtro_numero = args.numero
    filtro_ano = args.ano
    filtro_situacao = args.situacao

    inicio_busca = time.time()
    resultados = buscar_editais(termos_busca, filtro_modalidade, filtro_numero, filtro_ano, filtro_situacao)
    tempo_busca = round((time.time() - inicio_busca),3)

    print(f'Termo de busca: {" ".join(f"{termo}" for termo in termos_busca)}\n')
    print('Filtros:')
    
    if filtro_ano:
        print(f'  ano: {filtro_ano}')
    if filtro_numero:
        print(f'  numero: {filtro_numero}')
    if filtro_situacao:
        print(f'  situação: {filtro_situacao}')
    if filtro_modalidade:
        print(f'  modalidade: {filtro_modalidade}')

    print(f'\nTempo de resposta: {tempo_busca}ms\n')
    print(f'{len(resultados)} resultados\n')
    print('------------')
    for idx, edital in enumerate(resultados, start=1):
        print(f"\n{edital['titulo']}\n")
        print(f"Link: {edital['link_pdf']}\n")
        if idx != len(resultados):
            print('------------')

if __name__ == "__main__":
    main()
