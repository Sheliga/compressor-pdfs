import json
import os
import sys

import PyPDF2

# Carrega os parâmetros do arquivo JSON
with open('config.json') as f:
    config = json.load(f)

# Define as pastas de entrada e saída
input_folder = config['input_folder']
output_folder = config['output_folder']

# Define o nível de compressão
# varia de 1 a 10, onde 1 é a
# compressão mais rápida e menos agressiva e
# 10 é a compressão mais lenta e agressiva.
compression = config['compression']

# Cria a pasta de saída, se ela não existir
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Percorre todos os arquivos na pasta de entrada
for filename in os.listdir(input_folder):
    # Verifica se é um arquivo PDF
    if filename.endswith('.pdf'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Abre o arquivo PDF de entrada
        with open(input_path, 'rb') as input_file:
            pdf_reader = PyPDF2.PdfFileReader(input_file)

            # Cria um objeto PDF Writer para o arquivo de saída
            pdf_writer = PyPDF2.PdfFileWriter()

            # Percorre todas as páginas do PDF
            for page_num in range(pdf_reader.numPages):
                # Obtém a página
                page = pdf_reader.getPage(page_num)

                # Define o nível de compressão
                page.compressContentStreams(compression)

                # Adiciona a página ao objeto PDF Writer
                pdf_writer.addPage(page)

            # Escreve o arquivo PDF de saída
            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)
