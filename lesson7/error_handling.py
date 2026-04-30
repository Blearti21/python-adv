
numri1 = 10

numri2=0

try:
    rezultati = numri1/numri2

except ZeroDivisionError:
    print("hejj nuk munesh me pjestu me 000")



numri4 =20

numri5=2

try:
    rezultati = numri4/numri5

except ZeroDivisionError:
    print("Hejj nuk munesh me pjestu me 000")
else:
    print("pjestimi esht i pranueshem")

mesazhi = "hello"
try:
    textToInt = int(mesazhi)
except Exception as e:
    print("ka ndodh nje error",e)


def divide_numbers(a,b):
    try:
        resultat = a/b
        print("rezultati eshte :",resultat)
    except ZeroDivisionError:
        print("hej ke tentu me pjestu me 0")
    except TypeError:
        print("Invalid type for division")
    except Exception as a:
        print("Ka ndodh nje error",a)



divide_numbers(10,2)
divide_numbers(10,0)
divide_numbers(10,"absf")