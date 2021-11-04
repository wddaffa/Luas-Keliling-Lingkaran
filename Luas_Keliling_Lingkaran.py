print("Menghitung Luas Lingkaran")
print("======================================")
def luas_lingkaran(r):
    return 3.14 * (r * r)

r = int(input("masukan jari-jari lingkaran: "))
phi = 3.14
L = phi * (r * r)

print("Luas lingakaran dengan jari-jari {} adalah {}".format(r, L))
print("======================================")

print("Menghitung Keliling Lingkaran")
print("=============================")
def keliling_lingkaran(r):
    return 2 * phi * r

r = int(input("Masukkan jari-jari lingkaran: "))
phi = 3.14
k = 2 * phi * r

print("Keliling Lingkaran adalah {}".format(k))
print("============================")