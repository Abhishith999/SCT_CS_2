from PIL import Image

def process_image(image_path: str, output_path: str, key: int) -> None:
    """
    Encrypts or decrypts an image using XOR pixel manipulation.
    Because XOR is a reversible bitwise operation, the exact same logic 
    is used for both encryption and decryption.
    
    Args:
        image_path (str): The file path to the source image.
        output_path (str): The file path where the modified image will be saved.
        key (int): The numerical secret key used for the XOR operation.
    """
    try:
        # 1. Load the image and force it into RGB mode
        img = Image.open(image_path)
        img = img.convert("RGB")
        pixels = img.load()
        
        # Note: 'size' is a property, not a method, so no parentheses!
        width, height = img.size 
        
        # 2. Iterate through every pixel using your nested loops
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                
                # 3. Apply your XOR logic
                new_r = r ^ key
                new_g = g ^ key
                new_b = b ^ key
                
                # Update the pixel
                pixels[x, y] = (new_r, new_g, new_b)
                
        # 4. Save the final image
        img.save(output_path)
        print(f"✅ Success! Image saved to: {output_path}")
        
    except FileNotFoundError:
        print(f"❌ Error: The file '{image_path}' was not found. Please verify the path.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


def main() -> None:
    print("--- Professional Image Encryption Tool ---")
    
    # Force the input to uppercase so 'e' and 'E' both work
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
    
    if choice not in ['E', 'D']:
        print("❌ Invalid choice. Please run the program again.")
        return
        
    action = "encrypt" if choice == 'E' else "decrypt"
    
    image_path = input(f"Enter the path of the image to be {action}ed: ")
    output_path = input(f"Enter the path where the {action}ed image will be saved: ")
    
    # Protect against users typing letters instead of numbers for the key
    try:
        key = int(input("Enter the numerical key: "))
    except ValueError:
        print("❌ Error: The key must be a whole number.")
        return
        
    # Call the single function regardless of E or D
    process_image(image_path, output_path, key)


if __name__ == "__main__":
    main()