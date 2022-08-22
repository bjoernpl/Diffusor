# Image generation with Latent Diffusion

This is a repository to test image generation with latent diffusion. The pretrained model
used here is provided from https://huggingface.co/CompVis/stable-diffusion-v1-4 and the code
for the diffusor library can be found here: https://github.com/huggingface/diffusers

## Installation
First install the diffusers library and all other dependencies:
```bash
pip install --upgrade -r requirements.txt
```
Accept TOS on the [website](https://huggingface.co/CompVis/stable-diffusion-v1-4) and log in with the huggingace-cli:
```
huggingface-cli login
```
