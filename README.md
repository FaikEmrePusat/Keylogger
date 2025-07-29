# Keylogger & Monitoring Tools

Bu proje, klavye tuşlarını, panodaki (clipboard) değişiklikleri ve ekran görüntülerini kaydeden basit bir Python tabanlı izleme aracıdır.

## Özellikler

- **Keylogger:** Tüm tuş vuruşlarını `logs/` klasörüne zaman damgalı dosyalara kaydeder.
- **Clipboard Logger:** Panodaki değişiklikleri algılar ve (şu an sadece ekrana yazar, istenirse dosyaya kaydedilebilir).
- **Screenshot Capture:** Her 10 saniyede bir ekran görüntüsü alır ve `screenshot/` klasörüne kaydeder.

## Gereksinimler

- Python 3.x
- Gerekli kütüphaneler:
  - `pynput`
  - `pyperclip`
  - `Pillow`

Kurmak için:
```bash
pip install pynput pyperclip Pillow
```

## Kullanım

Her script bağımsız çalışır:

```bash
python logkeystokes.py
python monitoring_clip_board.py
python capture_screenshots.py
```

> Not: Scriptler Windows ortamında ve masaüstü oturumu açıkken çalışacak şekilde tasarlanmıştır.

## Dikkat

- Bu araçlar yalnızca eğitim ve test amaçlıdır. İzinsiz kullanım yasalara aykırıdır!
- Kendi bilgisayarınız dışında kullanmayınız.

## Geliştirme Önerileri

- Clipboard ve screenshot kayıtlarını da dosyaya yazacak şekilde geliştirin.
- Tüm işlevleri tek bir ana scriptte thread olarak birleştirin.
- Hata yönetimi ve loglama ekleyin.
- Kayıt dosyalarını şifreleyin veya erişimi kısıtlayın.

---

Herhangi bir sorunda veya katkı yapmak isterseniz iletişime geçebilirsiniz.