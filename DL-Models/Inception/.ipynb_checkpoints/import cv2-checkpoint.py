import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the ECG image
image_path = '5439ace6-e575-4368-a67c-d06c35138350.png'  # Adjust path if needed
img = cv2.imread(image_path)

# --- Functions Provided and Extended ---
def extract_green_channel(img):
    # Split the image into its RGB components
    b, g, r = cv2.split(img)
    return g  # Return the green channel

def preprocess_green_channel(green_channel):
    # Resize the image
    resized = cv2.resize(green_channel, (1024, 1024))  # Resize to 1024x1024
    # Normalize pixel values to [0, 1]
    normalized = resized / 255.0
    return normalized

def display_image(image, title='Image'):
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()

# --- Process ECG Image ---
green_channel = extract_green_channel(img)
preprocessed = preprocess_green_channel(green_channel)

# Display the result
display_image(preprocessed, title='Preprocessed Green Channel')
