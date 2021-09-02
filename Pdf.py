# programa que seleciona varias paginas de um pdf e junta-as em um novo arquivo
"""
De modo geral, eis o que o programa deverá fazer:
• Encontrar todos os arquivos PDF no diretório de trabalho atual.
• Ordenar os nomes dos arquivos para que os PDFs sejam acrescentados na
sequência.
• Gravar as páginas de cada PDF, exceto a primeira, no arquivo de saída.
Em termos de implementação, seu código deverá fazer o seguinte:
• Chamar os.listdir() para encontrar todos os arquivos no diretório de trabalho
atual e excluir qualquer arquivo que não seja PDF.
• Chamar o método de lista sort() do Python para organizar os nomes dos
arquivos em ordem alfabética.
• Criar um objeto PdfFileWriter para o PDF de saída.
• Percorrer todos os arquivos PDF em um loop, criando um objeto
PdfFileReader para cada um.
• Percorrer as páginas (exceto a primeira) de cada arquivo PDF em um loop.
• Acrescentar as páginas ao PDF de saída.
• Gravar o PDF de saída em um arquivo chamado allminutes.pdf.
Para esse projeto, abra uma nova janela no editor de arquivo e salve o
programa como combinePdfs.py.
"""

import PyPDF2
import os
import shutil

pdfs = []
# encontrando os pdfs no diretorio:
print("No diretório atual,há os seguintes pdf's:")
for cada_pdf in os.listdir('/home/marcus/PycharmProjects/pdfs'):
    if cada_pdf.endswith('.pdf'):
        pdfs.append(cada_pdf)
pdfs.sort()
for cada_pdf in pdfs:
    print(cada_pdf)
# fazendo a leitura dos arquivos:
    pdfs1 = open(cada_pdf, 'rb')
    pdfs1_leitura = PyPDF2.PdfFileReader(pdfs1)
    for num_pag in range(1, pdfs1_leitura.numPages):
        pagina = pdfs1_leitura.getPage(num_pag)
        print(pagina.extractText())

# acrescentando em um pdf de saida
    output = PyPDF2.PdfFileWriter()
    for num_pag in range(pdfs1_leitura.numPages):
        page = pdfs1_leitura.getPage(num_pag)
        output.addPage(page)
    saida = open('projeto_saida.pdf', 'wb')
    output.write(saida)
    print('Pdf criado')
    os.mkdir('/home/marcus/PycharmProjects/pdfs/allminutes')
    shutil.copy('projeto_saida.pdf', '/home/marcus/PycharmProjects/pdfs/allminutes')
    saida.close()
    pdfs1.close()
