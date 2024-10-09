
import datetime
import pytz


# Zaman dilimi tanımlamaları
utc_zaman_dilimi_str = 'UTC'
turkiye_zaman_dilimi_str = 'Europe/Istanbul'
new_york_zaman_dilimi_str = 'America/New_York'
tokyo_zaman_dilimi_str = 'Asia/Tokyo'
domain_suresi_bitis_tarihi_str = "2024-10-04 10:00"

# Zaman dilimlerini oluşturulması
utc_zaman_dilimi = pytz.timezone(utc_zaman_dilimi_str)
turkiye_zaman_dilimi = pytz.timezone(turkiye_zaman_dilimi_str)
new_york_zaman_dilimi = pytz.timezone(new_york_zaman_dilimi_str)
tokyo_zaman_dilimi = pytz.timezone(tokyo_zaman_dilimi_str)



# Domain süresi bitiş tarihini string'den datetime nesnesine çevir
domain_suresi_bitis_tarihi = datetime.datetime.strptime(domain_suresi_bitis_tarihi_str, '%Y-%m-%d %H:%M')


# Domain bitiş tarihini UTC zaman diliminde ayarla
domain_suresi_bitis_utc = utc_zaman_dilimi.localize(domain_suresi_bitis_tarihi)



# Farklı zaman dilimlerine çevir
domain_suresi_bitis_turkiye = domain_suresi_bitis_utc.astimezone(turkiye_zaman_dilimi)
domain_suresi_bitis_new_york = domain_suresi_bitis_utc.astimezone(new_york_zaman_dilimi)
domain_suresi_bitis_tokyo = domain_suresi_bitis_utc.astimezone(tokyo_zaman_dilimi)

# Sonuçları ekrana yazdır
print(f"Domain Süresi Bitiş Tarihi (UTC): {domain_suresi_bitis_utc}")
print(f"Domain Süresi Bitiş Tarihi (Türkiye): {domain_suresi_bitis_turkiye}")
print(f"Domain Süresi Bitiş Tarihi (New York): {domain_suresi_bitis_new_york}")
print(f"Domain Süresi Bitiş Tarihi (Tokyo): {domain_suresi_bitis_tokyo}")











