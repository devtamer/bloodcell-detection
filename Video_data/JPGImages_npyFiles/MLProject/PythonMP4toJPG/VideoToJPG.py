import cv2
import os
import numpy as np
import os
print("file exists?", os.path.exists('200x200 micrometer  channel B  0.72 ul per min  40x  01.mp4'))

vidcap = cv2.VideoCapture('200x200 micrometer  channel B  0.72 ul per min  40x  01.mp4')
success,image = vidcap.read()
count = 0
success = True
while success and count < 20:
  success,image = vidcap.read()
  cv2.imwrite( "frame%d.jpg" % count, image)     # save frame as JPEG file 
  np.save(os.path.join('/Users/noahbland/Desktop/MLProject/Video8', 'data'), image)
  print('Read a new frame: ', success)

  count += 1