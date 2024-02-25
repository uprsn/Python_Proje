from tradingview_ta import TA_Handler, Interval

#oge = TA_Handler(
#    screener="america", 
#    exchange="NASDAQ",
#    symbol="AAPL",
#    interval=Interval.INTERVAL_1_DAY
#    )
ulkeler = ["turkey","america"]
borsalar = ["BIST", "NASDAQ"]
borsalarSecim = int(input("Türkiye borsası için 1'e , ABD için 2'ye basınız : "))
hisse = input("Hangi hisseyi istiyorsunuz : ")
oge = TA_Handler(
    screener=ulkeler[borsalarSecim-1], 
    exchange=borsalar[borsalarSecim-1],
    symbol= hisse,
    interval=Interval.INTERVAL_1_DAY
    )

indikator = oge.get_analysis().indicators
hareket_Ortalamasi = oge.get_analysis().moving_averages
osilator = oge.get_analysis().oscillators
ozet = oge.get_analysis().summary
data = oge.get_analysis().exchange

print("Tüm indikatör verileri : ",indikator)
print(int(indikator.get('open')))

print("Tüm hareketli ortalama verileri : ",hareket_Ortalamasi)
print("Osilatör verileri : ",osilator)
print("Özet :",ozet)
print("Veri :", data)