import torch
from diffusers import AutoencoderKLAllegro, AllegroPipeline
from diffusers.utils import export_to_video
vae = AutoencoderKLAllegro.from_pretrained("rhymes-ai/Allegro", subfolder="vae", torch_dtype=torch.float32)
pipe = AllegroPipeline.from_pretrained(
    "rhymes-ai/Allegro", vae=vae, torch_dtype=torch.bfloat16
)
pipe.to("cuda")
pipe.vae.enable_tiling()
prompt = "In a world where magic reigns supreme, an immortal elven mage named Frieren embarks on a journey of self-discovery as she confronts her past and rekindles old friendships in the mystical realm of Eridoria. Beautiful key art featuring Frieren standing amidst a misty forest backdrop with hints of ancient ruins and mythical creatures lurking in the shadows."

positive_prompt = """
(masterpiece), (best quality), (ultra-detailed), (unwatermarked), 
{} 
emotional, harmonious, vignette, 4k epic detailed, shot on kodak, 35mm photo, 
sharp focus, high budget, cinemascope, moody, epic, gorgeous
"""

negative_prompt = """
nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, 
low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry.
"""

prompt = prompt.format(prompt.lower().strip())

video = pipe(prompt, negative_prompt=negative_prompt, guidance_scale=7.5, max_sequence_length=512, num_inference_steps=100, generator = torch.Generator(device="cuda:0").manual_seed(42)).frames[0]
export_to_video(video, "output.mp4", fps=15)