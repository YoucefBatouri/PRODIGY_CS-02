How It Works
Key Generation:
A fixed key is used to seed a random number generator.
This key generates a key_array with random values that match the size of the image.
Encryption and Decryption:
Encryption: The image is loaded and converted into a numpy array. The key_array is XORed with the image data. This modified data is saved as the encrypted image.
Decryption: The encrypted image is loaded and the same XOR operation is applied using the same key_array to recover the original image.
