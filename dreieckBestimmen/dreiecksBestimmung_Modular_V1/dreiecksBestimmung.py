import dreiecksFunktionen as dfn

testDreiecke = [
    [11, 10, 13],
    [3, 4, 5],
    [15, 30, 15],
    [13, 13, 25],
    [12, 14, 25]
]

for dreieck in testDreiecke:
    a = dreieck[0]
    b = dreieck[1]
    c = dreieck[2]
    if (dfn.gueltigesDreieck(a, b, c)):
        alpha, beta, gamma = dfn.winkelBerechnen(a, b, c)
        print("Gültiges Dreieck:")
        print("    Seiten a / b / c -->", a, "/", b, "/" , c)
        print("    Winkel α / β / γ -->", round(alpha, 2), "/", round(beta, 2), "/", round(gamma, 2))
        print("    Typ --> ", dfn.dreieckWinkel(gamma), "-", dfn.dreieckSeiten(a, b, c))
    else:
        print("Ungültiges Dreieck")
        print("    Seiten a / b / c -->", a, "/", b, "/" , c)
    print("-" * 55)
