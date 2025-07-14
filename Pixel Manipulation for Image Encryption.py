Run the following command in your command prompt to install Pillow:
pip install pillow
.
.
.
.
Once Pillow is installed, you can run the script:

from PIL import Image
import random

def encrypt(image_name, key):
    try:
        image = Image.open(image_name)
        new_image = image.copy()
        pixels = new_image.load()
        
        w, h = image.size
        random.seed(key)
        
        for i in range(w):
            for j in range(h):
                x = random.randint(0, w - 1)
                y = random.randint(0, h - 1)
                pixels[i, j], pixels[x, y] = pixels[x, y], pixels[i, j]

        encrypted_image_name = "encrypted_" + image_name
        new_image.save(encrypted_image_name, format="png")
        print(f"Encryption done. Saved as {encrypted_image_name}")
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt(enc_image, key):
    try:
        image = Image.open(enc_image)
        new_image = image.copy()
        pixels = new_image.load()
        
        w, h = image.size
        random.seed(key)
        swaps = []
        
        for i in range(w):
            for j in range(h):
                x = random.randint(0, w - 1)
                y = random.randint(0, h - 1)
                swaps.append(((i, j), (x, y)))

        for (i, j), (x, y) in reversed(swaps):
            pixels[i, j], pixels[x, y] = pixels[x, y], pixels[i, j]

        decrypted_image_name = "decrypted_" + enc_image
        new_image.save(decrypted_image_name, format="png")
        print(f"Decryption done. Saved as {decrypted_image_name}")
    except Exception as e:
        print(f"Error during decryption: {e}")

def main():
    while True:
        print("1. Encryption \n2. Decryption \n\n99. Exit")
        try:
            to_do = int(input("What do you want to do? "))

            if to_do == 1:
                image_name = input("Enter the image name: ")
                key = int(input("Enter the encryption key (integer): "))
                encrypt(image_name, key)

            elif to_do == 2:
                image_name = input("Enter the encrypted image name: ")
                key = int(input("Enter the decryption key (same as encryption key): "))
                decrypt(image_name, key)

            elif to_do == 99:
                break

            else:
                print("Wrong Input....")
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        print("\n\n")

if __name__ == "__main__":
    main()