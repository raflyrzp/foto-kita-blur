# Aplikasi "Foto Kita Blur" 📸✌️

Halo! Selamat datang di panduan penggunaan aplikasi "Foto Kita Blur". Aplikasi ini bisa menyalakan kamera laptopmu, mendeteksi jika kamu berpose "Peace" (✌️), dan otomatis membuat efek blur yang keren! 

Jangan khawatir jika kamu belum pernah menggunakan layar hitam ketik-ketik (terminal/Command Prompt) sebelumnya. Ikuti langkah-langkah di bawah ini pelan-pelan ya. Semuanya sangat mudah!

## Tahap 1: Persiapan Awal (Hanya dilakukan sekali)

Sebelum mulai, pastikan laptopmu memiliki dua program wajib ini (jika belum punya):
1. **Python**: Buka website [python.org](https://www.python.org/downloads/) dan klik tombol kuning "Download Python". Buka file yang terdownload. **SANGAT PENTING:** Saat layar instalasi pertama muncul, pastikan kamu mencentang kotak kecil bertuliskan *"Add python.exe to PATH"*. Setelah dicentang, baru klik "Install Now".
2. **Git**: Buka website [git-scm.com](https://git-scm.com/downloads) dan download untuk sistem operasimu. Buka filenya dan install dengan klik "Next" terus sampai selesai.

## Tahap 2: Mengambil Aplikasi ke Laptopmu

Sekarang, kita akan mengunduh aplikasi ini lewat "Layar Hitam".
1. Buka program bernama **Command Prompt** (jika kamu pakai Windows) atau **Terminal** (jika pakai Mac/Linux). 
   - *Cara buka di Windows:* Klik tombol Start/Windows di pojok kiri bawah layarmu, ketik tulisan `cmd`, lalu tekan tombol **Enter** di keyboard. Akan muncul layar hitam.
2. Di layar hitam tersebut, ketik (atau copy-paste) tulisan persis di bawah ini, lalu tekan **Enter**:
   ```bash
   git clone https://github.com/raflyrzp/foto-kita-blur.git
   ```
3. Tunggu sampai proses download selesai 100%.

## Tahap 3: Mempersiapkan Aplikasi (Hanya dilakukan sekali)

Masih di layar hitam yang sama, mari kita masuk ke folder aplikasinya. Ketik perintah di bawah ini SATU PER SATU, dan jangan lupa tekan **Enter** setiap selesai mengetik satu kotak abu-abu:

1. **Masuk ke folder aplikasi:**
   ```bash
   cd foto-kita-blur
   ```
2. **Buat "ruangan khusus" (virtual environment) agar aplikasi ini aman:**
   ```bash
   python -m venv venv
   ```
   *(Catatan: Langkah ini mungkin butuh waktu beberapa detik, tunggu sampai muncul baris baru untuk mengetik lagi).*

3. **Masuk ke dalam ruangan khusus tersebut:**
   - **Jika kamu pengguna Windows**, ketik:
     ```bash
     venv\Scripts\activate
     ```
   - **Jika kamu pengguna Mac/Linux**, ketik:
     ```bash
     source venv/bin/activate
     ```
   *(Jika berhasil, kamu akan melihat ada tulisan `(venv)` di baris ketikanmu).*

4. **Download "bahan-bahan" untuk aplikasinya (OpenCV & MediaPipe):**
   ```bash
   pip install opencv-python mediapipe
   ```
   *(Tunggu sampai proses download selesai dan layar berhenti bergerak).*

## Tahap 4: Menjalankan Aplikasi! 🚀

Jika semua persiapan di atas sudah selesai, kamu cukup mengetik perintah sakti ini lalu tekan **Enter**:

```bash
python main.py
```

Lampu kameramu akan menyala dan sebuah jendela akan terbuka!

### Cara Memainkan Aplikasinya:
1. Pastikan wajah atau tanganmu terlihat di kamera.
2. Angkat tanganmu dan buat pose **Peace / V** (Angkat jari telunjuk dan jari tengah, lalu tekuk jari lainnya).
3. Voila! Layar kamera akan otomatis memudar menjadi blur.
4. Jika kamu menurunkan tangan atau mengganti gaya, layarnya akan kembali normal.
5. Jika sudah bosan dan ingin **mematikan aplikasi**, klik jendela kameranya agar aktif, lalu tekan tombol huruf **`q`** di keyboard laptopmu.

---
**💡 Tips Penting:** 
Jika besok-besok kamu ingin membuka aplikasi ini lagi, kamu **tidak perlu** mengulang Tahap 1 dan Tahap 2!
Kamu cukup buka Command Prompt lagi, lalu ketik ini secara berurutan (tekan Enter setiap baris):
1. `cd foto-kita-blur`
2. `venv\Scripts\activate` (untuk Windows) atau `source venv/bin/activate` (untuk Mac/Linux)
3. `python main.py`

Selamat mencoba! 🎉
