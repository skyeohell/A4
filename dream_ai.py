import os
import base64
from io import BytesIO
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# -------- TEXT INTERPRETATION --------
def analyze_dream(dream_text):

    jung_prompt = f"""
You are a Jungian psychoanalyst trained in analytical psychology.

Interpret the following dream using Jungian concepts such as:
- archetypes
- shadow
- anima/animus
- the collective unconscious
- individuation

Focus on symbolic meaning, not prediction or superstition.
Write 2–3 reflective paragraphs.

Dream:
{dream_text}
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=jung_prompt
    )

    return response.output_text


# -------- IMAGE GENERATION --------
def generate_dream_image(dream_text):

    image_prompt = f"""
A surreal symbolic illustration representing this dream:

{dream_text}

Style: painterly, dreamlike, psychological symbolism, Carl Jung inspired,
moody lighting, soft textures, ethereal atmosphere
"""

    img = client.images.generate(
        model="gpt-image-1",
        prompt=image_prompt,
        size="1024x1024"
    )

    image_base64 = img.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    return image_bytes