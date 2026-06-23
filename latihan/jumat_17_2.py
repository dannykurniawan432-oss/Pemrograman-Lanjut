try:
    a = 10*"lima"
    raise NameError("error type")
except NameError:
    print("Tipe data error")
    raise