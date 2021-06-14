def gerar_professores(pagina):

    nomes_arq = open("resources/nomes_professores.txt", 'r') 
    fotos_arq = open("resources/urls_fotos", 'r')

    # Os ultimos elementos das listas são \n, por isso nós pegamos até o penúltimo.
    nomes = nomes_arq.read().split('\n')[:-1]
    fotos = fotos_arq.read().split('\n')[:-1]
    conteudo_interativo = open("templates/index-interativo.html").read()

    codigo = ""
    for i in range(0, len(nomes)):
        caminho_foto = "resources/fotos-professores/" + fotos[i]
        snippet_item = "\t    <li>\n"
        snippet_item_f = 2 * '\t' + "</li>\n"
        snippet_nome = 2 * '\t' + "<p> " + nomes[i] + "</p>\n"
        snippet_foto = 2 * '\t' + "<img src='" + caminho_foto + "' alt='Foto de perfil do professor'>\n" 

        codigo += snippet_item + snippet_nome + snippet_foto + conteudo_interativo + snippet_item_f

    nomes_arq.close()
    fotos_arq.close()

    pagina.write(codigo)

def gerar_inicio_da_pagina(pagina):
    
    temp = open("templates/index-inicial.html", 'r')
    INICIO = temp.read()
    temp.close()

    pagina.write(INICIO)

def gerar_final_da_pagina(pagina):

    temp = open("templates/index-final.html", 'r')
    FINAL = temp.read()
    temp.close()

    pagina.write(FINAL)


pagina = open("index.html", 'w')

gerar_inicio_da_pagina(pagina)
gerar_professores(pagina)
gerar_final_da_pagina(pagina)

pagina.close()