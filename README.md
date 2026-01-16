
Teste Técnico DClick: Automação em Python para baixar uma planilha xlsx e depois preencher o formulário com todos os dados.


## Estrutura do projeto
- `main.py`: Define as URLS e chama a função principal.
- `download_xlsx.py`: Função que inicia o teste, preenche os formulários e chama a função de baixar a planilha.
- `download_xlsx`: Função que baixa a planilha via requests.



## Requisitos
- Python 3.1x
- Bibliotecas:
  - `selenium` (para automação no navegador)
  - `pandas` (para manipulação de dados)
  - `requests` (para download de arquivos)
  - `openpyxl` (para leitura de arquivos Excel)
## Configuração e Execução
1. **Clonar o repositório**
   ```bash 
   git clone https://github.com/romulosousi/rpa-challenge.git
   cd rpa-challenge
2. **Instalar dependências**
   ```bash
    pip install -r requirements.txt

3. **Executar o script principal**
   ```bash
   python main.py
