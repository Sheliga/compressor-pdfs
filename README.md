
# Script para comprimir arquivos PDF

Este script permite comprimir arquivos PDF de uma pasta especificada de um parametro vindo de um arquivo JSON externo.

## Requisitos

Para utilizar este script, é necessário ter o Python 3.x e a biblioteca PyPDF2 instalados. Para instalar a biblioteca PyPDF2, basta utilizar o seguinte comando no terminal:

<pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs">pip install PyPDF2
</code></div></div></pre>

## Funcionamento

Ao ser executado, o script irá ler um arquivo JSON externo que contém as seguintes informações:

* `input_folder`: caminho para a pasta contendo os arquivos PDF que serão comprimidos;
* `output_folder`: caminho para a pasta onde os arquivos PDF comprimidos serão salvos;
* `compression_level`: nível de compressão dos arquivos PDF (entre 0 e 1, sendo 0 sem compressão e 1 máxima compressão).

O arquivo JSON deve ter a seguinte estrutura:

<pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"><span class="">json</span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-json">{
    "input_folder": "caminho/para/pasta/entrada",
    "output_folder": "caminho/para/pasta/saida",
    "compression_level": 1
}
</code></div></div></pre>

Com essas informações, o script irá iterar sobre todos os arquivos PDF da pasta de entrada e comprimi-los de acordo com o nível de compressão especificado. Os arquivos PDF comprimidos serão salvos na pasta de saída, com o mesmo nome do arquivo original.

## Utilização

Para utilizar o script, basta executar o seguinte comando no terminal:

<pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"><span class="">bash</span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python compress_pdf.py caminho/para/arquivo.json
</code></div></div></pre>

Onde `compress_pdf.py` é o nome do script e `caminho/para/arquivo.json` é o caminho para o arquivo JSON que contém as informações de entrada.

## Limitações

Este script não é capaz de comprimir arquivos PDF protegidos por senha. Além disso, a biblioteca PyPDF2 pode apresentar problemas ao lidar com alguns tipos de arquivos PDF. Em caso de erros, recomenda-se testar o script com outros arquivos ou buscar outras bibliotecas que possam atender melhor a necessidade.
