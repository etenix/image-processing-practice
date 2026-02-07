import cv2

# Read image
img = cv2.imread("test.jpg")

# Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save result
cv2.imwrite("gray_image.jpg", gray)

print("Image converted to grayscale.")