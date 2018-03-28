import cv2, sys, numpy, os, time
haar_file = 'haarcascade_frontalface_default.xml'
fn_dir = 'database'
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

def isPerson(image, username):
    vals = getPerson(image)
    if vals[0] == username and vals[1] < 102:
        print(vals[0])
        print(str(vals[1]))
        return 1
    else: 
        print(vals[0])
        print(str(vals[1]))
        return 0
