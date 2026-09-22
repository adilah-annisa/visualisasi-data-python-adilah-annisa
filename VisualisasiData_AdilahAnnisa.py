# Codingan Penyajian Data dan Statistika Deskripsi Menggunakan Python (Adilah Annisa - 3 TI D)
# 1. Pengorganisasian Data
# a. Penggunaan Library Python (Pandas dan Matplotlib)
import pandas as pd
import matplotlib.pyplot as plot

# b. Import Data Excel ke Python
path = r"D:\FILE PENTING ADILAH\1. KULIAH\AKADEMIK\TINGKAT 3\Semester 5\ProbStat\adilah.xlsx"
dataraw = pd.read_excel(path, sheet_name='DataGrade')
print(dataraw)

# c. Pembuatan Tabel Frekuensi berdasarkan Grade Mahasiswa
datafrq = pd.crosstab(index=dataraw['Grade'], columns='Frekuensi')
print(datafrq)

# Jika ingin menampilkan grafik apapun, gunakan perintah berikut:
plot.show()

# 2. Penyajian Data (Visualisasi Grafik dan Statistika Deskriptif)
# a. Grafik Garis
datafrq.plot(color='purple', title='Grafik Garis Frekuensi Nilai Mahasiswa', xlabel='Grade', ylabel='Frekuensi')
plot.show()

# b. Grafik Batang
datafrq.plot(kind='bar', color='red', title='Grafik Batang Frekuensi Nilai Mahasiswa', xlabel='Grade', ylabel='Frekuensi')
plot.show()

# c. Pie Chart
datafrq.plot(kind='pie', y='Frekuensi', autopct='%1.1f%%', title='Pie Chart Frekuensi Nilai Mahasiswa', legend=False)
plot.show()

# d. Statistika Deskriptif
# Mengubah Final Score menjadi data numerik
dataraw["Final Score"] = pd.to_numeric(
              dataraw["Final Score"], 
              errors='coerce')

dt = dataraw["Final Score"]

# Menghitung Statistika Deskriptif
stats = dt.describe()
stats['Standard Error'] = dt.sem()
stats['Variance'] = dt.var()
stats['Median'] = dt.median()
stats['Mode'] = dt.mode().iloc[0]
stats['Range'] = dt.max() - dt.min()
stats['Skewness'] = dt.skew()
stats['Kurtosis'] = dt.kurtosis()

# Menampilkan Hasil Statistika Deskriptif
print(stats)