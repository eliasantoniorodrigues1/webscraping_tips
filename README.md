# Web Scraping
## Passo a passo para fazer um scraping útil e funcional e que não impacte os servidores de terceiros


Bots que executam scrapings estão por toda a internet e são amplamente utilizados, o Google que o diga...rsrsr
Existem diversas bibliotecas para realizar coleta de dados na web, porém para esse tutorial, iremos nos manter nas mais básicas, porém muito úteis e funcionais que são elas:

- Requests
- Beautiful Soup
- Pandas
- Selenium (Iremos apenas comentar a respeito)

## Instalação

                pip install requests, bs4, pandas, selenium

## Boas Práticas

- Estude a estrutura do site primeiro. Veja as classes HTML, CSS do site. Evite enviar comandos para classes com os atributos hidden ou visibility = hidden
- Dê uma olhada no arquivos **robots.txt** esse arquivo contém as diretrizes dos sites para o comportamento de robôs.
    para acessar esse arquivo basta acessar o endereço parecido com o abaixo:
            www.sitedoscraping.com/robots.txt

- Não seja rápido a menos que você esteja fazendo solicitações em vários URLS ao mesmo tempo, garanta que seu script não irá sobrecarregar o servidor alvo do scraping.
    Muitas vezes eu já me senti mal por usar o comando sleep(3) que faz o robô esperar por três segundos antes de fazer uma nova ação. Mas isso além de evitar bloqueios do seu IP desnecessáriamente irá garantir que o servidor não sofra com seu scraping.
- Pareça um ser humano: Clique somente onde humanos clicariam. Temos alguns sites que possuem botões fakes e quando seu robô clica neles, você é descoberto.
- Ajuste seus cabeçalhos: Muitos sites enviam ou deixam de enviar informações com base no cabeçalho da sua requisição.
   Antigamente o cabeçalho de um scraping usando a urllib era mais ou menos assim:
                    {
                        "Accept-Encoding": "identity",
                        "User-Agent": "Python-urllib/3.4"
                    }
    Sendo que o ideal é termos um cabeçalho assim:
                    {
                        'Content-Type': 'text/html; charset=utf-8',
                        'Server': 'nginx/1.19.0',
                        'X-Powered-By': 'Express',
                        'ETag': 'W/"133b69-nhRpBNUUsMSaboZmiJCgmh4xpcQ"',
                        'Strict-Transport-Security': 'max-age=15724800; includeSubDomains',
                        'X-Akamai-Transformed': '9 - 0 pmb=mTOE,1',
                        'Content-Encoding': 'gzip',
                        'Transfer-Encoding': 'chunked',
                        'Connection': 'keep-alive,
                        'Set-Cookie': 'covid19=covid19; path=/; secure'
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
                    }

## Falando do site Atmosphere:

**URL Base:**
https://site.com

**URL Pesquisa:**
/cep-lista-estado-cidade-bairro#h-lista-de-cep-nas-cidades-de-minas-gerais

O primeiro passo para pegar os dados desse site é analisar o HTML e vê onde está as informações que a gente deseja pegar:
**Ver HTML do site**

Encontrar o padrão de onde está as informações e analisar qual abordagem iremos usar:

- Simular um ser humano abrindo a página e interagindo com a página (Selenium)?
- Fazer uma requisição sem abrir o navegador e analisar o retorno dela?
    Caso o retorno seja um html já contendo as informações que desejamos poderíamos:
        - Usar regex para identificar o padrão das informações e capturar elas
        - Usar o Beautiful Soup para gerar o objeto soup que nos possibilitaria consultar tanto as tags HTMl quanto as
        classes CSS e até mesmo Java Script
        - Usar o pandas.read_html para ler todas as tabelas do site?

Após definir a abordagaem fazer a requisição e salvar os dados em um arquivo local, para evitar ficar fazendo
diversas requisições de tentativa e erro.
Tendo o arquivo na nossa máquina o proximo passo seria usar a abordagem escolhida e extrair as informações.
