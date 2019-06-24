# Desafio Engenheiro de Dados
** Versão 1.0.0 **

Este desafio tem como finalidade realizar as consultas abaixo:

#### Calcular o número de hosts únicos. 
 - Informar o total de erros 404. 
 - Informar os 5 URLs que mais causaram erro 404.
 - Calcular a quantidade de erros 404 por dia e
 - Informar o total de bytes retornados no arquivo.

####  Para estes teste foram utilizados: 
- Python versão 3.6.4
- Spark versão 2.4.1

####  Dados Utilizados: 
- Julho  --  NASA_access_log_Jul95
- Agosto -- NASA_access_log_Aug95


Sobre o dataset: 
Esses dois conjuntos de dados possuem todas as requisições HTTP para o servidor da NASA Kennedy Space Center WWW na Flórida para um período específico.  
Fonte oficial do dateset: (http://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html) 

---
#### Autoria e contribuições

- Christopher Nothmann Tumenas Cabral da Costa 
<christopher.noth   mann@gmail.com>
---	

# Instrução

1. Baixe e desconpacte os arquivos zip referente aos log NASA (NASA_access_log_Jul95 e NASA_access_log_Aug95 ) em sua máquina
2. Abre o arquivo DesafioSpark.py e informe o caminho do arquivos descompatados no segundo argumento do método readTxt.Estes caminhos deverão estar preenchido conforme o exemplo, \'C:\\\Nasa\\\access_log_Jul95\'
- para o metódo readTxt que atribui a variável july informe o caminho do arquivo NASA_access_log_Jul95.
- para o metódo readTxt que atribui a variável aug informe o caminho do arquivo NASA_access_log_Aug95.
	
---
## License & copyright

 © Christopher Nothmann Tumenas Cabral da Costa