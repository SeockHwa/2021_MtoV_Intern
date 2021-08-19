import cv2
import numpy as np

img = cv2.imread('front3.jpg')
img2 = img.copy()
img3 = img.copy()

# 그레이 스케일로 변환 ---①
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imgray',imgray)

img_gaussian = cv2.GaussianBlur(imgray, ksize=(7, 7), sigmaX=0)


# 스레시홀드로 바이너리 이미지로 만들어서 검은배경에 흰색전경으로 반전 ---②

ret, imthres60 = cv2.threshold(imgray, 60, 255, cv2.THRESH_BINARY_INV)
# imthres2 = cv2.adaptiveThreshold(img_gaussian,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
# imthres3 = cv2.adaptiveThreshold (img_gaussian,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

ret, imthres_low = cv2.threshold(imgray, 60, 255, cv2.THRESH_BINARY_INV)
ret, imthres_high = cv2.threshold(imgray, 140, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('low', imthres_low)
cv2.imshow('high', imthres_high)

#cv2.imwrite('threshold.jpg', imthres60)

# cv2.imshow('imthres2', imthres2)
# cv2.imshow('imthres3', imthres3)

# # 가장 바깥쪽 컨투어에 대해 모든 좌표 반환 ---③
# contour, hierarchy = cv2.findContours(imthres65, cv2.RETR_EXTERNAL, \
#                                                  cv2.CHAIN_APPROX_NONE)
# # 가장 바깥쪽 컨투어에 대해 꼭지점 좌표만 반환 ---④
# contour2, hierarchy = cv2.findContours(imthres65, cv2.RETR_EXTERNAL, \
#                                                 cv2.CHAIN_APPROX_SIMPLE)

                                            
# # 각각의 컨투의 갯수 출력 ---⑤
# print('도형의 갯수: %d(%d)'% (len(contour), len(contour2)))

# # 모든 좌표를 갖는 컨투어 그리기, 초록색  ---⑥
# cv2.drawContours(img, contour, -1, (0,255,0), 4)
# # 꼭지점 좌표만을 갖는 컨투어 그리기, 초록색  ---⑦
# cv2.drawContours(img2, contour2, -1, (0,255,0), 4)


# # 컨투어 모든 좌표를 작은 파랑색 점(원)으로 표시 ---⑧
# for i in contour:
#     for j in i:
#         cv2.circle(img, tuple(j[0]), 1, (255,0,0), -1) 

# # 컨투어 꼭지점 좌표를 작은 파랑색 점(원)으로 표시 ---⑨
# for i in contour2:
#     for j in i:
#         cv2.circle(img2, tuple(j[0]), 1, (0,255,0), -1) 
       

# # 결과 출력 ---⑩
# cv2.imshow('CHAIN_APPROX_NONE', img)
# cv2.imshow('CHAIN_APPROX_SIMPLE', img2)

cv2.waitKey()
cv2.destroyAllWindows()