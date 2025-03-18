# services/interpretation.py

SYMBOL_DICTIONARY = {
    "water": {
        "meaning": "Represents emotions, spirituality, and cleansing.",
        "scripture": ["John 4:14", "Isaiah 12:3", "Revelation 22:1"]
    },
    "fire": {
        "meaning": "Symbolizes purification, transformation, or divine judgment.",
        "scripture": ["Exodus 3:2", "1 Corinthians 3:13", "Hebrews 12:29"]
    },
    "light": {
        "meaning": "Represents divine guidance, wisdom, and revelation.",
        "scripture": ["Matthew 5:14", "John 8:12", "Psalm 119:105"]
    },
    "snake": {
        "meaning": "Symbolizes wisdom, danger, or deception.",
        "scripture": ["Genesis 3:1", "Numbers 21:9", "Matthew 10:16"]
    },
    "tree": {
        "meaning": "Represents growth, stability, and divine connection.",
        "scripture": ["Psalm 1:3", "Revelation 22:2", "Matthew 13:32"]
    },
    "lion": {
        "meaning": "Symbolizes strength, courage, and authority.",
        "scripture": ["Revelation 5:5", "Proverbs 28:1", "Judges 14:8"]
    },
    "bread": {
        "meaning": "Represents provision, the Word of God, and sustenance.",
        "scripture": ["John 6:35", "Matthew 4:4", "Exodus 16:15"]
    },
    "storm": {
        "meaning": "Symbolizes trials, challenges, or divine intervention.",
        "scripture": ["Matthew 8:24-26", "Psalm 107:29", "Nahum 1:3"]
    },
    "gold": {
        "meaning": "Represents divine purity, wisdom, and heavenly wealth.",
        "scripture": ["Job 23:10", "Revelation 3:18", "1 Peter 1:7"]
    },
    "path": {
        "meaning": "Symbolizes life’s journey, direction, and God’s guidance.",
        "scripture": ["Psalm 119:105", "Proverbs 3:6", "Matthew 7:14"]
    },
    "blood": {
        "meaning": "Represents life, sacrifice, and redemption.",
        "scripture": ["Leviticus 17:11", "Hebrews 9:22", "Matthew 26:28"]
    },
    "door": {
        "meaning": "Symbolizes opportunity, transition, or Christ Himself.",
        "scripture": ["John 10:9", "Revelation 3:8", "Matthew 7:7-8"]
    },
    "mountain": {
        "meaning": "Represents divine presence, revelation, and spiritual elevation.",
        "scripture": ["Exodus 19:20", "Matthew 17:1-3", "Psalm 121:1"]
    },
    "rock": {
        "meaning": "Symbolizes strength, stability, and God as our foundation.",
        "scripture": ["Psalm 18:2", "1 Corinthians 10:4", "Matthew 16:18"]
    },
    "olive": {
        "meaning": "Represents peace, anointing, and God's provision.",
        "scripture": ["Psalm 52:8", "Zechariah 4:3", "Romans 11:17"]
    },
    "crown": {
        "meaning": "Symbolizes authority, victory, and divine reward.",
        "scripture": ["2 Timothy 4:8", "James 1:12", "Revelation 2:10"]
    },
    "shepherd": {
        "meaning": "Represents guidance, care, and Christ as the Good Shepherd.",
        "scripture": ["Psalm 23:1", "John 10:11", "Ezekiel 34:15"]
    },
    "wine": {
        "meaning": "Symbolizes joy, covenant, and spiritual blessing.",
        "scripture": ["John 2:10", "Matthew 26:27-29", "Proverbs 3:10"]
    },
    "harvest": {
        "meaning": "Represents blessing, divine timing, and the gathering of souls.",
        "scripture": ["Matthew 9:37", "Galatians 6:9", "Joel 3:13"]
    },
    "rain": {
        "meaning": "Symbolizes divine blessing, restoration, and cleansing.",
        "scripture": ["Deuteronomy 11:14", "Joel 2:23", "Zechariah 10:1"]
    },
    "sword": {
        "meaning": "Represents spiritual warfare, truth, and God's Word.",
        "scripture": ["Ephesians 6:17", "Hebrews 4:12", "Revelation 1:16"]
    },
}

def interpret_text(text):
    """
    Generates a structured symbolic analysis for the given sacred dream/vision text.
    """
    words = text.lower().split()
    matched_symbols = {}

    for word in words:
        if word in SYMBOL_DICTIONARY:
            symbol_data = SYMBOL_DICTIONARY[word]
            matched_symbols[word] = {
                "meaning": symbol_data["meaning"],
                "scripture": symbol_data["scripture"]
            }

    if not matched_symbols:
        return {"No significant symbols found": {"meaning": "Try using a more detailed description.", "scripture": []}}

    return matched_symbols


'''
def interpret_text(text):
    """
    Generates an interpretation by analyzing the symbols found in the text.
    """
    words = text.lower().split()
    matched_symbols = [word for word in words if word in SYMBOL_DICTIONARY]

    if not matched_symbols:
        return "No significant symbols found. Please try another description."

    interpretation = "This dream/vision contains the following symbols:\n\n"
    for symbol in matched_symbols:
        details = SYMBOL_DICTIONARY[symbol]
        interpretation += f"🔹 **{symbol.capitalize()}**: {details['meaning']}\n"
        interpretation += f"📖 **Biblical References**: {', '.join(details['scripture'])}\n\n"

    return interpretation.strip()
'''
'''
import openai

openai.api_key = "your-api-key"

def interpret_record_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that interprets dreams and visions with biblical references."},
            {"role": "user", "content": f"Interpret the following spiritual content and provide relevant biblical references: {text}"}
        ],
        max_tokens=300,
    )
    return response["choices"][0]["message"]["content"].strip()



import openai
from .biblical_references import get_biblical_references

def generate_interpretation(text):
    # AI Interpretation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Provide spiritual interpretation with biblical references"},
            {"role": "user", "content": text}
        ]
    )
    
    interpretation = response.choices[0].message['content']
    
    # Get ML-powered biblical references
    references = get_biblical_references(text)
    
    return {
        'interpretation': interpretation,
        'biblical_references': references
    }
    
'''