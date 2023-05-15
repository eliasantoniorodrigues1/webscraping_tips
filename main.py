import requests
from bs4 import BeautifulSoup
import pandas as pd


if __name__ == '__main__':
    # url actions
    # url = 'https://atmosphere.tech/cep-lista-estado-cidade-bairro#h-lista-de-cep-nas-cidades-de-minas-gerais'
    # s = requests.Session()
    # r = s.get(url, verify=False)

    # save content
    # with open('atmosphere.html', 'w', encoding='utf-8') as f:
    #   f.write(r.text)

    # read saved data
    with open('atmosphere.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # using pandas to detect HTML tables
    data = pd.read_html(html)
    ufs = data[2]['Estado'].values.tolist()

    # consolidate data into a list
    tables = []
    cont = 0
    for table in data:
        colunas = table.columns.tolist()
        if 'Localidade' in colunas and 'Faixa de CEP' in colunas:
            tamanho = len(table)
            uf_name = []
            for i in range(tamanho):
                uf_name.append(ufs[cont])

            table['UF'] = uf_name 
            tables.append(table)

            cont += 1

    consolidado = pd.concat(tables)
    consolidado = consolidado.drop_duplicates(subset='Localidade', keep='first')
    # create zip code range
    consolidado['inicio_faixa'] = consolidado['Faixa de CEP'].str[:9].str.replace('-', '').astype(int)
    consolidado['fim_faixa'] = consolidado['Faixa de CEP'].str[12:].str.replace('-', '').astype(int)

    # drop unnecessary columns
    consolidado = consolidado.drop(columns=consolidado.iloc[:, 1:4])
    
    consolidado.to_csv('faixa_ceps.csv', index=False, encoding='latin-1')
    print('Dados salvo com sucesso!')
