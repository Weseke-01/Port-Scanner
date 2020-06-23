import socket

scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scanner.settimeout(5)


def uitvoeren():
    while True:
        vraag_invoer()
        scan_poort(poort)

        tweede_poort_scan = input("Wil je nog een poort scannen? Typ dan: 'ja' ").lower()

        if tweede_poort_scan != "ja":
            exit()


def vraag_invoer():
        global host
        global poort

        host = input("Geef het IP-adres dat je wil scannen. ")
        poort = int(input("Geef de poort die je wil scannen op. "))


def scan_poort(poort):
        if scanner.connect_ex((host, poort)):
            print("Poort", poort, "is dicht.")
        else:
            print("Poort", poort, "is open.")
    

uitvoeren()