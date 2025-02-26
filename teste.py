import http.client

# Configurações da API
conn = http.client.HTTPSConnection("v3.football.api-sports.io")  # Endpoint da API-Football

headers = {
    'x-rapidapi-host': "v3.football.api-sports.io",
    'x-rapidapi-key': "74b057f6bdfbc1273e88ba141082137b"  # Substitua pela sua chave de API
}

# Parâmetros da busca (Brasileirão Série A - Temporada 2024)
params = {
    "league": 71,  # ID do Brasileirão Série A
    "season": 2023  # Temporada 2024
}

# Fazendo a requisição
conn.request("GET", "/fixtures?league=71&season=2023", headers=headers)

# Obtendo a resposta
res = conn.getresponse()
data = res.read()

# Exibindo os dados
print(data.decode("utf-8"))