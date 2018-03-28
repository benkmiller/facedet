import cv2, sys, numpy, os, time
haar_file = 'haarcascade_frontalface_default.xml'
fn_dir = 'database'

photo_path = sys.argv[1]
#user_name = sys.argv[1]

width = 112
height = 92


def getCropped(grey):
    face_cascade = cv2.CascadeClassifier(haar_file)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.3, 4)
    if len(faces) == 0:
    	print("no faces!!!")
    for (x,y,w,h) in faces:
        cv2.rectangle(grey,(x,y),(x+w,y+h),(255,0,0),2)
        face = grey[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        return face_resize

def getNames():
    (names, id) = ({}, 0)
    for (subdirs, dirs, files) in os.walk(fn_dir):
        for subdir in dirs:
            names[id] = subdir
            id += 1
    return names

def getPerson(image):
    cropped_image = getCropped(image)

    model = cv2.face.LBPHFaceRecognizer_create()
    model.read('trainer.yml')
    prediction = model.predict(cropped_image)
    names = getNames()
    retvals = [names[prediction[0]], prediction[1]]
    return retvals

if not os.path.exists(photo_path):
    print("wrong path")

print(photo_path)
image = cv2.imread(photo_path,0)
print(image)
#webcam = cv2.VideoCapture(0)
time.sleep(0.1)
#(_, image) = webcam.read()
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#print(image)
vals = getPerson(image)

'''
val = 1
while val:
    time.sleep(0.1)
    (_, image) = webcam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print(image)
    vals = getPerson(gray)
    if not vals == [0]:
    	break
'''
print(vals[0])
print(str(vals[1]))
'''
if vals[0] == user_name and vals[1] < 105:
    print("Hi, " + user_name)
    print("score: " + str(vals[1]))
else:
    print("not " + user_name + "!!!")
    print(vals[0])
    print("score: " + str(vals[1]))
'''
