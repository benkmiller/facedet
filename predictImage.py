'''
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
    else:
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

def isPerson(imagepath, username):
    image = cv2.imread(imagepath, 0)
    #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    #image = clahe.apply(im)

    face_cascade = cv2.CascadeClassifier(haar_file)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image, 1.3, 4)
    if len(faces) == 0:
        print("no faces!!!")
        return 0
    vals = getPerson(image)

    if vals[0] == username and vals[1] < 97:
        print(vals[0])
        print(str(vals[1]))
        return 1
    else:
        print(vals[0])
        print(str(vals[1]))
        return 0

'''

import face_recognition
import cv2

def isPerson(path):
	img2 = cv2.imread("/home/pi/ComputerVision/facedet/1.jpg", 0)
	cv2.imwrite("/home/pi/ComputerVision/facedet/1.jpg", img2)
	picture_of_me = face_recognition.load_image_file("/home/pi/ComputerVision/facedet/1.jpg")

	#face_locations = face_recognition.face_locations(picture_of_me)
	#print(face_locations)

	encodings = face_recognition.face_encodings(picture_of_me)
	if len(encodings) > 0:
		my_face_encoding = encodings[0]
	else:
		print("No face detected in the picture! Quitting!")
		return 0

	img = cv2.imread(path, 0)
	cv2.imwrite(path, img)
	unknown = face_recognition.load_image_file(path)

	#face_locations = face_recognition.face_locations(unknown)
	#print(face_locations)

	#picture_of_me = face_recognition.load_image_file("obama.jpg")
	#print(picture_of_me)
	#my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
	encodings2 = face_recognition.face_encodings(unknown)
	if len(encodings2) > 0:
		unknown_face_encoding = encodings2[0]
	else:
		print("No face detected in the picture! Quitting!")
		return 0

	results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

	if results[0] == True:
		print("success")
		return 1
	else:
		print("not me")
		return 0

#isPerson("./2.jpg")
'''
