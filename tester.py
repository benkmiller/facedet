import cv2, sys, numpy, os, time
import predictImage
fn_dir = 'database'

photo_path = sys.argv[1]
#num_photos = sys.argv[2]

width = 112
height = 92

if not os.path.exists(photo_path):
    print("wrong path")

print(photo_path)
#image = cv2.imread(photo_path,0)
time.sleep(0.1)

#if predictImage.isPerson(image, 'ben'):
#    print("Hello, Ben")
#else:
#    print("Intruder Alert!!!")


#subjectpath = os.path.join(datasets, subdir)
count = 0
for filename in os.listdir(photo_path):
    print(count)
    print(filename)
    path = photo_path + '/' + filename
    #image = cv2.imread(path, 0)
    if predictImage.isPerson(path, 'ben'):
        print("Hello, Ben")
    else:
        print("Intruder Alert!!!")
    count += 1





