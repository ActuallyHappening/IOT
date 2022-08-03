import time
import network
import secrets

wifi_keys = secrets.get_wifi_keys()
wifi_known_names = list(wifi_keys.keys())
wifi_known_passs = list(wifi_keys.values())

wlan = network.WLAN(network.STA_IF)
wlan.active(True)


def scan():
    return wlan.scan()


def networkInScan(__scan):
    print("networkInScan: ", wifi_known_names)
    for s in __scan:
        detected_name = s[0]
        # print(f"Checking if {detected_name}")
        if detected_name in wifi_known_names:
            return True, wifi_known_names.index(detected_name)
    return False, -1


def scanNetworks():
    return networkInScan(scan())


def plsConnect():
    can, index = scanNetworks()
    if not can:
        print('Could not find any known networks :(')
        print(f"{scan()=}")
        return False
    else:
        # print(f"{index=}")
        wifi_name = wifi_known_names[index]
        wifi_pass = wifi_known_passs[index]
        if type(wifi_pass) is not tuple:
            # print(f'Found wifi: {wifi_name}; Connecting with password: {wifi_pass}')
            print(f'Found wifi: {wifi_name}; Connecting;')
            wlan.connect(wifi_name, wifi_pass)
            # print('Connecting... _')
            tryNum = 0
            while not wlan.isconnected() and tryNum < 10:
                tryNum += 1
                time.sleep(1)
                print('Connecting ... ' + str(tryNum))
            return isGood(False)
        elif type(wifi_pass) is tuple:
            print(
                f"Found WPA2 Enterprise wifi: {wifi_name}; Connecting with username: {wifi_pass[0]}")
            wlan.connect(wifi_name, authmode=network.AUTH_WPA2_ENT,
                         username=wifi_pass[0], password=wifi_pass[1])


def isGood(getGood=False):
    if getGood:
        plsConnect()
    return wlan.isconnected()


def getGoodWIFI():
    # plsConnect()
    while not isGood():
        print("Top level attempting WIFI connect ...")
        plsConnect()
        time.sleep(1)
    # print(f"Got good wifi: {wlan.ifconfig()}")


def printStatus():
    print(f"Got good wifi: {wlan.ifconfig()}")
