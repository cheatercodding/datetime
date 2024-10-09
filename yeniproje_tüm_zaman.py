import datetime
import pytz

# Tüm zaman dilimleri
tüm_zaman_dilimleri = pytz.all_timezones

# Şu anki zamanı her bir zaman diliminde yazdırılması
for zaman_dilimi_str in tüm_zaman_dilimleri:
    zaman_dilimi = pytz.timezone(zaman_dilimi_str)

    # Zaman diliminde şu anki zamanı alınması
    current_time = datetime.datetime.now(zaman_dilimi)
       
        # Sonuçları yazdırılması
    print(f"Zaman Dilimi: {zaman_dilimi_str} | Şu Anki Zaman: {current_time}")
    

    
    


