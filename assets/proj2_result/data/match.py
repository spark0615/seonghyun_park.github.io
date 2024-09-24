import cv2

# Load the images
img1 = cv2.imread('bear.jpg')  # Image to transform
img2 = cv2.imread('gummy.jpg')  # Reference image
# Initialize ORB detector
orb = cv2.ORB_create()

# Detect keypoints and descriptors
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
# Use BFMatcher to find the best matches
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)
import numpy as np

# Extract the matched points
src_pts = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# Calculate the Homography matrix
M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
# Get the size of the second image
h, w, _ = img2.shape

# Warp the first image using the transformation matrix
transformed_img = cv2.warpPerspective(img1, M, (w, h))
# Create a blended image using weighted sum
blended = cv2.addWeighted(transformed_img, 0.5, img2, 0.5, 0)
import matplotlib.pyplot as plt

# Display the result
plt.imshow(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB))
plt.show()


