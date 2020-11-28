def uniqueSum(eins, zwei, drei):
    if eins == zwei == drei:
        return 0

    if eins == zwei:
        return drei
    elif eins == drei:
        return zwei
    elif zwei == drei:
        return eins
    elif eins != zwei != drei:
        return eins + zwei + drei

    
