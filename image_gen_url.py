import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO #used to store buffer memory to store and capture images


def load_image_from_url(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

elephant_url = "https://upload.wikimedia.org/wikipedia/commons/3/37/African_Bush_Elephant.jpg"
elephant = load_image_from_url(elephant_url)
#display an original image
plt.figure(figsize=(6,4))
plt.imshow(elephant)
plt.title('Elephant')
plt.axis('off')
plt.show()


#image to array
elephant_np = np.array(elephant)
print('Elephant image shape', elephant_np.shape)

#display gray scale images
elephant_gray = elephant.convert("L")

plt.figure(figsize=(6,6))
plt.imshow(elephant_gray, cmap='red')
plt.title('Elephant(gray_scale)')
plt.axis('off')
plt.show()