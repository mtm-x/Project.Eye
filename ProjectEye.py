import moondream as md
import cv2
from PIL import Image

model = md.vl(model='Model/moondream_vlm/moondream-0_5b-int8.mf.gz')  # Initialize model
image =Image.open("test_files/street.jpg")  # Load image
encoded_image = model.encode_image(image)  # Encode image (recommended for multiple operations)

# 1. Caption any image (length options: "short" or "normal" (default))
# caption = model.caption(encoded_image)["caption"]
# print("Caption:", caption)

# print("Streaming caption:", end=" ", flush=True)
# for chunk in model.caption(encoded_image, stream=True)["caption"]:
#     print(chunk, end="", flush=True)

# 2. Query any image
# answer = model.query(encoded_image, "Can You extract the text from the image")["answer"]
# print("\nAnswer:", answer)  # Single response

print("Streaming answer:", end=" ", flush=True)
for chunk in model.query(encoded_image, "What's in this image? Can you explain it ?", stream=True)["answer"]:
    print(chunk, end="", flush=True)

# 3. Detect any object
# detect_result = model.detect(encoded_image, "subject")  # change 'subject' to what you want to detect
# print("\nDetected:", detect_result["objects"])

