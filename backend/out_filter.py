"""
Clueless Outfit Maker - Steps A and B (filter + combination generator)

Step A: filter_items()      -> remove clothes that don't fit the weather/preferences
Step B: generate_outfits()  -> build every valid top + bottom + shoes (+ outerwear)

Saahir's scoring code takes the list that generate_outfits() returns.
"""
from itertools import product

# ---------- FAKE DATA (swap for SQL / weather API later) ----------
# warmth: 1 = very light, 5 = very warm
WARDROBE = [
    {"id": 1,  "name": "White tee",          "category": "top",       "color": "white", "warmth": 1, "waterproof": False, "style": "casual"},
    {"id": 2,  "name": "Black tank",         "category": "top",       "color": "black", "warmth": 1, "waterproof": False, "style": "casual"},
    {"id": 3,  "name": "Striped long sleeve","category": "top",       "color": "navy",  "warmth": 3, "waterproof": False, "style": "casual"},
    {"id": 4,  "name": "Cream sweater",      "category": "top",       "color": "cream", "warmth": 4, "waterproof": False, "style": "casual"},
    {"id": 5,  "name": "Button-up shirt",    "category": "top",       "color": "blue",  "warmth": 2, "waterproof": False, "style": "formal"},
    {"id": 6,  "name": "Blue jeans",         "category": "bottom",    "color": "blue",  "warmth": 3, "waterproof": False, "style": "casual"},
    {"id": 7,  "name": "Black skirt",        "category": "bottom",    "color": "black", "warmth": 1, "waterproof": False, "style": "casual"},
    {"id": 8,  "name": "Khaki trousers",     "category": "bottom",    "color": "beige", "warmth": 3, "waterproof": False, "style": "formal"},
    {"id": 9,  "name": "Denim shorts",       "category": "bottom",    "color": "blue",  "warmth": 1, "waterproof": False, "style": "casual"},
    {"id": 10, "name": "White sneakers",     "category": "shoes",     "color": "white", "warmth": 2, "waterproof": False, "style": "casual"},
    {"id": 11, "name": "Rain boots",         "category": "shoes",     "color": "black", "warmth": 3, "waterproof": True,  "style": "casual"},
    {"id": 12, "name": "Sandals",            "category": "shoes",     "color": "brown", "warmth": 1, "waterproof": False, "style": "casual"},
    {"id": 13, "name": "Rain jacket",        "category": "outerwear", "color": "green", "warmth": 2, "waterproof": True,  "style": "casual"},
    {"id": 14, "name": "Puffer coat",        "category": "outerwear", "color": "black", "warmth": 5, "waterproof": False, "style": "casual"},
    {"id": 15, "name": "Denim jacket",       "category": "outerwear", "color": "blue",  "warmth": 2, "waterproof": False, "style": "casual"},
]

WEATHER = {"feels_like" : 45, "rain_chance": 70, "wind_speed" : 12}
PREFERENCES = {"excluded_ids" : [], "occasion": "casual"}

#helper methods 
def target_warmth(feels_like):
    """Convert feels-like temp (F) to the warmth level the outfit should have."""
    if feels_like >= 80: return 1 
    if feels_like >= 70: return 2
    if feels_like >= 55: return 3 
    if feels_like >= 40: return 4

    return 5


def needs_outerwear(weather):
    return (weather["feels_like"] < 60)
        #or weather["rain_chance"] >= 40 
    

