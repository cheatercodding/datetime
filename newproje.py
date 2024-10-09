
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
kolkata_zaman_dilimi = pytz.timezone(kolkata_zaman_dilimi_str)


# Domain süresi bitiş tarihini string'den datetime nesnesine çevir
domain_suresi_bitis_tarihi = datetime.datetime.strptime(domain_suresi_bitis_tarihi_str, '%Y-%m-%d %H:%M')






