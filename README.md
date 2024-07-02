# teste-de-velocidade

Simples script de teste de velocidade de internet usando a biblioteca speedtest.

- speedtest.Speedtest() → cria o objeto que é responsável por criar os teste de internet.

- test.download() → responsável por receber a taxa de download da internet, dividimos essa taxa por 10**6, para obter o dado em megabits e não em bits.

- test.upload() → responsável por receber a taxa de upload da internet, dividimos essa taxa por 1e+6, para obter o dado em megabits e não em bits. 1e+6 é a anotação que representa 10**6.

- test.results.ping → retorna um dicionário contendo informações sobre o teste, nesse caso pegamos somente a chave com o valor ping.

- teste.get_best_server() → seleciona o melhor servidor para fazer o teste, `não é muito bom`.

- teste.results → retorna todos os parâmetros do teste.

- speedtest.shell() → faz o teste de maneira automática pelo shell, mostrando os detalhes.
