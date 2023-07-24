#@osmanmuratgull

import platform
import psutil
import socket

def islemci_bilgisi():
    return platform.processor()

def cpu_bilgisi():
    return f"{psutil.cpu_count(logical=False)} fiziksel çekirdek, {psutil.cpu_count()} toplam çekirdek"

def ram_bilgisi():
    ram = psutil.virtual_memory()
    ram_toplam = ram.total / (1024 ** 3)
    ram_kullanilan = ram.used / (1024 ** 3)
    ram_bos = ram.available / (1024 ** 3)
    return f"Toplam RAM: {ram_toplam:.2f} GB, Kullanılan RAM: {ram_kullanilan:.2f} GB, Boş RAM: {ram_bos:.2f} GB"

def depolama_bilgisi():
    depolama = psutil.disk_usage('/')
    depolama_toplam = depolama.total / (1024 ** 3)
    depolama_kullanilan = depolama.used / (1024 ** 3)
    depolama_bos = depolama.free / (1024 ** 3)
    return f"Toplam Depolama: {depolama_toplam:.2f} GB, Kullanılan Depolama: {depolama_kullanilan:.2f} GB, Boş Depolama: {depolama_bos:.2f} GB"

def ağ_bilgisi():
    ağ_bilgileri = {}
    for ad, bilgiler in psutil.net_if_addrs().items():
        ip_adresleri = [bilgi.address for bilgi in bilgiler if bilgi.family == socket.AF_INET]
        ağ_bilgileri[ad] = ip_adresleri
    return ağ_bilgileri

def isletim_sistemi():
    return platform.system()

def bilgisayar_adi():
    return platform.node()

if __name__ == "__main__":
    print("İşlemci Bilgisi:", islemci_bilgisi())
    print("CPU Bilgisi:", cpu_bilgisi())
    print("RAM Bilgisi:", ram_bilgisi())
    print("Depolama Bilgisi:", depolama_bilgisi())
    print("Ağ Bilgisi:")
    for ad, ip_listesi in ağ_bilgisi().items():
        print(f"  {ad}: {', '.join(ip_listesi)}")
    print("İşletim Sistemi:", isletim_sistemi())
    print("Bilgisayar Adı:", bilgisayar_adi())
