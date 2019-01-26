
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


if __name__ == "__main__":
    testWinkel = [89.0, 90.0, 91.0] 

    for winkel in testWinkel:
        print("Winkel:", winkel, " --> ", dreieckWinkel(winkel))
        print()
