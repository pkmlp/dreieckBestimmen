
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
