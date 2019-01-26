
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
