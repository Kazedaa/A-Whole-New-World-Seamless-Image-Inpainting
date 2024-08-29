# A Hole New World: Seamless Image Inpainting


Image inpainting is a computer vision task that involves filling in missing or damaged parts of an image. It has various applications including photo editing, image restoration, and object removal. The project focuses on image inpainting using PatchGAN, a type of Generative Adversarial Network (GAN), on the CelebA dataset, which contains over 200,000 celebrity images.

## Methodology

### Dataset Preparation:
The CelebA dataset consists of images with various resolutions and annotations such as facial key points and attributes.
We preprocess the dataset to extract the images and masks indicating the regions to be inpainted.

### Model Architecture:
A PatchGAN is employed, a type of GAN specifically designed for image-to-image translation tasks.
PatchGAN operates by classifying image patches as real or fake, enabling it to generate high-quality, coherent outputs.

 ### Training:
The model is trained using a combination of adversarial and reconstruction losses.
Adversarial loss encourages the generator to produce realistic images, while reconstruction loss ensures that the inpainted regions match the surrounding context.
<br>
[Training Code on Kaggle](https://www.kaggle.com/code/sciencerz/image-inpainting-celeba/settings)

#### Frontend and hosting:
A flask Website is made, to make the trained model accessible and user-friendly.
The front end of the website allows users to upload images with missing regions.
Users can specify the areas to be inpainted or allow the model to automatically detect and inpaint missing regions.

#### Backend:
The backend of the website integrates the trained PatchGAN model for inpainting.
Javascript's Fetch API is used to communicate between the frontend and backend.
Upon receiving an image with the position for the mask <div>, the image path along with the cordinates of the mask is sent to the backend via a Fetch API.
The backend creates a masked image, as input to the model and saves the output, which is then displayed on the website.

## Results
![image](https://github.com/Kazedaa/Image-Inpainting/assets/120291477/ac4dc3b2-0991-44c1-8d69-2ecd49e10acc)![image](https://github.com/Kazedaa/Image-Inpainting/assets/120291477/0d35c2ff-3f81-4216-a88e-ca9d1c28c5c5)
![image](https://github.com/Kazedaa/Image-Inpainting/assets/120291477/2faa5b4f-208d-4663-a1b5-7dfc0b33e398)![image](https://github.com/Kazedaa/Image-Inpainting/assets/120291477/02013534-3f5f-47ae-8323-d0523f1af256)

## Install
1. **Get Dependencies**
```bash
conda create -n img_inpaint python=3.8
conda activate img_inpaint
pip install -r app_requirements.txt
```
2. **Run App**
 ```bash
   python app.py
 ```
3. ** Use the `Samples` folder to select images to upload

Note on Hosting: The model is too big to be hosted on any free PaaS provider(vercel, heroku....) . If you are aware of any provider or have a different solution please feel free to contact me. Or post an issue :) Thanks! 
