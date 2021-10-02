# Conversor de medidas em python
medida = float(input('Uma distância em metros: '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida * 0.1
hm = medida * 0.01
km = medida * 0.001
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm, a {}dam, {}hm, {}km '.format(medida, cm, mm, dam, hm, km))