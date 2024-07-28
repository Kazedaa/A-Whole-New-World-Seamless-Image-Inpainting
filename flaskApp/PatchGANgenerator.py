import os
import torch
from torch.autograd import Variable
import torchvision.transforms as transforms
from torchvision.transforms import v2
from torchvision.utils import save_image
from PIL import Image

from flaskApp.PatchGanModel import PatchGan

import random
random.seed(42)
import warnings
warnings.filterwarnings("ignore")

# size of each image dimension
img_size = 128
# size of random mask
mask_size = 64
# number of image channels
channels = 3
#device agnostics
device = "cuda" if torch.cuda.is_available() else "cpu"


#Agmentation
transforms_ = v2.Compose([
    transforms.Resize((img_size, img_size), Image.BICUBIC),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

# Initialize generator
generator = PatchGan(channels=channels)
#Load Pretrained Weights
generator.load_state_dict(torch.load(os.path.join('flaskApp','Patchgenerator.pth'), map_location=torch.device(device)))


Tensor = torch.FloatTensor

def format(image_name:str)->None:
    image=transforms_(Image.open(os.path.join('flaskApp','images',image_name)))
    save_image(image, os.path.join('flaskApp','masks',image_name), normalize=True)


def inpaint(image_name:str , x1:int , y1:int)->None:
    image=transforms_(Image.open(os.path.join('flaskApp','images',image_name)))

    y2, x2 = y1 + mask_size, x1 + mask_size

    masked_image = image.clone()
    masked_image[:, y1:y2, x1:x2] = 0

    image = Variable(image.type(Tensor))
    masked_image = Variable(masked_image.type(Tensor))
    # Generate inpainted image
    generator.eval()
    with torch.inference_mode():
        generated_mask = generator(masked_image.unsqueeze(dim=0))
    inpainted_image = masked_image.clone().squeeze(dim=0)
    inpainted_image[: ,y1:y1+mask_size,x1:x1+mask_size] = generated_mask.unsqueeze(dim=0)
    # Save sample
    save_image(masked_image, os.path.join('flaskApp','masks',image_name), normalize=True)
    save_image(inpainted_image, os.path.join('flaskApp','inpainted',image_name), normalize=True)
