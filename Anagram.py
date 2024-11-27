from random import sample


def splitWords(text):
    return text.split(" ")


def anagram(word):
    if len(word) < 2:
        return f"{word} "
    if len(word) == 2:
        return f"{word[1]}{word[0]} "
    else:
        size = len(word)
        l = [v for v in range(size)]
        sl = sample(l, size)
        a = ""
        for i in sl:
            a = a+f"{word[i]}"
        
        return f"{a} "


def main(text):
    print(f"\n\nOriginal:\n{text}\n")
    wl = splitWords(text)
    at = ""
    for w in wl:
        at = at+anagram(w)
    
    print(f"Anagram:\n{at}\n\n")
    return at


text = "Abelha é um inseto"

main(text)