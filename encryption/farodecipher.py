
# Custom script to decrypt the CISO Pharoh Challenge 

'''

The Perfect Pharaoh
cisoCTF{iseshkncudobsytemteigolntetou}

In times past one pharaoh had 27 men two overtake 28.

When the pharaoh finally brought all together, they became a kingdom of 52.

Now YOU present yourself before him to challenge him for his throne.

Will you have what it takes to bring down a faro of his caliber once and for all?

'''

def decipher_string():

    # Set a variable with the ciphered text.
    cipher_text="iseshkncudobsytemteigolntetou"

    # Since the amount of characters are odd, 29 to be exact; Take the two midpoints of the entire string.
    midpoint = len(cipher_text) // 2
    first_half = cipher_text[:midpoint]
    second_half = cipher_text[midpoint:]

    # Take the max length of the two strings to ensure not to run into an index out of bounds error.
    max_length = max(len(first_half), len(second_half))

    # Create an empty string variable for the ciphered text.
    ciphered_text = ""

    i = 0

    # Iterate through each half of the string and append the letter to the ciphered text variable.
    for i in range(max_length):
        if i < len(first_half):
            ciphered_text += first_half[i]
            
        if i < len(second_half):
            ciphered_text += second_half[i]
            
    print(ciphered_text)
      

    
decipher_string()