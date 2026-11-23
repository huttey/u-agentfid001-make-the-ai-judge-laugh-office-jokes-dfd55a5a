import os

JOKE = "The reply-all chain finally stopped when someone replied all: 'Please stop replying all.'"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
