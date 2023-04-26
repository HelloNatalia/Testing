sentence = input("Podaj jakieś zdanie. Wyświetlę jego słowa w odwrotnej kolejności: ")
sentence = sentence.split(" ")
sentence = sentence[::-1]

reversed = ""
for word in sentence:
    reversed += word + " "

print(reversed)