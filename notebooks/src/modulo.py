# juego.py

# Valores por acción
KILL = 3
ASSIST = 1
DEATH = -1

def calcular_puntos(kills, assists, deaths):
    return kills * KILL + assists * ASSIST + (DEATH if deaths else 0)

def resultado_ronda(ronda):
    stats_ronda = {}
    for jugador, data in ronda.items():
        puntos = calcular_puntos(data['kills'], data['assists'], data['deaths'])
        stats_ronda[jugador] = {
            'puntos': puntos,
            'kills': data['kills'],
            'assists': data['assists'],
            'deaths': data['deaths']
        }
    return stats_ronda

def mvp_de_ronda(stats_ronda):
    mvp = None
    max_puntos = float('-inf')
    for jugador, datos in stats_ronda.items():
        if datos['puntos'] > max_puntos:
            max_puntos = datos['puntos']
            mvp = jugador
    return mvp

def actualizar_acumulado(acumulado, stats_ronda, mvp_jugador):
    for jugador, datos in stats_ronda.items():
        if jugador not in acumulado:
            acumulado[jugador] = {'puntos': 0, 'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0}
        acumulado[jugador]['puntos'] += datos['puntos']
        acumulado[jugador]['kills'] += datos['kills']
        acumulado[jugador]['assists'] += datos['assists']
        acumulado[jugador]['deaths'] += int(datos['deaths'])
    if mvp_jugador:
        acumulado[mvp_jugador]['mvps'] += 1

def imprimir_tabla(tabla, titulo=""):
    if titulo:
        print(f"\n🧾 {titulo}")
    print(f"{'Jugador':<10} {'PTS':<5} {'K':<3} {'A':<3} {'D':<3} {'MVPs':<4}")
    print("-" * 35)
    for jugador, datos in tabla.items():
        print(f"{jugador:<10} {datos['puntos']:<5} {datos['kills']:<3} {datos['assists']:<3} {datos['deaths']:<3} {datos.get('mvps',0):<4}")
