import os

JOKE = "I hit Reply All to say ‘Thanks’; by lunch, the thread had elected a chair and scheduled a follow-up."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
