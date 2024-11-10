def flugweite(weite : float) -> int:
    if weite > 198.7:
        return 1
    elif weite > 197.1:
        return 2
    elif weite > 195:
        return 3
    elif weite == 193.67:
        return 4
    elif weite >= 100 and weite <= 150:
        return 20
    elif weite >= 20 and weite <= 50:
        print("Achtung Unfall - Rettung rufen")
        return None # sorry wurde nicht spezifiziert

if __name__ == '__main__':
    print(flugweite(199))
    print(flugweite(198))
    print(flugweite(196))
    print(flugweite(193.67))
    print(flugweite(120))
    print(flugweite(33))
