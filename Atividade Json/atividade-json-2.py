import json



biblioteca = '''{

    "informacao": {

        "nome": "Biblioteca Municipal de Barbacena",

        "telefones": ["32 3333-3333", "32 9 9999-9999"]

    },

    "livros": {

        "romance": [

            {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "copias": 10, "emprestados": 5},

            {"titulo": "Quincas Borba", "autor": "Machado de Assis", "copias": 3, "emprestados": 3},

            {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "copias": 3, "emprestados": 0}

        ],

        "tecnologia": [

            {"titulo": "Java: como programar", "autor": "Deitel", "copias": 5, "emprestados": 4},

            {"titulo": "JavaScript: O Guia Definitivo", "autor": "David Flanagan", "copias": 5, "emprestados": 1},

            {"titulo": "C: como programar", "autor": "Deitel", "copias": 1, "emprestados": 1}

        ],

        "autoajuda": [

            {"titulo": "O Segredo", "autor": "Rhonda Byrne", "copias": 2, "emprestados": 0},

            {"titulo": "O Milagre da Manhã", "autor": "Hal Elrod", "copias": 5, "emprestados": 5},

            {"titulo": "Como Fazer Amigos e Influenciar Pessoas", "autor": "Dale Carnegie", "copias": 15, "emprestados": 8}

        ]

    }

}'''

def obter_nome_biblioteca(biblioteca_json):
    return biblioteca_json['informacao']['nome']

def obter_num_telefones_biblioteca(biblioteca_json):
    return len(biblioteca_json['informacao']['telefones'])

def obter_num_livros_autoajuda(biblioteca_json):
    num_livros = 0
    for livros_autoajuda in biblioteca_json['livros']['autoajuda']:
        num_livros += livros_autoajuda['copias']
    return num_livros

def obter_num_livros_diferentes(biblioteca_json):
    num_livros = 0
    for categoria in biblioteca_json['livros']:
        num_livros += len(biblioteca_json['livros'][categoria])
    return num_livros

def obter_num_livros_totais(biblioteca_json):
    num_livros = 0
    for categoria in biblioteca_json['livros']:
        for livro in biblioteca_json['livros'][categoria]:
            num_livros += livro['copias']
    return num_livros

def obter_num_livros_romance_emprestado(biblioteca_json):
    num_livros = 0
    for livro in biblioteca_json['livros']['romance']:
        num_livros += livro['emprestados']
    return num_livros

def obter_autor_mais_livros_emprestados(biblioteca_json):
    autor = {'nome' : "", 'livros' : 0}
    for categoria in biblioteca_json['livros']:
        for livros in biblioteca_json['livros'][categoria]:
            if livros['emprestados'] > autor['livros']:
                autor['nome'] = livros['autor']
                autor['livros'] = livros['emprestados']
    return autor['nome']

def obter_nome_livro_mais_copias(biblioteca_json):
    livro = {'nome' : "", 'copias' : 0}
    for categoria in biblioteca_json['livros']:
        for livros in biblioteca_json['livros'][categoria]:
            if livros['copias'] > livro['copias']:
                livro['nome'] = livros['titulo']
                livro['copias'] = livros['copias']
    return livro['nome']

def obter_indice_autor(autores,nome_autor):
    for i,autor in enumerate(autores) :
        if autor == nome_autor:
            return i

def obter_nome_autores_livros(biblioteca_json):
    autores = []
    for categoria in biblioteca_json['livros']:
        for livros in biblioteca_json['livros'][categoria]:
            if livros['autor'] not in autores[]:
                autores.append({'autor' : livros['autor'], 'livros' : []})
            indice_autor = obter_indice_autor(autores, livros['autor'])
            print(indice_autor)
            print(autores[indice_autor])
            # if livros['titulo'] not in autores[indice_autor][livros['autor']]:
            #     autores[indice_autor][livros['autor']].append(livros['titulo'])
    return autores                

    

def main():
    biblioteca_json = json.loads(biblioteca)

    nome_biblioteca = obter_nome_biblioteca(biblioteca_json) # 1
    numero_telefones = obter_num_telefones_biblioteca(biblioteca_json) # 2
    num_livros_autoajuda = obter_num_livros_autoajuda(biblioteca_json) # 3
    num_livros_diferentes = obter_num_livros_diferentes(biblioteca_json) # 4
    num_livros_totais = obter_num_livros_totais(biblioteca_json) # 5
    num_livro_romance_emprestados = obter_num_livros_romance_emprestado(biblioteca_json) # 6
    autor_mais_livros_emprestados = obter_autor_mais_livros_emprestados(biblioteca_json) # 7
    nome_livro_mais_copias = obter_nome_livro_mais_copias(biblioteca_json) # 8
    nome_autores_e_livros = obter_nome_autores_livros(biblioteca_json) # 9

    print(f'#1 Nome biblioteca: {nome_biblioteca}')
    print(f'#2 Numero telefones: {numero_telefones}')
    print(f'#3 Numero livros de autoajuda: {num_livros_autoajuda}')
    print(f'#4 Numero livros diferentes: {num_livros_diferentes}')
    print(f'#5 Numero livros totais: {num_livros_totais}')
    print(f'#6 Numero livros de romance emprestados: {num_livro_romance_emprestados}')
    print(f'#7 Autor com maior número de livros emprestados: {autor_mais_livros_emprestados}')
    print(f'#8 Nome do livro com mais cópias: {nome_livro_mais_copias}')
    print(f'#9 Nome de cada autor e seus livros: {nome_autores_e_livros}')





if __name__ == '__main__':
    main()




