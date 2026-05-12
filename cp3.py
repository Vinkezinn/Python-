temperaturas = [
    [28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]
]

limite_temp = 33


sala_critica = 1
mais_criticos = 0

for i in range(len(temperaturas)):
    sala = temperaturas[i]
    numero_sala = i + 1
    media = sum(sala) / len(sala)
    registros_criticos = sum(1 for t in sala if t >= limite_temp)

    print(f"Sala {numero_sala}:")
    print(f"Temperaturas registradas : {sala}")
    print(f"Média     : {media:.1f}°C")
    print(f"Registros críticos (≥33°C): {registros_criticos}")
    print("\n")

    if registros_criticos > mais_criticos:
        maior_criticos = registros_criticos
        sala_critica = numero_sala

print(f"Sala com maior risco: sala {sala_critica}")