
import dreieck.gueltigesDreieck as gd
import dreieck.winkelBerechnen as wb
import dreieck.dreieckSeiten as ds
import dreieck.dreieckWinkel as dw

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
    if (gd.gueltigesDreieck(a, b, c)):
        alpha, beta, gamma = wb.winkelBerechnen(a, b, c)
        print("Gültiges Dreieck:")
        print("    Seiten a / b / c -->", a, "/", b, "/", c)
        print("    Winkel α / β / γ -->", round(alpha, 2), "/", round(beta, 2), "/", round(gamma, 2))
        print("    Typ --> ", dw.dreieckWinkel(gamma), "-", ds.dreieckSeiten(a, b, c))
    else:
        print("Ungültiges Dreieck")
        print("    Seiten a / b / c -->", a, "/", b, "/", c)
    print("-" * 55)
