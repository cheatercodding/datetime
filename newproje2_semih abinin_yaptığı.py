import datetime
import pytz

# Zaman dilimi tanımlamaları
utc_timezone_str = 'UTC'
turkey_timezone_str = 'Europe/Istanbul'
domain_expire_date_str = "2024-10-04 10:00"

# Zaman dilimlerini oluştur
utc_timezone = pytz.timezone(utc_timezone_str)
turkey_timezone = pytz.timezone(turkey_timezone_str)

# Domain süresi bitiş tarihini string'den datetime nesnesine çevir
domain_expire_date = datetime.datetime.strptime(domain_expire_date_str, '%Y-%m-%d %H:%M')

# Domain bitiş tarihini UTC zaman diliminde ayarla
domain_expire_date_utc = utc_timezone.localize(domain_expire_date)


# UTC olan tarihi Türkiye zaman dilimine çevir
domain_expire_date_turkey = domain_expire_date_utc.astimezone(turkey_timezone)

