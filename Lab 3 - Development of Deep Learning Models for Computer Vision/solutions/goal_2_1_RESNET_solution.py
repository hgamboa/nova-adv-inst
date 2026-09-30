# -*- coding: utf-8 -*-
"""
Lab3 Goal 2.1 solution
RESNET solution
"""

import os
import torch
from torch import nn
from torchvision.io import read_image
from torchvision.transforms.functional import rgb_to_grayscale
from torchvision import models


#labels map
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

#prepare processing unit
device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
print(f"Using {device} device")

# Define model (ResNet18 pretrained model)
class NeuralNetwork(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        # Load pretrained ResNet18
        self.base_model = models.resnet18(pretrained=True)

        # Adapt input layer for grayscale images (1 channel instead of 3)
        self.base_model.conv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)

        # Replace the final fully connected layer
        self.base_model.fc = nn.Linear(self.base_model.fc.in_features, num_classes)

    def forward(self, x):
        return self.base_model(x)

model = NeuralNetwork().to(device)
print(model)

#Load trained model
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("model_ResNet.pth", weights_only=True))
model.eval() #tune network to evaluation mode
print('\nTrained model loaded\n')


#list img files to process
files = os.listdir('test_images')
img_folder = 'test_images'


for f in files:
    img=read_image(img_folder + '\\' + f)

    with torch.no_grad():
        img = rgb_to_grayscale(img, num_output_channels=1)
        img=img.float()
        #img = img.to(device)
        img = img.unsqueeze(0).to(device)
        pred = model(img)
        print(f'Image file: {f} \t Predicted: {labels_map[pred[0].argmax(0).item()]}')

