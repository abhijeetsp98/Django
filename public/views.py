from django.shortcuts import render
from django.contrib import messages
from django import forms
from .forms import PublicRegForm, VotingRegForm
from django.http import HttpResponse
import face_recognition as fr
import os
from cv2 import cv2
import face_recognition
import numpy as np
from time import sleep
from .models import PublicData
import shutil  
from blog.models import Post
def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("media/uploads/"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("media/uploads/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded


def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    face = fr.load_image_file("media/uploads/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding


def classify_face(im):
    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param im: str of file path
    :return: list of face names
    """
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())

    img = cv2.imread(im, 1)
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = img[:,:,::-1]
 
    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)

    return face_names 


def register_public(request):
    if request.method == 'POST': # if request is of type post then we want this data to be saved validated and saved to the database
        form = PublicRegForm(request.POST,request.FILES)
        if form.is_valid(): # all form data is validated if all are correct then save it to database
            form.save()
            messages.success(request, f'Public data has been added')
    else:
        form = PublicRegForm()
    return render(request,'public/register_public.html', {'form':form})


def voting_public(request):
    if request.method == 'POST': # if request is of type post then we want this data to be saved validated and saved to the database
            # all form data is validated if all are correct then save it to database
            key = cv2. waitKey(1)
            webcam = cv2.VideoCapture(0)
            while True:
                try:
                    check, frame = webcam.read()
                    cv2.imshow("Capturing", frame)
                    key = cv2.waitKey(1)
                    if key == ord('s'): 
                        cv2.imwrite(filename='testing.jpg', img=frame)
                        webcam.release()
                        img_new = cv2.imread('testing.jpg', cv2.IMREAD_GRAYSCALE)
                        img_new = cv2.imshow("Captured Image", img_new)
                        cv2.waitKey(1650)
                        cv2.destroyAllWindows()
                        img_ = cv2.imread('testing.jpg', cv2.IMREAD_ANYCOLOR)
                        break
                    elif key == ord('q'):
                        webcam.release()
                        cv2.destroyAllWindows()
                        break
                    
                except(KeyboardInterrupt):
                    webcam.release()
                    cv2.destroyAllWindows()
                    break
                    
            shutil.move("testing.jpg", "media/testing/testing.jpg")

            name = classify_face("media/testing/testing.jpg")
            path = os.path.join("media/testing", "testing.jpg") 
            os.remove(path)
            if name[0] == "Unknown":
                messages.success(request, f'You are not a registered user')
            else:
                p = PublicData.objects.get(firstname=name[0])
                if p.voted == True :
                    messages.success(request, f'You have already voted')
                else:
                    p.voted = True 
                    p.ready = True
                    p.save()
                    messages.success(request, f'Successfully verified')
                    return render(request, 'public/goToVotingBooth.html')
            
    else:
        form = VotingRegForm(request.POST,request.FILES)
    
    return render(request,'public/voting_public.html')
