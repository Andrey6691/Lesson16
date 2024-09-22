def single_root_words(root_word='auto', *other_words):
    root_word.upper()
    other_words = [s.lower() for s in other_words]
    same_words = []
    for word in other_words:
        if root_word in word:
            same_words.append(word)
        continue
    return same_words

result1 = single_root_words('auto', 'automobile', 'autobus', 'lemon', 'aura', 'aut')
result2 = single_root_words('ball', 'minibal', 'basketball', 'balet', 'football')
print(result1)
print(result2)
