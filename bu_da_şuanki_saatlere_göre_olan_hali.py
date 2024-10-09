import datetime
import pytz


# Zaman dilimi tanımlamalanması
utc_timezone_str = 'UTC'
turkey_timezone_str = 'Europe/Istanbul'
new_york_zaman_dilimi_str = 'America/New_York'


# Zaman dilimlerini oluşturulması
utc_timezone = pytz.timezone(utc_timezone_str)
turkey_timezone = pytz.timezone(turkey_timezone_str)
new_york_zaman_dilimi = pytz.timezone(new_york_zaman_dilimi_str)


# Şu anki zamanı al ve UTC zaman diliminde ayarlanması
current_time = datetime.datetime.now()
current_time_utc = utc_timezone.localize(current_time)

# UTC olan zamanı Türkiye ve New York zaman dilimlerine çevrilmesi
current_time_turkey = current_time_utc.astimezone(turkey_timezone)
current_time_new_york = current_time_utc.astimezone(new_york_zaman_dilimi)






