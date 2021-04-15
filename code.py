import math

	  # waktu, paket, frekwensi, prioritas, gangguan
tabel = [["pendek", "besar", "sedang", "rendah", "gangguan"],
	 ["pendek", "kecil", "tinggi", "rendah", "normal"],
	 ["pendek", "kecil", "sedang", "tinggi", "gangguan"],
	 ["pendek", "kecil", "tinggi", "rendah", "normal"],
	 ["pendek", "kecil", "sedang", "tinggi", "normal"],
	 ["panjang", "besar", "sedang", "rendah", "normal"],
	 ["panjang", "kecil", "tinggi", "tinggi", "gangguan"],
	 ["pendek", "besar", "sedang", "rendah", "normal"],
	 ["panjang", "kecil", "rendah", "tinggi", "normal"],
	 ["pendek", "kecil", "tinggi", "tinggi", "normal"],
	 ["panjang", "besar", "tinggi", "tinggi", "normal"],
	 ["panjang", "kecil", "rendah", "tinggi", "normal"]
	]

# ============================== E(S) ==============================
print("LABEL")
gangguan = ["normal", "gangguan"]	
gtot = [0, 0]
for x in range(len(tabel)):
	if tabel[x][4] == gangguan[0]:
		gtot[0] += 1
	else :
		gtot[1] += 1
print("normal : ", str(gtot[0]))
print("gangguan : ", str(gtot[1]))
a = gtot[0]
b = gtot[1]
c = (gtot[0]+gtot[1])
ES = round((-(a/c)*math.log2(a/c) - (b/c)*math.log2(b/c)), 3)
print("E(S) : {}".format(ES))

# ============================== EWaktu ==============================
print("\nWAKTU")					# ini bisa berubah
waktu = ["pendek", "panjang"]		# ini bisa berubah
waktuHitung = [0, 0, 0, 0]
for x in range(len(tabel)):
	# pendek
	if tabel[x][0] == waktu[0]:		# ini bisa berubah
		# normal
		if tabel[x][4] == gangguan[0]:
			waktuHitung[0] += 1
		# gangguan
		else :
			waktuHitung[1] += 1
	# panjang
	else :
		# normal
		if tabel[x][4] == gangguan[0]:
			waktuHitung[2] += 1
		# gangguan
		else :
			waktuHitung[3] += 1

print("pendek normal : ", waktuHitung[0])
print("pendek gangguan : ", waktuHitung[1])
print("panjang normal : ", waktuHitung[2])
print("panjang gangguan : ", waktuHitung[3])
a = waktuHitung[0]
b = waktuHitung[1]
c = a+b
ESpendek = round((-(a/c)*math.log2(a/c) - (b/c)*math.log2(b/c)),3)
print("E(Spendek) : {}".format(ESpendek))
d = waktuHitung[2]
e = waktuHitung[3]
f = d+e
ESpanjang = round((-(d/f)*math.log2(d/f) - (e/f)*math.log2(e/f)),3)
print("E(Spanjang) : {}".format(ESpanjang))
GainWaktu = round((ES - ((c/(c+f))*ESpendek) - ((f/(c+f))*ESpanjang)), 3)
print("Gain(S, Waktu) : {}".format(GainWaktu))

# ============================== EPaket ==============================
print("\nPAKET")					# ini bisa berubah
paket = ["besar", "kecil"]			# ini bisa berubah
paketHitung = [0, 0, 0, 0]
for x in range(len(tabel)):
	# besar
	if tabel[x][1] == paket[0]:		# ini bisa berubah
		# normal
		if tabel[x][4] == gangguan[0]:
			paketHitung[0] += 1
		# gangguan
		else :
			paketHitung[1] += 1
	# kecil
	else :
		# normal
		if tabel[x][4] == gangguan[0]:
			paketHitung[2] += 1
		# gangguan
		else :
			paketHitung[3] += 1

print("besar normal : ", paketHitung[0])
print("besar gangguan : ", paketHitung[1])
print("kecil normal : ", paketHitung[2])
print("kecil gangguan : ", paketHitung[3])
a = paketHitung[0]
b = paketHitung[1]
c = a+b
ESbesar = round((-(a/c)*math.log2(a/c) - (b/c)*math.log2(b/c)),3)
print("E(Sbesar) : {}".format(ESbesar))
d = paketHitung[2]
e = paketHitung[3]
f = d+e
ESkecil = round((-(d/f)*math.log2(d/f) - (e/f)*math.log2(e/f)),3)
print("E(Skecil) : {}".format(ESkecil))
Gainpaket = round((ES - ((c/(c+f))*ESbesar) - ((f/(c+f))*ESkecil)), 3)
print("Gain(S, paket) : {}".format(Gainpaket))

