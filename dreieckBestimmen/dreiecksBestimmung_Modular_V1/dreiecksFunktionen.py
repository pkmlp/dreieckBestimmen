
import numpy


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

    if (a >= b and a >= c):
        if (b + c > a):
            gueltigesDreieck = True
    elif (b >= c and b >= a):
        if (a + c > b):
            gueltigesDreieck = True
    else:
        if (a + b > c):
            gueltigesDreieck = True

    return gueltigesDreieck


def winkelBerechnen(a, b, c):
    ''' Winkel Berechnung mit Kosinussatz anhand der drei Seiten eines Dreieckes

    α = arccos( (b² + c² - a²) / 2bc )
    β = arccos( (a² + c² - b²) / 2ac )
    γ = arccos( (a² + b² - c²) / 2ab )

    Quelle: https://rechneronline.de/pi/dreieck.php

    Arguments:
        a int -- Seite a
        b int -- Seite b
        c int -- Seite c

    Returns:
        float, float, float -- die Winkel α, β, γ

    '''

    # Arkuscosinus berechnen gem. obiger Formeln
    arccos_a = numpy.arccos((b*b + c*c - a*a) / (2 * b * c))
    arccos_b = numpy.arccos((a*a + c*c - b*b) / (2 * a * c))
    arccos_c = numpy.arccos((a*a + b*b - c*c) / (2 * a * b))

    # Arkuscosinus ist in radiant (Bogenmass) und muss umgewandelt
    # werden in degree (Gradmass)
    winkel_a = numpy.rad2deg(arccos_a)
    winkel_b = numpy.rad2deg(arccos_b)
    winkel_c = numpy.rad2deg(arccos_c)

    return winkel_a, winkel_b, winkel_c


def dreieckSeiten(seite_a, seite_b, seite_c):
    ''' Definition des Dreieckes anhand der Seiten

    Arguments:
        a int -- Seite a
        b int -- Seite b
        c int -- Seite c

    Returns:
        str -- gleichseitig, gleichschenklig, ungleichseitig

    '''

    if (seite_a == seite_b and seite_a == seite_c):
        return "gleichseitig"
    elif(seite_a == seite_b or seite_a == seite_c or seite_b == seite_c):
        return "geleichschenklig"
    else:
        return "ungleichseitig"


def dreieckWinkel(gamma):
    ''' Definition des Dreieckes anhand des Winkels gamma

    Arguments:
        γ float -- Winkel γ

    Returns:
        str -- rechtwinklig, spitzwinklig, stumpfwinklig

    '''

    if (gamma > 90.0):
        return "stumpfwinklig"
    elif(gamma < 90.0):
        return "spitzwinklig"
    else:
        return "rechtwinklig"
