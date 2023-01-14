letters="abcdefghijklmnopqrstuvwxyz"
#Caesar cypher encoder
def encode_text(input_text, offset):
  encoded_text = ""
  for c in input_text:
    if c in letters:
      position = letters.find(c)
      new_pos = (position - offset) % 26
      new_char = letters[new_pos]
      encoded_text += new_char
    else:
      encoded_text += c
  return encoded_text

#Caesar cypher decoder
def decode_text(input_text, offset):
  decoded_text = ""
  for c in input_text:
    if c in letters:
      position = letters.find(c)
      new_pos = (position + offset) % 26
      new_char = letters[new_pos]
      decoded_text += new_char
    else:
      decoded_text += c
  return decoded_text

input_text = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

decoded_text = decode_text(input_text, 10)
print(decoded_text)

encoded_text = encode_text("bcd", 10)
print(encoded_text)


