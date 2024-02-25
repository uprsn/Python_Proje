from tradingview_ta import TA_Handler, Interval

#oge = TA_Handler(
#    screener="america", 
#    exchange="NASDAQ",
#    symbol="AAPL",
#    interval=Interval.INTERVAL_1_DAY
#    )
ulkeler = ["turkey","america"]
borsalar = ["BIST", "NASDAQ"]
borsalarSecim1 = int(input("Birinci hisse için borsa seçiniz; Türkiye borsası için 1'e , ABD için 2'ye basınız : "))
hisse1 = input("Birinci hisse ne olsun : ")
oge1 = TA_Handler(
    screener=ulkeler[borsalarSecim1-1], 
    exchange=borsalar[borsalarSecim1-1],
    symbol= hisse1,
    interval=Interval.INTERVAL_1_DAY
    )

borsalarSecim2 = int(input("İkinci hisse için borsa seçiniz; Türkiye borsası için 1'e , ABD için 2'ye basınız : "))
hisse2 = input("İkinci hisse ne olsun : ")
oge2 = TA_Handler(
    screener=ulkeler[borsalarSecim2-1], 
    exchange=borsalar[borsalarSecim2-1],
    symbol= hisse2,
    interval=Interval.INTERVAL_1_DAY
    )

#  Birinci hisse için veriler çekiliyor
indikator1 = oge1.get_analysis().indicators
hareket_Ortalamasi1 = oge1.get_analysis().moving_averages
osilator1 = oge1.get_analysis().oscillators
ozet1 = oge1.get_analysis().summary
data1 = oge1.get_analysis().exchange


#  İkinci hisse için veriler çekiliyor
indikator2 = oge2.get_analysis().indicators
hareket_Ortalamasi2 = oge2.get_analysis().moving_averages
osilator2 = oge2.get_analysis().oscillators
ozet2 = oge2.get_analysis().summary
data2 = oge2.get_analysis().exchange

print("Tüm indikatör verileri : ",indikator1)
print(int(indikator1.get('open')))

print("Tüm hareketli ortalama verileri : ",hareket_Ortalamasi1)
print("Osilatör verileri : ",osilator1)
print("Özet :",ozet1)
print("Veri :", data1)

print("1. Hisse\t\t\t","2.Hisse")

for key in indikator1.keys():
#    print (indikator1.keys(key),"\t\t",indikator2.keys(key))
    print (indikator1.get(key), "\t\t\t", indikator2.get(key))