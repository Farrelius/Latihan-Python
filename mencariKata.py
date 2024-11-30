def search_word(text, word):
    return text.lower().count(word.lower())

text = input("Masukkan teks: ")
word = input("Masukkan kata yang dicari: ")
count = search_word(text, word)
print(f"Kata '{word}' ditemukan sebanyak {count} kali.")