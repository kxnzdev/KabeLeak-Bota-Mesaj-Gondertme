# Discord Kanalına Otomatik Mesaj Gönderen Bot

Bu Python tabanlı Discord botu, belirli bir kanala otomatik olarak mesaj gönderebilir. Botu hızlıca kurup başlatmak için aşaşıdaki adımları takip etmeniz yeterlidir.

---

##  Kurulum

### 1. Python Gereksinimi
Botu çalıtırmak için bilgisayarınızda [Python 3.8+](https://www.python.org/downloads/) yüklü olmalıdır.

### 2. Gerekli Kütüphane: `discord.py`

Terminal veya Komut İstemi'nde şu komutu çalıştırarak gerekli kütüphaneyi yükleyin:

```
pip install -U discord.py
```

Alternatif olarak:

```
python -m pip install -U discord.py
```
yada direk kurulum.bat dosyasını çalıştırarak kurabilirsiniz
---

##  Bot Yapılandırma
channel_id = 123456789012345678


- `BOT_TOKENİNİ_BURAYA_YAPIŞTIR`: [Discord Developer Portal](https://discord.com/developers/applications) üzerinden oluşturduğunuz botun token'ını buraya yapıştırın.
- `channel_id`: Mesaj gönderilecek kanalın ID sini yazın.

### 2. Kanal ID'si Nasıl Alınır?

1. Discord'da "Ayarlar > Geliştirici Modu"nu açın.
2. Kanal adına sağ tıklayın ID Kopyala??*

---

##  Botu çalıştırma

### Yöntem 1: Manuel Başlatma

Klasörünüzde şu komutu çalıştırarak botu başlatabilirsiniz:

```
python bot.py
```

### Yöntem 2: `.bat` Dosyası ile Otomatik Başlatma

Klasörde bulunan `baslat.bat` dosyasına çift tıklayarak botu çalıştırabilirsiniz.

Eğer `python` komutu tanınmıyorsa tam yolu girin:
```bat
"C:\Python311\python.exe" bot.py
pause
```

---

##  Destek ve Topluluk

Herhangi bir sorunla karşılaşırsanız veya yardım almak isterseniz, topluluğumuza katılabilirsiniz:

?? **[Destek Sunucusu](https://discord.gg/kabeleak)**

---

## Lisans
Bu proje [MIT Lisansı](https://opensource.org/licenses/MIT) ile lisanslanmıştır. Dilediğiniz gibi kullanabilir, dağıtabilir ve geliştirebilirsiniz.
"""
