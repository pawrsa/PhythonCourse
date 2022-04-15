string = input('matn ra vared konid: ')
shift = int(input('meghdare shift ra vared konid: '))


text = ''
for ch in string:
    if('a'<=ch<='z'):
        letter = chr((ord(ch) + shift - 97) % 26 + 97)
    else:
        letter = chr((ord(ch) + shift-65) % 26 + 65)
    text += letter

print(text)


