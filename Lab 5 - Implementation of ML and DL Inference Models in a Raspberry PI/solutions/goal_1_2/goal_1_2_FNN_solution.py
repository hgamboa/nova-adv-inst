# -*- coding: utf-8 -*-
"""
Lab3 Goal 1.2 solution
FNN solution
"""

print('Starting goal_2_1_FNN_solution.py')
print('Importing Libraries')

import os
import torch
from torchvision import transforms
from torch import nn
from torchvision.io import read_image
from PIL import Image

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

# Define image transformations
transform = transforms.Compose([
    transforms.Grayscale(),              # Ensure single channel
    #transforms.Resize((28, 28)),  # Resize to match RegNet input
    transforms.ToTensor(),        # Convert to tensor
    #transforms.Normalize((0.5,), (0.5,))  # Normalize grayscale images
])

#prepare processing unit
print('Preparing processing unit')
device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
print(f"Using {device} device")

# Define model
print('Defining FNN Model')
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
print('Loading trained model')
model = NeuralNetwork().to(device)
model.load_state_dict(torch.load("model_FNN.pth", map_location=torch.device('cpu'), weights_only=True))
model.eval() #tune network to evaluation mode
print('\nTrained model loaded\n')


#list img files to process
print('Running model inference')
files = os.listdir('test_images')
img_folder = 'test_images'


for f in files:
    img=Image.open(os.path.join(img_folder, f))
    input_tensor = transform(img).unsqueeze(0)  # Add batch dimension

    with torch.no_grad():
        input_tensor = input_tensor.to(device)
        pred = model(input_tensor)
        print(f'Image file: {f} \t Predicted: {labels_map[pred[0].argmax(0).item()]}')

print('End')

