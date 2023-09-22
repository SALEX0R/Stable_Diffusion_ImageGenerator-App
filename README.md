# Stable_Diffusion_ImageGenerator-App
This project is a simple graphical user interface (GUI) application that uses the Tkinter library to create a user-friendly interface for generating images. It leverages the power of the StableDiffusionPipeline model to generate images based on user-provided text prompts.

## Features

- Generate images from text prompts.
- Visualize the generated images in real-time.
- Save the generated images to your local machine.

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- Pip (Python package manager)

Use the following command to install the required Python packages:

pip install -r requirements.txt

## Usage
Clone the repository to your local machine.
Install the required Python packages (if not already installed).
Run the app.py script to start the application.
Enter text prompts in the input field.
Click the "Generate" button to generate images.
View and save the generated images.
Configuration
You can configure the following settings in the config.json file:

Model ID: The ID of the pre-trained model to use for image generation.
Device: Choose between "cuda" (GPU) or "cpu" (CPU) for model inference.


## Acknowledgments
Tkinter - Python's standard GUI (Graphical User Interface) package.
Hugging Face Transformers - For pre-trained models and pipelines.
Pillow (PIL Fork) - Python Imaging Library for image processing.
