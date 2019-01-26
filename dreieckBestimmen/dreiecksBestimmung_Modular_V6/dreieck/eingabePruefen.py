
def eingabePruefen(eingabe):
    ''' Prüfen, ob im Input wirklich genau drei Integer Werte sind

    Arguments:
        list  --  Eingabe

    Returns:
        boolean -- True wenn Eingabe genau drei Integer-Werte sind
                -- False wenn nicht

    '''

    # Prüfen, ob genau drei Werte eingegeben wurden
    if len(eingabe) != 3:
        return False

    # Testen ob die drei Werte Integer Werte sind
    if (type(eingabe[0]) == int and
        type(eingabe[1]) == int and
        type(eingabe[2]) == int):
        return True
    else:
        return False


if __name__ == "__main__":
    testDreiecke = [
        [11, 10, "drei"],
        [3, 4],
        [15, 0, 15],
        [13, 13, 25],
        [12, 14, 25, 21]]

    for dreieck in testDreiecke:
        if eingabePruefen(dreieck):
            print("Input ist korrekt")
        else:
            print("Input ist nicht korrekt")
        print("   --> ", dreieck)
        print()
