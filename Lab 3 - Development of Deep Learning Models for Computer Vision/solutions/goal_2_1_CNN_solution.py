# -*- coding: utf-8 -*-
"""
Lab3 Goal 2.1 solution
CNN solution
"""

import os
import torch
from torch import nn
from torchvision.io import read_image
from torchvision.transforms.functional import rgb_to_grayscale


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

# Define model (Convoution Neural Network (CNN) model)
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_stack = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),  # Input: 1×28×28 → Output: 32×28×28
            nn.ReLU(),
            nn.MaxPool2d(2, 2),                         # Output: 32×14×14

            nn.Conv2d(32, 64, kernel_size=3, padding=1),# Output: 64×14×14
            nn.ReLU(),
            nn.MaxPool2d(2, 2)                          # Output: 64×7×7
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),                               # Flatten 64×7×7 → 3136
            nn.Linear(64 * 7 * 7, 512),
            nn.ReLU(),
            nn.Linear(512, 10)                          # 10 output classes
        )

    def forward(self, x):
        x = self.conv_stack(x)
        x = self.classifier(x)
        return x

model = NeuralNetwork().to(device)
print(model)

#Load trained model
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("model_CNN.pth", weights_only=True))
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

