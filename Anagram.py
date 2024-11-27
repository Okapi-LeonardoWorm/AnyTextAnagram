from random import sample


def splitWords(text:str) -> list[str]:
    return text.split(" ")


def anagram(word:str) -> str:
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


def main(text:str, printResults:bool=False) -> str:
    wl = splitWords(text)
    at = ""
    for w in wl:
        at = at+anagram(w)
    
    if printResults:
        print(f"\n\nOriginal:\n{text}\n")
        print(f"Anagram:\n{at}\n\n")
    
    return at


if __name__ == "__main__":
    main(input("Enter text: "))
