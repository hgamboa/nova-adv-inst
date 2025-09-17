# -*- coding: utf-8 -*-
"""
Lab3 Goal 2.1 solution
"""

import os
import torch
from torch import nn
from torchvision.io import read_image

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

# Define model
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10)
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

model = NeuralNetwork().to(device)
print(model)

#Load trained model
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("model_FNN.pth", weights_only=True))
model.eval() #tune network to evaluation mode
print('\nTrained model loaded\n')


#list img files to process
files = os.listdir('test_images')
img_folder = 'test_images'


for f in files:
    img=read_image(img_folder + '\\' + f)

    with torch.no_grad():
        img=img.float()
        img = img.to(device)
        pred = model(img)
        print(f'Image file: {f} \t Predicted: {labels_map[pred[0].argmax(0).item()]}')

