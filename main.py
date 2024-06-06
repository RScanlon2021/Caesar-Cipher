def caesar_cipher_encrypt(text, shift):
  encrypted_text = ""
  for char in text:
      if char.isalpha():
          # Determine whether the character is uppercase or lowercase
          if char.isupper():
              # Encrypt uppercase letters
              encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
          else:
              # Encrypt lowercase letters
              encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
      else:
          # If the character is not a letter, leave it unchanged
          encrypted_text += char
  return encrypted_text + '!'

password = caesar_cipher_encrypt('MyMothersNameIsBridie',3)
# password = caesar_cipher_encrypt('MyFathersNameIsTom',3)
# password = caesar_cipher_encrypt('GemmaMarriedMeInSeptember',3)

print(password)