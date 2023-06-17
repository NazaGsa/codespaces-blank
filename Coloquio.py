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

def fixture_torneo(equipos):
    num_equipos = len(equipos)
    partidos = []
    for i in range(num_equipos - 1):
        for j in range(i + 1, num_equipos):
            partido = (equipos[i], equipos[j])
            partidos.append(partido)
    return partidos