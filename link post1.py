print("======RAYSFLORIST====")
print("======WELCOME TO MY GOLDEN  WORLD====")
print("Fresh flowers and Bouquet available herre!")
items={
    "red roses" :400,
    "rose bonquet" :1000,
    "boxed flowers(roses)" :850,
    "lotus" :100,
    "lotus bonquet" :500
    }
print("FLOWERS AND PRICE LIST")
for flower,price in items.items():
    print(f"{items}-RS{price}")
discount=10
total=0
order={}
while True:
    print("Enter the flower name or done):")
    choice=input("enter your order")
    if choice=="done":
        break
    if choice in items:
           try:
              final=int(input("enter your favourite bonquet or flowers quantity"))
              if final <=0:
                print("please enter above 0 flowers")
                continue
              order[choice]=order.get(choice,0)+final
              print("Conform your order")
           except ValueError:
               print("INVAILD QUANTITY!PLEASE ENTER A NUMBER")
    else:
        print("Thanks for you Time ")
for flower,final in order.items():
    total+=items[flower]*final
if total>=500:
    discount1=(discount/100)*total
    amount=total-discount
    print(f"discount applied {discount}%=RS.{discount1}")
else:
    amount=total
    print("NO discount applied(buy more next time)")
print(f"Total money to pay us:{amount}")
print("THANK YOU FOR MORE LOVE FOR US")
print("============================")

