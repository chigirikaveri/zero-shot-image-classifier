from transformers import BlipProcessor,BlipForConditionalGeneration
from PIL import Image
import requests
import matplotlib.pyplot as plt
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model=BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
img_url = "https://images.unsplash.com/photo-1478098711619-5ab0b478d6e6"
image = Image.open(requests.get(img_url,stream=True).raw).convert("RGB")
plt.imshow(image)
plt.axis("off")
plt.show()
inputs=processor(images=image,return_tensors="pt")
output=model.generate(**inputs)
caption = processor.decode(output[0],skip_special_tokens=True)
print("caption:",caption)
