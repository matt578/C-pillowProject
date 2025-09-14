from PIL import Image, ImageDraw, ImageFont

# === SETTINGS ===
width, height = 700, 700
use_background_image = True   # Change to False if you want solid color
bg_color = "#1e1e2f"          # Used only if use_background_image = False
background_image_path = "images-Z-PkPJp1v-transformed.jpeg"  # Your background image file



# === CREATE POSTER CANVAS ===
if use_background_image:
    try:
        poster = Image.open(background_image_path).convert("RGB")
        poster = poster.resize((width, height))  # resize background to fit
    except FileNotFoundError:
        print(f"⚠️ Background image not found: {background_image_path}, using solid color instead.")
        poster = Image.new("RGB", (width, height), bg_color)
else:
    poster = Image.new("RGB", (width, height), bg_color)

draw = ImageDraw.Draw(poster)

# === FONTS ===
try:
    title_font = ImageFont.truetype("arial.ttf", 70)
    slogan_font = ImageFont.truetype("arial.ttf", 40)
    footer_font = ImageFont.truetype("arial.ttf", 28)
except:
    title_font = ImageFont.load_default()
    slogan_font = ImageFont.load_default()
    footer_font = ImageFont.load_default()



# === ADD CUSTOM IMAGES (YOU DECIDE LAYOUT) ===
# Replace these paths with your own images
image_paths = [
    
    "winner-chicken-dinner-cool-gaming-600w-1667196991-removebg-preview.png",
    "wmremove-transformed-removebg-preview.png"
       
    
]

# Example positions — adjust freely to design your own layout
positions = [
    
    (90, 50),
    (60, 150)
    
    
]

for i, path in enumerate(image_paths):
    try:
        img = Image.open(path).convert("RGBA")
        img = img.resize((550, 550))  # resize for uniformity
        poster.paste(img, positions[i], img)
    except FileNotFoundError:
        print(f"⚠️ Image not found: {path}")



# === SAVE & SHOW ===
poster.save("BSCS-4_DajaoMattAndraeMalanog.png")
poster.show()
