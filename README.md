# Descrição do script de compressão de PDFs em Python

Este script Python tem como objetivo comprimir arquivos PDF para reduzir o tamanho do arquivo, tornando-os mais fáceis de armazenar, enviar e compartilhar.

## Instalação de dependências

Antes de executar o script, é necessário instalar algumas dependências:

* `PyPDF2`: biblioteca Python para processamento de PDFs
* `tqdm`: biblioteca Python para exibir uma barra de progresso durante a execução do script

As dependências podem ser instaladas usando o gerenciador de pacotes `pip`. Abra o terminal e execute os seguintes comandos:

<pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"><span class="">bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">pip install PyPDF2
pip install tqdm
</code></div></div></pre>

## Utilização

Para utilizar o script, execute o seguinte comando no terminal:

<pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"><span class="">bash</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-bash">python compress_pdfs.py --input-dir caminho/para/pasta/entrada --output-dir caminho/para/pasta/saida --compression-level nivel_de_compressao
</code></div></div></pre>

Onde:

* `--input-dir`: caminho para a pasta de entrada contendo os arquivos PDF a serem comprimidos.
* `--output-dir`: caminho para a pasta de saída onde os arquivos comprimidos serão salvos.
* `--compression-level`: nível de compressão a ser aplicado (de 0 a 10, onde 0 significa sem compressão e 10 significa compressão máxima).

Por padrão, o nível de compressão é definido como 2 e a pasta de saída é definida como `compressed_pdfs` dentro da pasta de entrada. Você pode alterar esses valores editando o arquivo `config.json`.

## Funcionamento do script

O script irá percorrer todos os arquivos PDF na pasta de entrada e aplicar a compressão definida pelo usuário. O arquivo comprimido será salvo na pasta de saída com o mesmo nome do arquivo original.

Durante o processo de compressão, uma barra de progresso será exibida indicando o andamento da compressão. Ao finalizar, o script exibirá a quantidade de espaço em disco economizada pela compressão.

## Considerações finais

Este script é uma solução simples e eficiente para compressão de arquivos PDF em massa. No entanto, é importante lembrar que a compressão pode afetar a qualidade do arquivo, especialmente se o nível de compressão for muito alto. Certifique-se de testar o nível de compressão adequado para seu caso de uso específico.
