# # 1 - misol
# from collections import namedtuple
# Sportchilar = namedtuple('sportchi', ['ismi', 'sport_turi', 'yutuqlari'])
# sportchilar = [
#     Sportchilar(ismi='ali', sport_turi='tennis', yutuqlari=8),
#     Sportchilar(ismi='bilol', sport_turi='boks', yutuqlari=23),
#     Sportchilar(ismi='sadir', sport_turi='ufc', yutuqlari=23),
#     Sportchilar(ismi= 'Messi', sport_turi='futbol', yutuqlari=7),
#     Sportchilar(ismi='CRonaldo', sport_turi='futbol', yutuqlari=78),
# ]
# kuchli = max(sportchilar, key=lambda sportchi: sportchi.yutuqlari)
# print(f"Yutuqlari eng kop sportchi {kuchli.ismi} {kuchli.yutuqlari} yutuqlari.")

# 2-misol
# my_list = [1, 2, 3, 4,354,5657,124]
# ortacha_qimat=sum(my_list)/len(my_list)
# print(ortacha_qimat)


# 3 - masala
# numbers = range(1, 11)
# squares = (n**2 for n in numbers)
# for square in squares:
#     print(square)

# 4-misol
# text =str(input("soz kirt"))
# unliy_harv = "aeiouAEIOU"
# unliy = [harf for harf in text if harf in unliy_harv]
# print(unliy)

# 5-misol
# def juft_sonlar(limit):
#     for a in range(2, limit + 1, 2):
#         yield a
# for juft in juft_sonlar(100):
#     print(juft)

# 6-misol
# def uzunligi():
#     def a(s):
#         return len(s)
#     return a
#
# uzunligini_olchandi = uzunligi()
# print(uzunligini_olchandi("dfghjkfdfgjghfffl;"))



