from usb_manager import UsbManager

usbm = UsbManager()

usbs = []
vid = ""
pid = ""
b = 0
c = 1
dings = "000"
z = 0
for x in range(65535):
    if z == 16:
        dings = "00"
    if z == 256:
        dings = "0"
    if z == 4096:
        dings = ""
    v = str(hex(x))
    vid = v.split("x")
    vids = dings + vid[1]
    test = str(usbm.filterBy(vid=vids))
    usbd = test.split(" ")
    usb = usbd[3]

    if usb not in usbs:
        usbs.append(usb)
        print("0x" + dings+ vid[1])
        bums = "000"
        for x in range(65535):
            if z == 16:
                bums = "00"
            if z == 256:
                bums = "0"
            if z == 4096:
                bums = ""
            p = str(hex(x))
            pid = p.split("x")
            pids = dings + pid[1]
        print(type(usbm.filterBy(vid= vids ,pid= pids)))
    if b == 100:
        #print("0x" + dings+ vid[1])
        print(b * c)
        c += 1
        b = 0
    b += 1
    z +=1
x = 0
for inhalt in usbs:
    x +=1
    print(inhalt)
print(len(usbs))

print(UsbManager().filterBy(vid="058f", pid="6387").get("device"))

while True:
    print('wer bist Du?')
    name = input()
    if name != 'Roger':
        continue
    print("Hallo, Roger. wie lautet das Passwort? (es ist ein Fisch.)")
    password = input()
    if password == "Schwertfisch":
        break
    else:
        print('Das Passwort war falsch')
print('Zugang gewährt.')
