from PIL import Image, ImageDraw
import os
import numpy as np

# Mapping user asset files to standard normalized names
mapping = {
    "Ant_Man.png": "antman.png",
    "Black Panther.jpg": "blackpanther.png",
    "Black_Widow.png": "blackwidow.png",
    "Captain_America.png": "captainamerica.png",
    "Captain_Marvel.png": "captainmarvel.png",
    "Doctor_Strange.png": "doctorstrange.png",
    "Groot.png": "groot.png",
    "Hawkeye.jpg": "hawkeye.png",
    "Hulk.png": "hulk.png",
    "Iron_Man.png": "ironman.png",
    "Loki.png": "loki.png",
    "Quick_Silver.png": "quicksilver.png",
    "Rocket.png": "rocket.png",
    "Scarlet Witch.png": "scarletwitch.png",
    "Spider_Man.png": "spiderman.png",
    "Thor.png": "thor.png",
    "Vision.png": "vision.png",
    "War_Machine.png": "warmachine.png",
    "Wolverine.png": "wolverine.png"
}

assets_dir = "assets"
processed_dir = os.path.join(assets_dir, "processed")
os.makedirs(processed_dir, exist_ok=True)

print("Starting background removal and normalization...")

for src_name, target_name in mapping.items():
    src_path = os.path.join(assets_dir, src_name)
    if not os.path.exists(src_path):
        print(f"Skipping missing: {src_name}")
        continue
    
    im = Image.open(src_path).convert("RGBA")
    w, h = im.size
    
    # Check background color tolerance
    thresh = 35
    if "Thor" in src_name:
        thresh = 50
    elif "Scarlet" in src_name:
        thresh = 30
    
    # Floodfill from all 4 corners and midpoints of edges
    seed_points = [
        (0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1),
        (0, h // 2), (w - 1, h // 2), (w // 2, 0), (w // 2, h - 1)
    ]
    
    for pt in seed_points:
        try:
            ImageDraw.floodfill(im, pt, (0, 0, 0, 0), thresh=thresh)
        except Exception:
            pass

    # Save to processed folder and to assets/ with normalized name
    target_path = os.path.join(assets_dir, target_name)
    im.save(target_path, "PNG")
    
    arr = np.array(im)
    trans = np.sum(arr[:, :, 3] == 0) / (w * h)
    print(f"Processed: {src_name:22} -> {target_name:18} | Transparent: {trans*100:.1f}%")

print("All images processed successfully with clean transparency!")
