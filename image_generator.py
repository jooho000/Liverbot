import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

def create_welcome_image(username, avatar_url):
    """Generate a personalized welcome image with the user's avatar and name."""

    # Load the new background image
    background = Image.open("welcome_background.jpg")  # Ensure this file exists

    # Fetch and process the user's avatar
    response = requests.get(avatar_url)
    avatar = Image.open(BytesIO(response.content)).convert("RGBA")
    avatar = avatar.resize((150, 150))

    # Create a circular mask for the avatar
    mask = Image.new("L", (150, 150), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 150, 150), fill=255)
    avatar.putalpha(mask)

    # Paste avatar onto the background at a chosen position
    background.paste(avatar, (50, 50), avatar)

    # Add welcome text
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("arial.ttf", 40)  # Ensure this font file exists
    text = f"¡Bienvenido, {username}!"
    text_position = (220, 90)
    draw.text(text_position, text, fill="white", font=font)

    # Save the image to bytes
    image_bytes = BytesIO()
    background.save(image_bytes, format="PNG")
    image_bytes.seek(0)

    return image_bytes
