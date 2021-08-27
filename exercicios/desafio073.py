times = ("Flamengo", "Internacional", "Atlético-MG", "São Paulo", "Fluminense", "Grêmio", "Palmeiras", "Santos", "Athletico-PR", "Bragantino",
"Ceará SC", "Corinthians", "Atlético-GO", "Bahia", "Sport Recife", "Fortaleza", "Vasco da Gama", "Goiás", "Coritiba", "Botafogo")
print(f"Os 5 primeiros colocados são: {times[0:5]}")
print(f"Os 4 últimos colocados são: {times[-4:]}")
print(f"Os times em ordem alfabética fica: {sorted(times)}")
if "Chapecoense" not in times:
    print(f"O time Chapecoense não está em nenhuma posição")
else:
    print(f"O time Chapecoense está na posição: {times.index('Chapecoense') + 1}")
