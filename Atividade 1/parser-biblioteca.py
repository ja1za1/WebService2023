from lxml import etree

XML = etree.parse('biblioteca.xml')

def obter_porcentagem_livros_emprestados():
    livros_emprestados = 0
    total_livros = 0
    livros = XML.getroot().find('livros')

    for livro in livros:
        livros_emprestados += int(livro.attrib['emprestados'])
        total_livros += int(livro.attrib['quantidade'])
    
    return livros_emprestados/total_livros * 100


def obter_livros_deitel():
    livros_deitel = 0
    livros = XML.getroot().find('livros')

    for livro in livros:
        autor = livro.find('autor').text
        if autor == 'Deitel':
            livros_deitel += 1
    
    return livros_deitel

def obter_menor_livro():
    menor_livro = {'titulo' : "", 'paginas' : 0}
    livros = XML.getroot().find('livros')
    for livro in livros:
        quantidade_paginas = int(livro.find('paginas').text)
        if quantidade_paginas < menor_livro['paginas'] or menor_livro['paginas'] == 0:
            menor_livro['titulo'] = livro.find('titulo').text
            menor_livro['paginas'] = quantidade_paginas
    return menor_livro
        

def obter_livro_mais_um_autor():
    livros = XML.getroot().find('livros')
    livro_multiautor = []
    for livro in livros:
        autores_livro = livro.findall('autor')
        if len(autores_livro) > 1 :
            livro_multiautor.append(livro.find('titulo').text)
    return livro_multiautor




def main():
    porcentagem_livros_emprestados = obter_porcentagem_livros_emprestados()
    print(f'Porcentagem livros emprestados = {porcentagem_livros_emprestados: .2f}')

    livros_deitel = obter_livros_deitel()
    print(f'Quantidade livros do Deitel = {livros_deitel}')

    menor_livro = obter_menor_livro()
    print(f'Menor livro = {menor_livro["titulo"]} - Quantidade de páginas = {menor_livro["paginas"]}')

    livro_multiautores = obter_livro_mais_um_autor()
    print(f'Livros que possuem mais de um autor = {", ".join(livro_multiautores)}')

if __name__ == '__main__':
    main()