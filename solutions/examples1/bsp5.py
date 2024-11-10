def ist_schaltjahr(jahr : int) -> bool:
    if (jahr % 400) == 0:
        return True;
    if (jahr % 100) == 0:
        return False;
    if (jahr % 4) == 0:
        return True;

    return False;


if __name__ == '__main__':
    print(ist_schaltjahr(123))
    print(ist_schaltjahr(1900))
    print(ist_schaltjahr(2004))
    print(ist_schaltjahr(2000))
    print(ist_schaltjahr(8))


