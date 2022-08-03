import os
os.remove('main.py')

print('Purge complete')

try:
    from Helper import networking
    import webrepl
except:
    print("Purge couldn't auto start webrepl")
else:
    networking.getGoodWIFI()
    webrepl.start()
