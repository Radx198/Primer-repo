primos = []
def es_primo(i):
	cantidadDiv=0
	for ii in range(1,i+1):
		if i%ii == 0:
			cantidadDiv+=1
	if cantidadDiv == 2:
		return True
	return False
	

for i in range (1,200 +1):
	if es_primo(i):
		primos.append(i)
print(primos)
