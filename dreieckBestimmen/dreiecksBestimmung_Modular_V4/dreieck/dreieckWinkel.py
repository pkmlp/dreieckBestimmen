
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
