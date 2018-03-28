import cv2, sys, numpy, os, time
fn_haar = 'haarcascade_frontalface_default.xml'
fn_dir = 'database'
out_dir = sys.argv[1]
input_dir = sys.argv[2]
numphotos = sys.argv[3]
images = []
labels = []

width = 112
height = 92

#path = os.path.join(database, sub_data)
#if not os.path.isdir(path):
#    os.mkdir(path)

#face_cascade = cv2.CascadeClassifier(haar_file)
#gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#faces = face_cascade.detectMultiScale(gray, 1.3, 4)
webcam = cv2.VideoCapture(0)

count = 1
while count < int(numphotos): 
    (_, im) = webcam.read()
    images.append(im)
    cv2.imwrite('%s/%s.png' % (out_dir,count), im)
    i = 0
    input(i)
    count += 1

'''
for filename in os.listdir(input_dir):
    print('hey')
    path = input_dir + '/' + filename
    images.append(cv2.imread(path, 0))
'''
print(images)
#for (x,y,w,h) in faces:
#    cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
#    face = gray[y:y + h, x:x + w]
#    face_resize = cv2.resize(face, (width, height))
#    cv2.imwrite('%s/%s.png' % (path,count), face_resize)


