d_e = {
    "milk": "moo",
    "I": "Me",
    "want": "tu-tu"
}

s = "I want milk!"

translation = ""

for w in s.split():

    print(w)

    if w in d_e.keys():
        translation+=d_e[w]+" "
    else:
        translation += w

print(" ".join(translation))
