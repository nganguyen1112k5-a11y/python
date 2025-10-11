import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Lấy đường dẫn thư mục chứa file test1.py
# base_dir = os.path.dirname(os.path.abspath("aa"))
# image_path = os.path.join(base_dir, 'Screenshot 2025-10-03 224913.png')

a = 'Screenshot 2025-10-06 073408.png'

img = mpimg.imread(a)
## display image 
plt.imshow(img)
## show
plt.show()
