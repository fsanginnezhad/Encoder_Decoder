def rot13(text: str):
    translate_char = text.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    )
    return text.translate(translate_char)


while True:
    text = input("Enter Your Text: ")
    if text.lower() in ['q', 'e', 'exit', 'quit']:
        text1 = input("Are You Sure to EXIT? ")
        if text1.lower() in ['y', 'yes']:
            break
        else:
            print(rot13(text))
    else:
        print(rot13(text))
