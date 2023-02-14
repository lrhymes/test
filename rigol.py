import usbtmc
import matplotlib.pyplot as plt

#b = usbtmc.Instrument(usbtmc.list_resources()[0])
b = usbtmc.Instrument(usbtmc.list_devices()[0])

b.open()
b.write("*RST")
b.write("*IDN?")
c = b.read()
print(c)

b.write(":RUN")
b.write(":StOP")

b.write(":WAV:DATA?")

t = b.read()
ll = list(t)
lll = ll[10:-1]
d = [int.from_bytes(bytes(c,'utf-8'),'big') for c in lll]


fig,ax = plt.subplots()
p1, = ax.plot(d)
plt.pause(0.1)

