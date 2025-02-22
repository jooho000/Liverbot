import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os

def create_welcome_image(username, avatar_url):
    """Generate a personalized welcome image with the user's avatar and name."""

    # Ensure the correct path to the background image
    background_path = os.path.join("data", "welcome_background.jpg")  

    if not os.path.exists(background_path):
        raise FileNotFoundError(f"❌ Error: {background_path} no encontrado. Verifica que la imagen esté en la carpeta 'data/'.")

    # Load the background image
    background = Image.open(background_path)
    bg_width, bg_height = background.size  # Get background dimensions

    # Fetch and process the user's avatar
    try:
        if avatar_url.startswith("file://"):  # Handle local images
            avatar_path = avatar_url.replace("file://", "")
            avatar = Image.open(avatar_path).convert("RGBA")
        else:
            response = requests.get(avatar_url, timeout=5)
            response.raise_for_status()
            avatar = Image.open(BytesIO(response.content)).convert("RGBA")

    except (requests.exceptions.RequestException, Image.UnidentifiedImageError, FileNotFoundError):
        print(f"⚠️ Error loading avatar for {username}, using default image.")
        avatar = Image.open("data/welcome_background.jpg").convert("RGBA")  # Use welcome background as fallback

    # Resize avatar (increase size)
    avatar_size = int(bg_width * 0.3)  # 30% of background width
    avatar = avatar.resize((avatar_size, avatar_size))

    # Create a circular mask for the avatar
    mask = Image.new("L", (avatar_size, avatar_size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, avatar_size, avatar_size), fill=255)
    avatar.putalpha(mask)

    # Paste avatar onto the background (centered)
    avatar_x = (bg_width - avatar_size) // 2
    avatar_y = int(bg_height * 0.2)  # Position avatar slightly above center
    background.paste(avatar, (avatar_x, avatar_y), avatar)

    # Add welcome text
    draw = ImageDraw.Draw(background)

    # Try different fonts based on OS
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Linux
    if os.name == "nt":  # Windows
        font_path = "C:/Windows/Fonts/Arial.ttf"

    try:
        font = ImageFont.truetype(font_path, int(bg_width * 0.08))  # Adjust text size dynamically
    except:
        raise FileNotFoundError(f"⚠️ Font not found: {font_path}")

    text = f"¡Bienvenido, {username}!"
    
    # Get text size correctly using textbbox()
    text_bbox = draw.textbbox((0, 0), text, font=font)  # Get bounding box
    text_width = text_bbox[2] - text_bbox[0]  # Width = right - left
    text_height = text_bbox[3] - text_bbox[1]  # Height = bottom - top

    # Center text
    text_x = (bg_width - text_width) // 2
    text_y = avatar_y + avatar_size + 20  # Below avatar
    draw.text((text_x, text_y), text, fill="white", font=font)

    # Save the image to bytes
    image_bytes = BytesIO()
    background.save(image_bytes, format="PNG")
    image_bytes.seek(0)

    return image_bytes
