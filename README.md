# A Whole New World: Seamless Image Inpainting


Image inpainting is a computer vision task that involves filling in missing or damaged parts of an image. It has various applications including photo editing, image restoration, and object removal. In this project, we focus on image inpainting using PatchGAN, a type of Generative Adversarial Network (GAN), on the CelebA dataset, which contains over 200,000 celebrity images.

## Methodology

### Dataset Preparation:
The CelebA dataset consists of images with various resolutions and annotations such as facial key points and attributes.
We preprocess the dataset to extract the images and masks indicating the regions to be inpainted.

### Model Architecture:
We employ PatchGAN, which is a type of GAN specifically designed for image-to-image translation tasks.
PatchGAN operates by classifying image patches as real or fake, enabling it to generate high-quality, coherent outputs.

 ### Training:
The model is trained using a combination of adversarial and reconstruction losses.
Adversarial loss encourages the generator to produce realistic inpainted images, while reconstruction loss ensures that the inpainted regions match the surrounding context.

### Evaluation:
We evaluate the performance of the model on both quantitative and qualitative metrics.
Quantitatively, we measure metrics such as PSNR (Peak Signal-to-Noise Ratio) and SSIM (Structural Similarity Index).
Qualitatively, we visually inspect the inpainted images to assess the quality and coherence of the generated content.

### Hosting
To make the trained model accessible and user-friendly, we develop a Flask-based website for hosting the image inpainting service.

#### Frontend:
The front end of the website allows users to upload images with missing regions.
Users can specify the areas to be inpainted or allow the model to automatically detect and inpaint missing regions.
#### Backend:
The backend of the website integrates the trained PatchGAN model for inpainting.
Upon receiving an image, the backend processes it through the model and returns the inpainted result to the user.
#### Deployment:
We deploy the Flask website on Vercel.
And can be accessed here.

## Results
![image](https://github.com/Kazedaa/Image-Inpainting/assets/120291477/ac4dc3b2-0991-44c1-8d69-2ecd49e10acc)![image](https://github.com/Kazedaa/Image-Inpainting/assets/120291477/0d35c2ff-3f81-4216-a88e-ca9d1c28c5c5)
![image](https://github.com/Kazedaa/Image-Inpainting/assets/120291477/2faa5b4f-208d-4663-a1b5-7dfc0b33e398)![image](https://github.com/Kazedaa/Image-Inpainting/assets/120291477/02013534-3f5f-47ae-8323-d0523f1af256)

## Install
1. **Get Dependencies"
```bash
conda create -n img_inpaint python=3.8
conda activate img_inpaint
pip install -r requirements.txt
```
2. **Run App"
   ```bash
   python app.py
  ```
