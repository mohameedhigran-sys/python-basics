#  10.5 حساب الاجر الاسبوعي اذا كان 40 او اقل نحسب حساب الاجر الاعتيادي الي هو 
# اذا كان اكثر من 40 نحسب الزايد اب 1.5 من الاجر الاصلي
hrs = input("enter hours: ")
rate = input("enter rate: ")
h = float(hrs)
r = float(rate)
if h <= 40 :
    #الاجر نكتبه pay
    pay = (h * r)
else :
    pay = (r * 40 + (h - 40) * r * 1.5)
print (pay)