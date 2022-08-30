#!/bin/bash
wget --directory-prefix=models/first_stage_models/kl-f4 https://ommer-lab.com/files/latent-diffusion/kl-f4.zip
wget --directory-prefix=models/first_stage_models/kl-f8 https://ommer-lab.com/files/latent-diffusion/kl-f8.zip
wget --directory-prefix=models/first_stage_models/kl-f16 https://ommer-lab.com/files/latent-diffusion/kl-f16.zip
wget --directory-prefix=models/first_stage_models/kl-f32 https://ommer-lab.com/files/latent-diffusion/kl-f32.zip
wget --directory-prefix=models/first_stage_models/vq-f4 https://ommer-lab.com/files/latent-diffusion/vq-f4.zip
wget --directory-prefix=models/first_stage_models/vq-f4-noattn https://ommer-lab.com/files/latent-diffusion/vq-f4-noattn.zip
wget --directory-prefix=models/first_stage_models/vq-f8 https://ommer-lab.com/files/latent-diffusion/vq-f8.zip
wget --directory-prefix=models/first_stage_models/vq-f8-n256 https://ommer-lab.com/files/latent-diffusion/vq-f8-n256.zip
wget --directory-prefix=models/first_stage_models/vq-f16 https://ommer-lab.com/files/latent-diffusion/vq-f16.zip



cd models/first_stage_models/kl-f4
unzip -o kl-f4.zip

cd ../kl-f8
unzip -o kl-f8.zip

cd ../kl-f16
unzip -o kl-f16.zip

cd ../kl-f32
unzip -o kl-f32.zip

cd ../vq-f4
unzip -o vq-f4.zip

cd ../vq-f4-noattn
unzip -o vq-f4-noattn.zip

cd ../vq-f8
unzip -o vq-f8.zip

cd ../vq-f8-n256
unzip -o vq-f8-n256.zip

cd ../vq-f16
unzip -o vq-f16.zip

cd ../..