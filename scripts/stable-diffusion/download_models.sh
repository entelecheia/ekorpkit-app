#!/bin/bash
wget --directory-prefix=models/ldm/celeba256/celeba-256.zip https://ommer-lab.com/files/latent-diffusion/celeba.zip
wget --directory-prefix=models/ldm/ffhq256/ffhq-256.zip https://ommer-lab.com/files/latent-diffusion/ffhq.zip
wget --directory-prefix=models/ldm/lsun_churches256/lsun_churches-256.zip https://ommer-lab.com/files/latent-diffusion/lsun_churches.zip
wget --directory-prefix=models/ldm/lsun_beds256/lsun_beds-256.zip https://ommer-lab.com/files/latent-diffusion/lsun_bedrooms.zip
wget --directory-prefix=models/ldm/text2img256/model.zip https://ommer-lab.com/files/latent-diffusion/text2img.zip
wget --directory-prefix=models/ldm/cin256/model.zip https://ommer-lab.com/files/latent-diffusion/cin.zip
wget --directory-prefix=models/ldm/semantic_synthesis512/model.zip https://ommer-lab.com/files/latent-diffusion/semantic_synthesis.zip
wget --directory-prefix=models/ldm/semantic_synthesis256/model.zip https://ommer-lab.com/files/latent-diffusion/semantic_synthesis256.zip
wget --directory-prefix=models/ldm/bsr_sr/model.zip https://ommer-lab.com/files/latent-diffusion/sr_bsr.zip
wget --directory-prefix=models/ldm/layout2img-openimages256/model.zip https://ommer-lab.com/files/latent-diffusion/layout2img_model.zip
wget --directory-prefix=models/ldm/inpainting_big/model.zip https://ommer-lab.com/files/latent-diffusion/inpainting_big.zip



cd models/ldm/celeba256
unzip -o celeba-256.zip

cd ../ffhq256
unzip -o ffhq-256.zip

cd ../lsun_churches256
unzip -o lsun_churches-256.zip

cd ../lsun_beds256
unzip -o lsun_beds-256.zip

cd ../text2img256
unzip -o model.zip

cd ../cin256
unzip -o model.zip

cd ../semantic_synthesis512
unzip -o model.zip

cd ../semantic_synthesis256
unzip -o model.zip

cd ../bsr_sr
unzip -o model.zip

cd ../layout2img-openimages256
unzip -o model.zip

cd ../inpainting_big
unzip -o model.zip

cd ../..
