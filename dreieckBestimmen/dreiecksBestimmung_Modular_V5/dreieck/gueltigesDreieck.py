
def gueltigesDreieck(a, b, c):
    ''' Prüfen, ob die drei Seiten ein Dreieck bilden können

    Arguments:
        a int -- Seite a
        b int -- Seite b
        c int -- Seite c

    Returns:
        boolean -- True wenn die drei Seiten ein Dreieck bilden
                -- False wenn die Summe der zwei kürzeren Seiten   
                   nicht grösser als die Länge der längste Seite ist       

    '''

    gueltigesDreieck = False

    if (a >= b and a>= c):
        if (b + c > a):
            gueltigesDreieck = True
    elif (b >= c and b>= a):
        if (a + c > b):
            gueltigesDreieck = True
    else:
        if (a + b > c):
            gueltigesDreieck = True

    return gueltigesDreieck


if __name__ == "__main__":
    testDreiecke = [
        [11, 10, 13],
        [3, 4, 5],
        [15, 30, 15],
        [13, 13, 25],
        [12, 14, 25]] 

    for dreieck in testDreiecke:
        a = dreieck[0]
        b = dreieck[1]
        c = dreieck[2]
        print("Seite a:", a, "- Seite b:", b, "- Seite c:", c)
        print("   --> ", gueltigesDreieck(a, b, c))
        print()
