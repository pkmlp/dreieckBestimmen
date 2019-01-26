
import numpy

print("                                                                   ")
print("-------------------------------------------------------------------")
print("Programm zur Bestimmung eines Dreiecks anhand der drei Seitenlängen")
print("-------------------------------------------------------------------")
print("                                                                   ")
print("  Bitte drei ganzzahlige Werte (getrennt mit Leerschlag) eingeben  ")
print("    Um das Programm zu beenden alle drei Seiten mit 0 eingeben     ")
print("                                                                   ")
print("-------------------------------------------------------------------")
print("                                                                   ")

while True:

    # ------------------------------------------------------
    # Die Eingabe abholen und prüfen, ob diese gültig sind
    # ------------------------------------------------------

    eingabe = input("Eingabe der drei Seitenlängen,"
                   " getrennt mit Leerschlag: ")
    print("")

    # Die Eingabe aufteilen in eine Liste mit den Eingaben
    dreiecksSeiten = eingabe.split()

    # Prüfen, ob genau drei Werte eingegeben wurden
    if len(dreiecksSeiten) != 3:
        print("")
        print("ungültige Eingabe, bitte drei ganzzahlige "
              "Werte getrennt durch Leerschlag eingeben")
        print("")
        continue

    # Versuchen die drei Werte in numerische Werte umzuwandeln
    # wenn NOK, Fehlermeldung ausgeben und nächste Eingabe holen
    try:
        a = int(dreiecksSeiten[0])
        b = int(dreiecksSeiten[1])
        c = int(dreiecksSeiten[2])
    except:
        print("")
        print("ungültige Eingabe, bitte drei ganzzahlige "
              "Werte getrennt durch Leerschlag eingeben")
        print("")
        continue

    # Prüfen, ob Programm abgebrochen werden soll
    if a == 0 and b == 0 and c == 0:
        print("")
        print("Programm beendet")
        print("")
        break

    # Prüfen, ob die drei Seiten ein Dreick sein können,
    # wenn Ja: im Programm weiterfahren
    # wenn Nein: nächste Eingabe abholen
    if (a >= b and a >= c):
        if (b + c > a):
            pass
        else:
            print("")
            print("ungültige Eingabe, die drei "
                  "Seiten ergeben kein Dreieck")
            print("")
            continue
    elif (b >= c and b >= a):
        if (a + c > b):
            pass
        else:
            print("")
            print("ungültige Eingabe, die drei "
                  "Seiten ergeben kein Dreieck")
            print("")
            continue
    else:
        if (a + b > c):
            pass
        else:
            print("")
            print("ungültige Eingabe, die drei "
                  "Seiten ergeben kein Dreieck")
            print("")
            continue

    # ------------------------------------------------------------
    # Eingaben sind gültig, das Dreieck kann nun bestimmt werden
    # ------------------------------------------------------------

    # Bestimmung anhand der Seiten
    if (a == b and a == c):
        seitenTyp = "gleichseitig"
    elif(a == b or a == c or b == c):
        seitenTyp = "gleichschenklig"
    else:
        seitenTyp = "ungleichseitig"

    # Bestimmung anhand der Winkel:
    # Klammern von innen nach aussen auflösen:
    # Zuerst Arkuscosinus berechnen (Resultat ist in radiant, Bogenmass)
    # Arkuscosinus und muss umgewandelt werden in degree (Gradmass)
    winkel_a = numpy.rad2deg(numpy.arccos((b*b + c*c - a*a) / (2*b*c)))
    winkel_b = numpy.rad2deg(numpy.arccos((a*a + c*c - b*b) / (2*a*c)))
    winkel_c = numpy.rad2deg(numpy.arccos((a*a + b*b - c*c) / (2*a*b)))

    if (winkel_c > 90.0):
        winkelTyp = "stumpfwinklig"
    elif(winkel_c < 90.0):
        winkelTyp = "spitzwinklig"
    else:
        winkelTyp = "rechtwinklig"

    print("")
    print("Eingabe:", eingabe)
    print("Dreieckstyp: " + seitenTyp + ", " + winkelTyp)
    print("")
    print("")
