
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
        return "gleichschenklig"
    else:
        return "ungleichseitig"


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
        print("   --> ", dreieckSeiten(a, b, c))
        print()
