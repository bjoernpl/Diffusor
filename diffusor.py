import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"

pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, use_auth_token=True)
pipe = pipe.to(device)

prompt = "An oil painting of a monstera plant."
with autocast("cuda"):
    image = pipe(prompt)["sample"][0]

image.save("monstera.png")
plt.imshow(image)
plt.axis("off")
plt.title(prompt)
plt.tight_layout()
plt.savefig("monstera.pdf")
plt.show()