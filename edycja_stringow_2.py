"""name = input("Podaj swoje imię ")
surname = input("Podaj swoje nazwisko ")
phone = input("Podaj swój numer telefonu ")
print (name.isalpha())
print (surname.isalpha())
print (phone.isdigit())
name = name.capitalize()
print (name)
surname = surname.capitalize()
print (surname)
phone = phone.replace(" ","")
print (phone)
phone = phone.replace("-","")
print (phone)
print (name.endswith("a"))
personal = name + " " + surname + " " + phone
print (personal)
len(personal)"""
p = 0
personal = "Piotr Machnik 405405060"
for i in personal:
    if i.isdigit:
        print(i)
        p +=1
        print (p)
print (p)
print (len(personal))
