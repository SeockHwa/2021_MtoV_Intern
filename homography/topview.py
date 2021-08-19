import cv2
import matplotlib.pyplot as plt
import numpy as np

# Input Image
input = cv2.imread('front_image/front3.jpg')
plt.imshow(input)
plt.show()

# Coordinates that you want to Perspective Transform
pts1 = np.float32([[407, 722], [823, 300], [1390, 300], [1762, 722]])
# Size of the Transformed Image
pts2 = np.float32([[100,1140],[100,100],[620,100],[620,1140]])

#view point position
#for val in pts1:
#    cv2.circle(paper,(val[0],val[1]),5,(0.0,255.0,0.0),-1)

# Homography Matrix
M = cv2.getPerspectiveTransform(pts1,pts2)

# Apply Homography Matrix
dst = cv2.warpPerspective(input,M,(720,1440))
dst = np.array(dst)

# Output Image
cv2.imwrite("output_front.jpg", dst)
plt.imshow(dst)
plt.show()
