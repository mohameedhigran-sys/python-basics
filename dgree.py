#هذا المشروع يعادل درجتك بل امتحان عل احرب الانكليزيه 
score = input("enter your score: ")
#الي راح اسوي هسه اذا دخل اليوزر غسر شي هن الي الي اريده البرنمج يطلع  حتى ليسووي ايرور
try :
    s = float(score)
except:
    print ("BAD ENTER")
    quit()
if s <0.0 or s > 1.0 :
    print("Bad Score!!!")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print ("B")
elif s >=0.7:
    print ("C")
elif s >= 0.6 :
    print ("D")
elif s >= 0.5:
    print ("F")
else :
    print ("You are a dog shit ")