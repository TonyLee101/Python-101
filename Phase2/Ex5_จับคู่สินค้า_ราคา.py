#จับคู่สินค้าและราคา

fruit=["มะม่วงดอง","แตงโมปั่น","ฝรั่งแช่บ๊วย"]
price=["50","30","15"]

for x,y in zip(fruit,price):
    print(x, "ราคา ",y)

print("")

for x,y in zip(fruit,price[::-1]):
    print(x, "ราคา ",y)
