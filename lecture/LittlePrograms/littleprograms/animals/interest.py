
# zins_satz:
def verzinse(betrag : float, jahre : int = 1 , zins_satz : float = 5 ):
    return betrag * pow(1 + zins_satz / 100, jahre)
    # return betrag * (1 + zins_satz / 100) ** jahre


if __name__ == '__main__':
    print(verzinse(100, 1, 10))
    print(verzinse(5000, 7, 5 ))

    print(verzinse(1000))
    # ich möchte nur mit betrag und zin_satz aufrufen
    print(verzinse(1000, zins_satz=22))
    print(verzinse(1000, zins_satz=22, jahre = 10)) # parameter mit name zuweisen - nicht anhand der position
    # print(verzinse(betrag = 1000, 22, 10)) # geht nicht - nachdem name verwendet wurde sind positionsangaben im parameter nicht mehr möglich
    help(list)
    liste = [1, 2, 3, 4]
    liste.index(2, __stop= 20) # auch bekannte methoden haven evtl. noch weitere parameter



