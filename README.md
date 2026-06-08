# Image Encryption Tool using Pixel Manipulation

## Overview

This project is a simple Image Encryption and Decryption Tool developed using Python and the Pillow (PIL) library. The tool secures images by applying XOR-based pixel manipulation techniques to every pixel in the image.

The same operation is used for both encryption and decryption because XOR is a reversible operation.

---

## Features

* Encrypt images using XOR pixel manipulation
* Decrypt encrypted images using the same secret key
* Supports RGB image processing
* User-friendly command-line interface
* Error handling for invalid file paths and keys

---

## Technologies Used

* Python 3
* Pillow (PIL) Library

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Abhishith999/SCT_CS_2
cd SCT_CS_2
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How the Encryption Works

Each pixel in the image contains RGB values.

The program performs an XOR operation between each RGB value and the user-provided secret key.

Example:

```python
new_r = r ^ key
new_g = g ^ key
new_b = b ^ key
```

Because XOR is reversible:

* Applying the same key again decrypts the image
* The original image is restored

---

## Project Structure

```plaintext
image-encryption-tool/
│
├── image_encryption.py
├── README.md
├── input_images/
├── output_images/
```

---

## Usage

### Run the Program

```bash
python image_encryption.py
```

### Choose Operation

```plaintext
Enter 'E' for encryption or 'D' for decryption
```

### Provide:

* Input image path
* Output image path
* Numerical secret key

---

## Example

### Encryption

```plaintext
Enter 'E' for encryption or 'D' for decryption: E
Enter the path of the image to be encrypted: input.jpg
Enter the path where the encrypted image will be saved: encrypted.jpg
Enter the numerical key: 45
```

### Decryption

```plaintext
Enter 'E' for encryption or 'D' for decryption: D
Enter the path of the image to be decrypted: encrypted.jpg
Enter the path where the decrypted image will be saved: decrypted.jpg
Enter the numerical key: 45
```

---

## Error Handling

The program handles:

* Invalid file paths
* Incorrect key input
* Unexpected runtime errors

---

## Learning Outcomes

Through this project, the following concepts were learned:

* Image processing using Pillow
* Pixel manipulation techniques
* XOR encryption logic
* File handling in Python
* Exception handling
* Command-line interaction

---

## Future Improvements

* GUI-based interface
* Multiple encryption algorithms
* Password-based key generation
* Drag-and-drop image support
* Batch image encryption

---

## Author

Developed as part of the Cyber Security Internship Program at SkillCraft Technology.

---
