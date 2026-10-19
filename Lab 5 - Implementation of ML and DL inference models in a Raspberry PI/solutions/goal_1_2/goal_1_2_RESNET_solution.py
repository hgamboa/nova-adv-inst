# -*- coding: utf-8 -*-
"""
Lab3 Goal 1.2 solution
RESNET solution
"""

print('Starting goal_2_1_RESNET_solution.py')
print('Importing Libraries')

import os
import torch
from torch import nn
from torchvision import transforms
from torchvision.io import read_image
from torchvision.transforms.functional import rgb_to_grayscale
from torchvision import models

from PIL import Image

# Define image transformations
transform = transforms.Compose([
    transforms.Grayscale(),              # Ensure single channel
    #transforms.Resize((28, 28)),  # Resize to match RegNet input
    transforms.ToTensor(),        # Convert to tensor
    #transforms.Normalize((0.5,), (0.5,))  # Normalize grayscale images
])

#labels map
print('Creating Labels Maps')
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
print('Preparing processing unit')
device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
print(f"Using {device} device")

# Define model (ResNet18 pretrained model)
print('Defining ResNet18 Model')
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
print('Loading trained model')
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("model_ResNet.pth", map_location=torch.device('cpu'), weights_only=True))
model.eval() #tune network to evaluation mode
print('\nTrained model loaded\n')


#list img files to process
print('Running model inference')
files = os.listdir('test_images')
img_folder = 'test_images'


for f in files:  
    img = Image.open(os.path.join(img_folder, f))
    input_tensor = transform(img).unsqueeze(0)  # Add batch dimension


    with torch.no_grad():
        input_tensor = input_tensor.to(device)
        pred = model(input_tensor)
        print(f'Image file: {f} \t Predicted: {labels_map[pred[0].argmax(0).item()]}')

print('End')
