my_sentence = "python is fun and powerful!"
print(len(my_sentence))

print(my_sentence[0])

substring = my_sentence[10:25]

print(substring)

print(my_sentence.lower())

print(my_sentence.count('o'))

index_of_fun = my_sentence.index("fun")

print(index_of_fun)

new_sentence = my_sentence.replace("powerful", "amazing")

print(new_sentence)

new_message = "Learning Python is exciting!"

concat_plus = my_sentence + ", " + new_message

print(concat_plus)

concat_format = "{} {}".format(my_sentence, new_message)

print(concat_format)

concat_fstring = f"{my_sentence} {new_message}"

print(concat_fstring)

print(dir(my_sentence))

help(str.replace)
