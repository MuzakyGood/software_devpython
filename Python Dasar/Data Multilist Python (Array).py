# Single List

var_list = ["Code 1","Code 2"]

print(var_list)

# MultiList

multilist = [["Data 1","Data 2"],
             ["Data 3","Data 4"],
             ["Data 5","Data 6"]]

print(multilist)

data_siswa = [
    ["Muzaky","Pria","Islam",15],
    ["Ucok","Pria","Islam",21],
    ["Alex","Wanita","Kristen",21]]

print("\n Contoh Data Siswa Multilist =",data_siswa[0])
print("\n Contoh Data Siswa nama saja Multilist =",data_siswa[1][0])

# Latihan: Buatlah biodata 3 pahlawan
# Tampilkan

data_pahlawan = [["Moh.Hatta","12 Agustus 1902 Bukkittinggi",77,"Wakil Presiden"],
                 ["Bung Tomo","13 Oktober 1920 Surabaya",61,"Pahlawan dalam pertempuran surabaya"],
                 ["Ki Hajar Dewantara","2 Mei 1889 Pakualaman",69,"Mengembangkan pendidikan di Indonesia"]]

print("\nSeluruh Data Multilist Pahlawan =",data_pahlawan)
print("\n=====Biodata Pahlawan=====")

print("\n1. Nama Pahlawan          =",data_pahlawan[0][0])
print("   Kelahiran              =",data_pahlawan[0][1])
print("   Umur sebelum meninggal =",data_pahlawan[0][2])
print("   Jasanya                =",data_pahlawan[0][3])

print("\n2. Nama Pahlawan          =",data_pahlawan[1][0])
print("   Kelahiran              =",data_pahlawan[1][1])
print("   Umur sebelum meninggal =", data_pahlawan[1][2])
print("   Jasanya                =",data_pahlawan[1][3])

print("\n3. Nama Pahlawan          =",data_pahlawan[2][0])
print("   Kelahiran              =",data_pahlawan[2][1])
print("   Umur Sebelum meninggal =",data_pahlawan[2][2])
print("   Jasanya                =",data_pahlawan[2][3])
