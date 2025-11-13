"""
AI-Generated Image Compression Script (Interactive Version)
-----------------------------------------------------------
This script compresses images using the open-source Pillow library in Python.

✅ Features:
- Accepts image path and quality input from the user
- Compresses and saves the result in the same folder
- Maintains attribution to open-source library
- Works for JPEG, PNG, etc.

📜 Attribution:
This program uses the Pillow (PIL) library — MIT License.
Source: https://pillow.readthedocs.io/en/stable/
"""

from PIL import Image
import os

def compress_image(input_path, output_path=None, quality=40):
    """
    Compress an image and save it with reduced quality.
    """
    if not os.path.exists(input_path):
        print("❌ Error: File not found! Please check your path.")
        return

    try:
        # Open the image
        image = Image.open(input_path)

        # Default output path
        if output_path is None:
            filename, ext = os.path.splitext(input_path)
            output_path = f"{filename}_compressed.jpg"

        # Convert RGBA or P to RGB for JPEG format
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")

        # Save the compressed image
        image.save(output_path, "JPEG", optimize=True, quality=quality)

        # Print before & after size
        original_size = os.path.getsize(input_path) / 1024
        compressed_size = os.path.getsize(output_path) / 1024

        print(f"\n✅ Image compressed successfully: {output_path}")
        print(f"📏 Original Size: {original_size:.2f} KB")
        print(f"📉 Compressed Size: {compressed_size:.2f} KB")
        print(f"💡 Compression Quality: {quality}%")

    except Exception as e:
        print(f"⚠ Compression failed: {e}")


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    print("🖼 AI-Based Image Compression Tool")
    print("==================================")

    # Take input from user
    input_path = input("📂 Enter the full path of your image file: ").strip()
    quality_input = input("🎚 Enter compression quality (1–95, default=40): ").strip()

    # Validate and convert quality
    if quality_input.isdigit():
        quality = int(quality_input)
    else:
        quality = 40  # default

    # Call compression function
    compress_image(input_path, quality=quality)