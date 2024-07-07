def vowels(word):
    list_of_vowels = ['a', 'e', 'i', 'o', 'u']
    total_count = len([i for i in word if i.lower() in list_of_vowels])
    return total_count


num = 10000

print(f"{num:,}")

