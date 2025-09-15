def outer():
    print("Entering outer")

    def inner():
        print("Entering inner")
        print("Processing")
        print("Leaving inner")
    return inner
ref=outer()
print("After executing outer")
ref()
print("After executing inner using ref")