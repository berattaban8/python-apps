print("""****************
1: +
2: -
3: *
4: /
****************""")

a = int(input("First one: "))
b = int(input("Second one: "))
result = input("choose a number: ")

if result == "1":
    print("Here is your result: {}".format(a+b))
elif result =="2":
    print("Here is your result: {}".format(a-b))
elif result =="3":
        print("Here is your result: {}".format(a*b))
elif result =="4":
         print("Here is your result: {}".format(a/b))
else:
      print("Unknown value")