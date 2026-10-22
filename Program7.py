s=input("Enter a sentence:")
print(s)
wordsList=s.split()
print(wordsList)
uniqueWord=set(wordsList)
for word in uniqueWord:
    print(f"{word} occurs {wordsList.count{word}} times")
