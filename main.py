import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import csv
from tabulate import tabulate  # Modul tabulate

# Baca data dari file CSV
def read_csv_data(file_name):
    data = []
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def display_table(data, headers):
    print(tabulate(data, headers=headers, tablefmt='grid'))

# Data contoh
data = read_csv_data('leaf_data.csv')

# Pisahkan data menjadi fitur (X) dan label (y)
X = np.array(data[1:])[:, :-1].astype(float)
y = np.array(data[1:])[:, -1]

# Encode label menjadi angka
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Handling kasus 2: Jika ada data baru tanpa salah satu kolom
def impute_missing_data(new_data):
    # Cek apakah data memiliki semua kolom
    if new_data.shape[1] == X_train.shape[1]:
        return new_data  # Tidak ada yang hilang, kembalikan data baru

    # Hitung nilai rata-rata untuk setiap kolom dalam data latih
    column_means = np.mean(X_train, axis=0)

    imputed_data = np.copy(new_data)
    for i in range(imputed_data.shape[1]):
        if np.isnan(imputed_data[0, i]):
            imputed_data[0, i] = column_means[i]

    return imputed_data

# Buat model deep learning sederhana
model = keras.Sequential([
    keras.layers.Dense(32, input_shape=(2,), activation='relu'),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(2, activation='softmax')
])

# Kompilasi model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Latih model pada data contoh
model.fit(X_train, y_train, epochs=50, batch_size=1, verbose=1)

# Inisialisasi tabel dengan data awal
table_data = [data[0]]

while True:
    print("\nPilihan Menu:")
    print("1. Prediksi data baru")
    print("2. Prediksi data baru tanpa salah satu kolom")
    print("3. Prediksi data baru dengan satu kolom tambahan")
    print("4. Prediksi data baru dengan golongan species baru")
    print("5. Tampilkan Tabel")
    print("6. Keluar")
    choice = input("Pilih opsi (1/2/3/4/5/6): ")

    if choice == '1':
        leaf_width = float(input("Masukkan Leaf Width: "))
        leaf_length = float(input("Masukkan Leaf Length: "))
        
    
        leaf_area = leaf_width * leaf_length
        
      
        if leaf_area >= 14.80:
            predicted_species = "big-leaf"
        else:
            predicted_species = "small-leaf"
            
        print("Hasil prediksi berdasarkan Leaf Area dan Ukuran Daun:", predicted_species)

    elif choice == '2':
        leaf_width = float(input("Masukkan Leaf Width: "))
        leaf_length = float(input("Masukkan Leaf Length (kosongkan untuk small-leaf): "))
    
        if leaf_width <= 3 or (leaf_length is not None and leaf_length <= 5.1):
            predicted_species = "small-leaf"
        else:
            new_data = np.array([[leaf_width, np.nan]])  # Kolom kedua diisi dengan nilai yang hilang
            new_data_imputed = impute_missing_data(new_data)
            predicted_probs = model.predict(new_data_imputed)
            predicted_species = label_encoder.inverse_transform(np.argmax(predicted_probs))


    elif choice == '3':
        leaf_width = float(input("Masukkan Leaf Width: "))
        leaf_length = float(input("Masukkan Leaf Length: "))
        extra_column = float(input("Masukkan Nilai Kolom Tambahan: "))
        new_data = np.array([[leaf_width, leaf_length, extra_column]])
        predicted_probs = model.predict(new_data)
        predicted_species = label_encoder.inverse_transform(np.argmax(predicted_probs))
        print("Hasil prediksi untuk data baru dengan satu kolom tambahan:", predicted_species)

    elif choice == '4':
        leaf_width = float(input("Masukkan Leaf Width: "))
        leaf_length = float(input("Masukkan Leaf Length: "))
        leaf_thickness = float(input("Masukkan Tebal Daun (milimeter): "))  # Menambahkan kolom "tebal daun"
        new_species = input("Masukkan Golongan Species Baru: ")
    
        new_data = np.array([[leaf_width, leaf_length, leaf_thickness, new_species]])
    
        X_new_species = new_data[:, :-1].astype(float)
        y_new_species = new_data[:, -1]

   
        model.fit(np.vstack([X, X_new_species]), np.hstack([y, y_new_species]))

        predicted_probs = model.predict(X_new_species)
        predicted_species = label_encoder.inverse_transform(np.argmax(predicted_probs))


    elif choice == '5':
        # Tampilkan tabel dengan data baru
        display_table(table_data, headers=data[0])

    elif choice == '6':
        break

    else:
        print("Pilihan tidak valid. Silakan pilih opsi 1, 2, 3, 4, 5, atau 6.")
