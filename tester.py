import cv2, sys, numpy, os, time
import predictImage
fn_dir = 'database'

photo_path = sys.argv[1]
#user_name = sys.argv[1]

width = 112
height = 92

if not os.path.exists(photo_path):
    print("wrong path")

print(photo_path)
image = cv2.imread(photo_path,0)
print(image)
time.sleep(0.1)

if predictImage.isPerson(image, 'ben'):
    print("Hello, Ben")
else:
    print("Intruder Alert!!!")


