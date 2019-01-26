
import numpy


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
        float, float, float -- die Winkel α, β, γ (0 wenn NOK)

    '''

    # Arkuscosinus berechnen gem. obiger Formeln 
    arccos_a = numpy.arccos( (b*b + c*c - a*a) / (2 * b * c) )
    arccos_b = numpy.arccos( (a*a + c*c - b*b) / (2 * a * c) )
    arccos_c = numpy.arccos( (a*a + b*b - c*c) / (2 * a * b) )

    # Arkuscosinus ist in radiant (Bogenmass) und muss umgewandelt werden in degree (Gradmass)
    winkel_a = numpy.rad2deg(arccos_a)
    winkel_b = numpy.rad2deg(arccos_b)
    winkel_c = numpy.rad2deg(arccos_c)

    return winkel_a, winkel_b, winkel_c


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
        print("   --> ", winkelBerechnen(a, b, c))
        print()
