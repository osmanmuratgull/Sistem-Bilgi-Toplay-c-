# Sistem Bilgi Toplayıcı
Bu proje, Python dilini kullanarak sistem donanımı ve ağ bilgilerini toplamak ve kullanıcıya sunmak amacıyla geliştirilmiştir.

## Kullanım

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları takip edin.

### Gereksinimler

- Python 3.x
- psutil kütüphanesi (psutil modülü, sistem bilgilerini elde etmek için kullanılır.)
- socket modülü (ağ arayüzlerinin IP adreslerini elde etmek için kullanılır.)

### Kurulum

1. Proje dosyalarını yerel makinenize kopyalayın.

2. Gerekli bağımlılıkları yükleyin:
<code>pip install psutil</code>

3. Projeyi çalıştırın.

## Özellikler

Bu sistem bilgi toplayıcı, aşağıdaki bilgileri kullanıcıya sunar:

- İşlemci bilgisi
- CPU çekirdek sayısı
- RAM bilgisi (Toplam RAM, Kullanılan RAM ve Boş RAM)
- Depolama bilgisi (Toplam Depolama, Kullanılan Depolama ve Boş Depolama)
- Ağ bilgisi (Ağ arayüzlerinin adları ve IP adresleri)
- İşletim sistemi türü
- Bilgisayar adı
