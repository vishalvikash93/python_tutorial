sentence = input("enter the sentence: ")
word = input("enter the word to find: ")

if word in sentence:
    updated_sentence = sentence.replace(word, "Python")
    print("updated sentence:", updated_sentence)
else:
    print("word not found")
