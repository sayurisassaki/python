# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

h = float(height)
w = int(weight)

# print (type(h))
# print (type(w))

imc= w /(h*h)
imc_int = int(imc)
print (imc_int)