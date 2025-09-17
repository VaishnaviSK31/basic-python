def print_msg():
    msg="Hello Everyone"
    return msg
def outer(print1):
    print("Entering outer")

    def inner():
        print("Entering inner")
        ref1=print1
        msg2=ref1()
        new_v=msg2.upper()
        print(new_v)
        print("Leaving inner")
    return inner
ref2=outer(print_msg)
ref2()