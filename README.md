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

Note that this model requires an NVIDIA GPU with at least 7GB of VRAM when running in FP16 mode.

## Citation
Stable Diffusion is a latent text-to-image diffusion model capable of generating 
photo-realistic images given any text input. 
For more information about how Stable Diffusion functions, 
please have a look at 🤗's [Stable Diffusion with D🧨iffusers blog](https://huggingface.co/blog/stable_diffusion).

It is based on the following paper:
[High-Resolution Image Synthesis With Latent Diffusion Models](https://arxiv.org/abs/2112.10752)
```
@InProceedings{Rombach_2022_CVPR,
    author    = {Rombach, Robin and Blattmann, Andreas and Lorenz, Dominik and Esser, Patrick and Ommer, Bj\"orn},
    title     = {High-Resolution Image Synthesis With Latent Diffusion Models},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2022},
    pages     = {10684-10695}
}
```
