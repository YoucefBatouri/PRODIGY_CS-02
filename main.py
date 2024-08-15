import numpy as np
from PIL import Image


def xor_encrypt_decrypt(image_path, key, output_path):
    # Load image and convert to array
    img = Image.open(image_path)
    img_array = np.array(img)

    # Generate a key array based on some pattern or function
    np.random.seed(key)  # Use key to seed random number generator
    key_array = np.random.randint(0, 256, size=img_array.shape, dtype=np.uint8)

    # XOR operation
    encrypted_array = np.bitwise_xor(img_array, key_array)

    # Convert back to image and save
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_path)


if __name__ == "__main__":
    choice = input("Would you like to (E)ncrypt or (D)ecrypt an image? ").strip().lower()
    image_path = input("Enter the path of the image: ")

    key = 192  # Example key, used to seed the random number generator

    if choice == 'e':
        xor_encrypt_decrypt(image_path, key, "encrypted_image.png")
        print("Image encrypted successfully,saved as encrypted_image.png")
    elif choice == 'd':
        xor_encrypt_decrypt("encrypted_image.png", key,
                            "decrypted_image.png")
        print("Image decrypted successfully, saved as decrypted_image.png")
    else:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")
