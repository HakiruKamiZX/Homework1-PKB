HomeWork PKB 

Anggota :  

Andreas             - 13136210
Krisna Humnasi      - 1313621015
Aditya Nugraha      - 1313621024      
Handrian Wibisono R - 1313621036

--------Panduan pengunaan program :--------

1. Install tensorflow, tabulate
2. import dataset dibawah ini ke CSV (atau download file CSV yang ada) (namakan file : 'leaf_data.csv')

| Leaf Width | Leaf Length |  Species  |
|------------|-------------|-----------|
|    2.7     |     4.9     | small-leaf|
|    3.2     |     5.5     | big-leaf  |
|    2.9     |     5.1     | small-leaf|
|    3.4     |     6.8     | big-leaf  |

3.run program di command prompt
--------------------------------------------

-------- Penjelasan program --------

1. program dimulai dengan membaca file csv yang 'wajib' dinamakan "leaf_data.csv"
2. kemudian program akan meminta pilihan 1-4
3. untuk pilihan 1  menentukan apakah sbeuah daun small atau big, saya menggunakan algoritma dimana panjang dan lebar daun dikali dan jika hasilnya dibawah atau sama dengan 14.80 makan hasilnya akan jadi small leaf dan sebaliknya
4. untuk opsi 2, saya menggunakan parameter untuk panjang daun jika dibawah/sama dengan 5.1 atau lebar daun dibawah/sama 3, maka daun tergolong small, dan sebaliknya
5. untuk opsi 3 dan 4, kita menambahkan kolom "ketebalan daun = 'leaf_thickness'" sebagai definisi spesies baru, dan menentukannya dengan parameter data yang ada yaitu panjang dan lebar daun
