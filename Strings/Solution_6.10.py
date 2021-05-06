#Replacing characters in strings with replace()....

boy = 'Manoj is good boy, Manoj is hard-working, Manoj is graduated in CSE, Manoj loves Python'

new_string = boy.replace('Manoj', "He", 2)

print(new_string)

song = 'Let it be, let it be, let it be, let it be'

# replacing only two occurences of 'let'
print(song.replace('let', "don't let", 2))