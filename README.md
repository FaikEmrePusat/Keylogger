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


## Keylogger 2.0

https://github.com/FaikEmrePusat/Keylogger/tree/keylogger_2.0
