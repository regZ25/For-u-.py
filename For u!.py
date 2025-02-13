import streamlit as st
import random

# List of motivational messages
messages = [
    "You're like a tiny spark—small but powerful enough to light up the darkest days!✨",
    "Keep going! Even turtles win the race when they don’t stop.🐢💖",
    "You’re a cupcake in a world full of muffins—sweet, special, and totally unique!🧁💕",
    "Every little step you take is still progress. Keep moving forward! 🚶‍♂️💫",
    "You shine so bright, even the stars get jealous!🌟💖",
    "Mistakes are just proof that you’re trying, and trying is already winning!🏆💖",
    "The world needs your magic, so never stop being you!✨🦄",
    "Even the strongest trees started as tiny seeds. Keep growing!🌱🌳",
    "Your heart is a garden—keep planting kindness, and soon, everything will bloom!🌸💖",
    "You are more amazing than a panda riding a unicorn!🐼🦄💫",
    "Believe in yourself like I believe in you (which is A LOT)💕🙌!",
    "You don’t have to be perfect to be incredible—just be YOU!🌟💖",
    "You're like sunshine on a rainy day—so warm and full of light!☀️🌧️",
    "Big dreams start with small steps, so keep stepping forward!🚀💖",
    "You are someone's reason to smile today—keep being wonderful!😊💛",
    "Every time you feel like giving up, remember why you started!💪💖",
    "You are braver than a lion and stronger than your morning coffee!🦁☕💖",
    "A bad day doesn’t mean a bad life—tomorrow is a new start!🌈💖",
    "You are growing and glowing, even if you don’t see it yet!✨🌿",
    "Don't be afraid to take up space—you deserve to shine!💖🌟",
    "You are a masterpiece in progress—every stroke makes you more beautiful!🎨💖",
    "You are enough, just as you are—no changes needed!💕💖",
    "The best things take time, and you are one of them!⏳💖",
    "Be like a sunflower—always turn towards the light!🌻☀️",
    "You’re not alone; even the moon needs the stars to shine!🌙✨",
    "If the caterpillar stopped trying, it would never become a butterfly! 🐛🦋",
    "Your kindness makes the world a better place—never stop sharing it!💕🌍",
    "Your story is still being written, and I can’t wait to see how amazing it turns out! 📖💖",
    "Life is tough, but so are you—keep being the fighter you are!💪💖",
    "You are loved, you are valued, and you are truly special!💖✨"
]

# Streamlit UI
st.set_page_config(page_title="Cute Motivational Messages", page_icon="💖")

st.title("Click Me! uwu <3 🌟💖")

if st.button("Click Me!"):
    st.subheader(random.choice(messages))
