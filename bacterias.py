def calcular_poblacion_bacteriana(bacterias, dias):
    for _ in range(dias):
        adultos = []
        for i in range(len(bacterias)):
            bacterias[i] -= 1  # Reducir el contador de la bacteria adulta
            if bacterias[i] == -1:
                bacterias[i] = 4  # Promover la bacteria recién nacida a adulta
                adultos.extend([4, 4])  # Agregar dos nuevas bacterias
        bacterias.extend(adultos)  # Agregar los nuevos adultos a la lista
    return len(bacterias), bacterias
