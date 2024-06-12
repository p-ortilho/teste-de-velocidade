import speedtest

# Define o objeto de teste
teste = speedtest.Speedtest()

# Definindo o melhor servidor para teste pode ou não ser utilizado
# teste.get_best_server()

# Teste de download e upload e ping
download = teste.download() / 10**6
upload = teste.upload() / 1e+6
ping = teste.results.ping

print(f'Velocidade de download: {download:.2f}\nVelocidade de upload: {upload:.2f}\nTeste ping: {ping:.2f}')

# Para ver todos os parametros do teste
print(teste.results)