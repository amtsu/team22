# Inference
import re
import torch
from diffusers import StableDiffusion3Pipeline
import time

idea = "In a world where magic reigns supreme, an immortal elven mage named Frieren embarks on a journey of self-discovery as she confronts her past and rekindles old friendships in the mystical realm of Eridoria. Beautiful key art featuring Frieren standing amidst a misty forest backdrop with hints of ancient ruins and mythical creatures lurking in the shadows."
image = pipe(
    idea,
    num_inference_steps=28,
    guidance_scale=3.5,
).images[0]
image.save("image.png")
 
