# Foto Kita Blur 📸✌️

Aplikasi simpel buat nge-blur kamera laptop otomatis pas kamu nunjukkin pose Peace (✌️). Dibikin pake OpenCV sama MediaPipe.

Panduan ini ditulis khusus buat kamu yang belum pernah ngoding atau pegang terminal/command prompt sama sekali. Santai aja, tinggal ikuti step-by-step di bawah!

---

## 1. Install Perlengkapan (Cuma sekali aja)

Sebelum mulai, laptop kamu butuh 2 aplikasi ini. Berikut cara instalnya secara detail:

### A. Cara Install Python
1. Buka website [python.org/downloads](https://www.python.org/downloads/).
2. Klik tombol kuning besar bertuliskan **"Download Python"** untuk mengunduh installer.
3. Buka file installer yang baru saja kamu download (biasanya ada di folder *Downloads* kamu).
4. **⚠️ LANGKAH WAJIB:** Pada halaman pertama instalasi, lihat bagian paling bawah dan **centang** kotak kecil bertuliskan **"Add python.exe to PATH"**. Jika kamu melewatkan langkah ini, aplikasi tidak akan bisa berjalan di terminal.
5. Setelah dicentang, klik tombol **"Install Now"** di bagian atas.
6. Tunggu prosesnya sampai selesai, lalu klik **"Close"**.

### B. Cara Install Git
1. Buka website [git-scm.com/downloads](https://git-scm.com/downloads).
2. Klik opsi **"Windows"** (atau sesuaikan dengan laptopmu).
3. Pilih versi installer (misalnya klik **"64-bit Git for Windows Setup"**).
4. Buka file installer Git yang sudah selesai di-download.
5. Klik **"Next"** terus-menerus tanpa perlu mengubah pengaturan apa pun sampai proses instalasi berjalan.
6. Setelah selesai, klik **"Finish"**.

---

## 2. Download Kodenya

Kita bakal download kodenya lewat terminal/layar hitam:

1.  Buka **Command Prompt** (Windows) atau **Terminal** (Mac/Linux).
    *   *Cara buka di Windows:* Klik tombol Start, ketik `cmd`, lalu tekan **Enter**.
2.  Copas perintah di bawah ini ke layar hitam itu, terus tekan **Enter**:
    ```bash
    git clone https://github.com/raflyrzp/foto-kita-blur.git
    ```
3.  Tungguin sampai proses downloadnya selesai.

---

## 3. Setup Aplikasi

Masih di layar hitam yang sama, jalankan perintah di bawah ini satu-satu (jangan lupa tekan **Enter** tiap habis ngetik):

1.  **Masuk ke folder proyek:**
    ```bash
    cd foto-kita-blur
    ```
2.  **Bikin virtual environment (biar rapi dan ga ngerusak sistem laptop):**
    ```bash
    python -m venv venv
    ```
    *(Tunggu beberapa detik sampai muncul baris baru)*
3.  **Aktifkan virtual environment-nya:**
    *   **Pengguna Windows:**
        ```bash
        venv\Scripts\activate
        ```
    *   **Pengguna Mac/Linux:**
        ```bash
        source venv/bin/activate
        ```
    *(Kalau berhasil, bakal muncul tulisan `(venv)` di sebelah kiri baris perintahmu)*
4.  **Install library pendukungnya:**
    ```bash
    pip install opencv-python mediapipe
    ```
    *(Tunggu proses download-nya selesai)*

---

## 4. Waktunya Nyobain! 🚀

Tinggal ketik perintah ini terus **Enter**:

```bash
python main.py
```

Nanti kamera laptop kamu bakal nyala. 

*   **Cara pakainya:** Arahkan tangan ke kamera, terus tunjukkin jari telunjuk sama jari tengah (pose Peace ✌️). Layar bakal otomatis nge-blur halus.
*   **Cara matiinnya:** Klik dulu di jendela kameranya, terus tekan tombol huruf **`q`** di keyboard.

---

## 💡 Catatan buat Nanti

Kalau besok-besok kamu mau jalanin aplikasinya lagi, kamu **nggak perlu** ngulang langkah 1 dan 2. Cukup buka Command Prompt, terus ketik ini berurutan:

```bash
cd foto-kita-blur
venv\Scripts\activate  # (atau source venv/bin/activate kalau di Mac)
python main.py
```

Gampang kan? Selamat mencoba! 🎉
