#Creamos un programa que nos permite ingresar X cantidad de equipos para un torneo de futbol.
print("#"*20)
print("Torneo de Futbol")
print("#"*20)
def ingresar_equipos():
    num_equipos = int(input("Cantidad de equipos en el torneo: "))
    equipos = []
    for i in range(num_equipos):
        equipo = input("Ingrese el nombre del equipo" + str(i+1) + ": ")
        equipos.append(equipo)
    return equipos

#Creamos el fixture, donde se enfrentan en cada fehca los equipos.
def fixture_torneo(equipos):
    num_equipos = len(equipos)
    partidos = []
    for i in range(num_equipos - 1):
        for j in range(i + 1, num_equipos):
            partido = (equipos[i], equipos[j])
            partidos.append(partido)
    return partidos

#Solicitamos al usuario ingresar los goles del equipo local y visitante, el equipo con mas goles es el ganador.

def resultados_partidos(partidos):
    resultados = {}
    for partido in partidos:
        equipo_local = partido[0]
        equipo_visitante = partido[1]
        resultado_local = int(input("Ingrese el resultado del partido " + str(equipo_local) + " VS " + str(equipo_visitante) + ": " ))
        resultado_visitante = int(input("Ingrese el resultado del partido " + str(equipo_visitante) + " VS " + str(equipo_local) + ": "))
        resultados[partido] = (resultado_local, resultado_visitante)
    return resultados

#Creamos una funcion donde calcule los puntos de cada partido. (Victoria + 3), (Empate + 1), (Derrota no suma)
#Se calcula la puntuacion y los goles a favor y en contra y se arma la tabla de posiciones.

def tabla_posiciones(equipos, resultados):
    tabla_posiciones = {}
    for equipo in equipos:
        tabla_posiciones[equipo] = {"Puntos": 0, "Goles a favor": 0, "Goles en contra": 0}

    for partido in resultados:
        goles_local = resultados[partido][0]
        goles_visitantes = resultados[partido][1]

        equipo_local = partido[0]
        equipo_visitante = partido[1]

        if goles_local > goles_visitantes:
            tabla_posiciones[equipo_local]["Puntos"] += 3
        elif goles_local < goles_visitantes:
            tabla_posiciones[equipo_visitante]["Puntos"] += 3
        else:
            tabla_posiciones[equipo_local]["Puntos"] += 1
            tabla_posiciones[equipo_visitante]["Puntos"] += 1
        
        tabla_posiciones[equipo_local]["Goles a favor"] += goles_local
        tabla_posiciones[equipo_local]["Goles en contra"] += goles_visitantes
        tabla_posiciones[equipo_visitante]["Goles a favor"] += goles_visitantes
        tabla_posiciones[equipo_visitante]["Goles en contra"] += goles_local
    return tabla_posiciones

equipos = ingresar_equipos()
partidos = fixture_torneo(equipos)
resultados = resultados_partidos(partidos)
posiciones = tabla_posiciones(equipos, resultados)
print(posiciones)
