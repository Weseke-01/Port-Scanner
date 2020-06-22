import socket

scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scanner.settimeout(5)


def uitvoeren():
    te_scannen()
    poort_scanner(poort)

    tweede_poort_scan = input("Wil je nog een poort scannen? Typ dan: 'ja' ").lower()

    if tweede_poort_scan == "ja":
        uitvoeren()
    else:
        exit()


def te_scannen():
        global host
        global poort

        host = input("Geef het IP-adres dat je wil scannen. ")
        poort = int(input("Geef de poort die je wil scannen op. "))


def poort_scanner(poort):
        if scanner.connect_ex((host, poort)):
            print("Poort", poort, "is dicht.")
        else:
            print("Poort", poort, "is open.")
    

uitvoeren()