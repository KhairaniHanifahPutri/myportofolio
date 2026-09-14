Nama: Khairani Hanifah Putri

NPM: 2506587371

Kelas: PBP E


### Tugas 1
1. Ya, saya menggunakan <section> dalam pengerjaan tugas 1. <section> ini membantu saya dalam membuat fitur baru yaitu experience. Saya bisa membuat header baru yang bisa di click lalu mengarah ke experience. 
2. Tantangan yang saya alami saat mengatur CSS adalah saya kurang punya bayangan terkait kode ini akan seperti apa. Ini membuat saya harus berulang kali menjalankan runserver untuk melihat bagaimana design dari kode saya. Hal ini juga saya rasakan saat menyesuaikan tampilan mobile, meskipun tidak sesulit itu. Saya memprioritaskan headernya (tulisan Experience).
3. Saya tidak yakin apakah ini bisa disebut batasan, tapi bagi saya ini kurang efektif. Berhubungan dengan poin 2, saya merasa kurang efektif karena harus save lalu runserver dulu, lalu kalau ingin mengubah lagi harus stop running dulu lalu ulangi runserver. Saya berharap bisa menambahkan fungsi yang dapat menjadi solusi atas permasalahan ini. Mungkin untuk sekarang saya butuh banyak latihan, tapi kalau saya bisa menambahkan suatu fungsi, saya mau mencoba menambahkan fitur seperti "preview" berdasarkan html dan css yang sudah dibuat.
Pada tugas 1, saya tidak menggunakan AI dalam membuat kode html maupun css. Saya kebanyakan menyalin kode dari tutorial 1 lalu saya modifikasi sesuai kebutuhan tugas.

### Tugas 2
1. Sepemahaman saya, dimulai dari membuat model berdasarkan permintaan yang diterima. Modelnya dibuat di folder main\models.py, buat primary key dan field nya berdasarkan permintaan. Setelah jadi, model dimakemigrations dan migrate ke django terlebih dahulu. Jika sudah, baru edit websitenya dengan html (membuat template) dan css (desainnya). Karena ini membuka halaman baru, berarti perlu edit view dan urlnya. Buat view di main\views.py untuk membuka halaman baru, lalu url nya diedit di main\urls.py agar halamannya dapat dinavigasi nantinya. Tidak perlu mengedit portofolio\urls.py lagi karena sudah diarahkan ke main\urls.py disana. Jika sudah, di bagian template hanya perlu memasukkan urls yang sesuai ke bagian yang ingin dijadikan navigasi. Kurang lebih halaman baru selesai dibuat. 
2. Menurut saya, alasannya adalah karena data bisa sewaktu-waktu berubah. Misalnya, template dibuat pada tahun 2026. Pada saat pembuatan, experience saya kosong. Setelah berjalan setahun, saya mulai ikut organisasi sehingga experience saya bertambah. Tidak efektif jika menulis data langsung di template. Jika hanya template, aplikasi akan lebih mudah untuk ditinjau karena tidak banyak data yang tersimpan di template. Aplikasi juga akan lebih mudah di update karena tidak perlu mengubah template.
3. Sepemahaman saya, makemigrations untuk menyimpan penambahan/perubahan model, lalu migrate untuk menyesuaikan penambahan tersebut ke django. Contoh penambahan sudah ada di nomor 1. Contoh perubahan model yang perlu melakukan dua perintah tersebut adalah ketika ingin mengubah field pada modelnya. Ini terjadi saat saya ingin menambahkan tanggal pada halaman baru. Ternyata format field yang saya tulis itu mengambil tanggal saat ini data ditambahkan, bukan yang saya atur. Lalu saya menyesuaikan fieldnya. Setelah dicoba ternyata saya perlu melakukan makemigrations dan migrate lagi. 
Saya menggunakan AI (ChatGPT) untuk mencari error dari output css saya yang tidak konsisten. Namun, setelah saya menyalakan ulang laptop saya, output sudah sama. Berikut adalah link terkait prompting saya. 
https://chatgpt.com/share/6aa7ed83-f1f8-83ec-8964-d098ef8b6688