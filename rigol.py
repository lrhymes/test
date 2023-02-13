import usbtmc


b = usbtmc.Instrument(usbtmc.list_resources()[0])
b.open()
b.write("*RST")
b.write("*IDN?")
c = b.read()
print(c)

b.write(":RUN")
b.write(":StOP")

b.write(":WAV:DATA?")

t = b.read()