# ============================== EFrekwensi ==============================
print("\nFREKWENSI")					# ini bisa berubah
frekwensi = ["sedang", "tinggi", "rendah"]			# ini bisa berubah
frekwensiHitung = [0, 0, 0, 0, 0, 0]
for x in range(len(tabel)):
	# sedang
	if tabel[x][2] == frekwensi[0]:		# ini bisa berubah
		# normal
		if tabel[x][4] == gangguan[0]:
			frekwensiHitung[0] += 1
		# gangguan
		else :
			frekwensiHitung[1] += 1
	# tinggi
	elif tabel[x][2] == frekwensi[1]:		# ini bisa berubah
		# normal
		if tabel[x][4] == gangguan[0]:
			frekwensiHitung[2] += 1
		# gangguan
		else :
			frekwensiHitung[3] += 1
	# rendah
	else :
		# normal
		if tabel[x][4] == gangguan[0]:
			frekwensiHitung[4] += 1
		# gangguan
		else :
			frekwensiHitung[5] += 1

print("sedang normal : ", frekwensiHitung[0])
print("sedang gangguan : ", frekwensiHitung[1])
print("tinggi normal : ", frekwensiHitung[2])
print("tinggi gangguan : ", frekwensiHitung[3])
print("rendah normal : ", frekwensiHitung[4])
print("rendah gangguan : ", frekwensiHitung[5])
a = frekwensiHitung[0]
b = frekwensiHitung[1]
c = a+b
ESsedang = round((-(a/c)*math.log2(a/c) - (b/c)*math.log2(b/c)),3)
print("E(Ssedang) : {}".format(ESsedang))
d = frekwensiHitung[2]
e = frekwensiHitung[3]
f = d+e
EStinggi = round((-(d/f)*math.log2(d/f) - (e/f)*math.log2(e/f)),3)
print("E(Stinggi) : {}".format(EStinggi))
g = frekwensiHitung[4]
h = frekwensiHitung[5]
i = g+h
print("E(Srendah) : tidak dapat dikalkulasi")
Gainfrekwensi = round((ES - ((c/(c+f+i))*ESsedang) - ((f/(c+f+i))*EStinggi)), 3)
# Gainpaket     = round((ES - ((c/(c+f))*ESbesar) - ((f/(c+f))*ESkecil)), 3)
print("Gain(S, frekwensi) : {}".format(Gainfrekwensi))

# ============================== EPrioritas ==============================
print("\nPRIORITAS")					# ini bisa berubah
prioritas = ["rendah", "tinggi"]			# ini bisa berubah
prioritasHitung = [0, 0, 0, 0]
for x in range(len(tabel)):
	# rendah
	if tabel[x][3] == prioritas[0]:		# ini bisa berubah
		# normal
		if tabel[x][4] == gangguan[0]:
			prioritasHitung[0] += 1
		# gangguan
		else :
			prioritasHitung[1] += 1
	# tinggi
	else :
		# normal
		if tabel[x][4] == gangguan[0]:
			prioritasHitung[2] += 1
		# gangguan
		else :
			prioritasHitung[3] += 1

print("rendah normal : ", prioritasHitung[0])
print("rendah gangguan : ", prioritasHitung[1])
print("tinggi normal : ", prioritasHitung[2])
print("tinggi gangguan : ", prioritasHitung[3])
a = prioritasHitung[0]
b = prioritasHitung[1]
c = a+b
ESrendah = round((-(a/c)*math.log2(a/c) - (b/c)*math.log2(b/c)),3)
print("E(Srendah) : {}".format(ESrendah))
d = prioritasHitung[2]
e = prioritasHitung[3]
f = d+e
EStinggi = round((-(d/f)*math.log2(d/f) - (e/f)*math.log2(e/f)),3)
print("E(Stinggi) : {}".format(EStinggi))
Gainprioritas = round((ES - ((c/(c+f))*ESrendah) - ((f/(c+f))*EStinggi)), 3)
print("Gain(S, prioritas) : {}".format(Gainprioritas))
