a = int(input("Diga um valor : "))
b = int(input("Diga um valor : "))
c = int(input("Diga um valor : "))

if a>=b>=c:
     print(f"{c} {b} {a}")
elif a>=c>=b:
     print(f"{b} {c} {a}")
elif c>=b>=a:
    print(f"{a} {b} {c}")
elif c>=a>=b:
    print(f"{b} {a} {c}")
elif b>=c>=a:
     print(f"{a} {c} {b}")
elif b>=a>=c:
     print(f"{c} {a} {b}")