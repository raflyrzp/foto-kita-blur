# Foto Kita Blur 📸✌️

Aplikasi simpel buat nge-blur kamera laptop otomatis pas kamu nunjukkin pose Peace (✌️). Dibikin pake OpenCV sama MediaPipe.

Panduan ini ditulis khusus buat anak akuntansi atau siapa pun yang belum pernah ngoding atau pegang terminal/command prompt sama sekali. Santai aja, tinggal ikuti step-by-step di bawah!

---

## 1. Install Perlengkapan Perang (Cuma sekali aja)

Sebelum mulai, laptop kamu butuh 2 aplikasi ini:

*   **Python**: Download di [python.org](https://www.python.org/downloads/). Pas install, **wajib centang** tulisan *"Add python.exe to PATH"* di bagian bawah sebelum ngeklik Install.
*   **Git**: Download di [git-scm.com](https://git-scm.com/downloads/). Klik Next-Next aja pas install sampai kelar.

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
