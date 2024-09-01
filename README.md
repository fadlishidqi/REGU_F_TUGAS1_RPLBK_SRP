# python-srp-example

## Deskripsi

Repositori ini berisi contoh kode Python yang mendemonstrasikan **Single Responsibility Principle (SRP)**, salah satu prinsip dari SOLID dalam pemrograman berorientasi objek. SRP menyatakan bahwa setiap kelas seharusnya memiliki satu alasan untuk berubah, yaitu hanya memiliki satu tanggung jawab atau tujuan. Dengan menerapkan SRP, kita bisa menulis kode yang lebih mudah dipelihara, lebih terstruktur, dan lebih fleksibel untuk pengembangan di masa depan.

Contoh yang disediakan dalam repositori ini menunjukkan dua versi dari program sederhana yang mengelola data karyawan:

1. **Tanpa SRP**: Sebuah kelas `Employee` menangani beberapa tanggung jawab sekaligus, seperti manajemen data karyawan dan pembuatan laporan.
2. **Dengan SRP**: Tanggung jawab dipisahkan menjadi tiga kelas berbeda (`Employee`, `EmployeeDatabase`, dan `EmployeeReport`), masing-masing menangani satu tanggung jawab.

## Konten

- **`Tanpa SRP.py`**: Script Python yang menunjukkan contoh pelanggaran SRP, di mana satu kelas (`Employee`) bertanggung jawab untuk beberapa tugas.
- **`Dengan SRp.py`**: Script Python yang menunjukkan penerapan SRP yang benar dengan memisahkan tanggung jawab ke dalam beberapa kelas.
- **`README.md`**: Dokumentasi yang menjelaskan contoh kode dan manfaat penerapan SRP.
