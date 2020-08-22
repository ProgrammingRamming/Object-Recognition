import numpy as np
import cv2
import pyttsx3

mobilecharger_cascade = cv2.CascadeClassifier('mobilecharger.xml')
face_cascade = cv2.CascadeClassifier('face.xml')
radio_cascade = cv2.CascadeClassifier('radio.xml')
blindstick_cascade = cv2.CascadeClassifier('blindstick.xml')
mobile_cascade = cv2.CascadeClassifier('mobile.xml')
toothbrush_cascade = cv2.CascadeClassifier('toothbrush.xml')
plate_cascade = cv2.CascadeClassifier('plate.xml')
spoon_cascade = cv2.CascadeClassifier('spoon.xml')
knife_cascade = cv2.CascadeClassifier('knife.xml')
sportshoes_cascade = cv2.CascadeClassifier('sportshoes.xml')
dustbin_cascade = cv2.CascadeClassifier('dustbin.xml')
wallet_cascade = cv2.CascadeClassifier('wallet.xml')
handwash_cascade = cv2.CascadeClassifier('handwash.xml')
watch_cascade = cv2.CascadeClassifier('watch.xml')
umbrella_cascade = cv2.CascadeClassifier('umbrella.xml')
sleeper_cascade=cv2.CascadeClassifier('sleeper.xml')
engine = pyttsx3.init()

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    word1="mobile charger is detected"
    word2="face is detected"
    word3="radio is detected"
    word4="blindstick is detected"
    word5="mobile is detected"
    word6="toothbrush is detected"
    word7="plate is detected"
    word8="spoon is detected"
    word9="knife is detected"
    word10="sport shoes is detected"
    word11="dustbin is detected"
    word12="wallet is detected"
    word13="handwash is detected"
    word14="watch is detected"
    word15="umbrella is detected"
    word16="sleeper is detected"

    mobilecharger = mobilecharger_cascade.detectMultiScale(gray,1.3, 5)
    for (x1,y1,w1,h1) in mobilecharger:
        print(word1)
        engine.say(word1)
        engine.setProperty('rate',100)
        engine.runAndWait()

    face = face_cascade.detectMultiScale(gray,1.3, 5)    
    for (x2,y2,w2,h2) in face:
        print(word2)
        engine.say(word2)
        engine.setProperty('rate',100)
        engine.runAndWait()


    radio = radio_cascade.detectMultiScale(gray,1.3, 5)    
    for (x3,y3,w3,h3) in radio:
        print(word3)
        engine.say(word3)
        engine.setProperty('rate',100)
        engine.runAndWait()

    blindstick = blindstick_cascade.detectMultiScale(gray,1.3, 5)    
    for (x4,y4,w4,h4) in blindstick:
        print(word4)
        engine.say(word4)
        engine.setProperty('rate',100)
        engine.runAndWait()


    mobile = mobile_cascade.detectMultiScale(gray,1.3, 5)    
    for (x5,y5,w5,h5) in mobile:
        print(word5)
        engine.say(word5)
        engine.setProperty('rate',100)
        engine.runAndWait()

    toothbrush = toothbrush_cascade.detectMultiScale(gray,1.3, 5)    
    for (x6,y6,w6,h6) in toothbrush:
        print(word6)
        engine.say(word6)
        engine.setProperty('rate',100)
        engine.runAndWait()

    plate = plate_cascade.detectMultiScale(gray,1.3, 5)    
    for (x7,y7,w7,h7) in plate:
        print(word7)
        engine.say(word7)
        engine.setProperty('rate',100)
        engine.runAndWait()

    spoon = spoon_cascade.detectMultiScale(gray,1.3, 5)    
    for (x8,y8,w8,h8) in spoon:
        print(word8)
        engine.say(word8)
        engine.setProperty('rate',100)
        engine.runAndWait()

    knife = knife_cascade.detectMultiScale(gray,1.3, 5)    
    for (x9,y9,w9,h9) in knife:
        print(word9)
        engine.say(word9)
        engine.setProperty('rate',100)
        engine.runAndWait()

    sportshoes = sportshoes_cascade.detectMultiScale(gray,1.3, 5)    
    for (x10,y10,w10,h10) in sportshoes:
        print(word10)
        engine.say(word10)
        engine.setProperty('rate',100)
        engine.runAndWait()

    dustbin = dustbin_cascade.detectMultiScale(gray,1.3, 5)    
    for (x11,y11,w11,h11) in dustbin:
        print(word11)
        engine.say(word11)
        engine.setProperty('rate',100)
        engine.runAndWait()

    wallet = wallet_cascade.detectMultiScale(gray,1.3, 5)    
    for (x12,y12,w12,h12) in wallet:
        print(word12)
        engine.say(word12)
        engine.setProperty('rate',100)
        engine.runAndWait()

    handwash= handwash_cascade.detectMultiScale(gray,1.3, 5)    
    for (x13,y13,w13,h13) in handwash:
        print(word13)
        engine.say(word13)
        engine.setProperty('rate',100)
        engine.runAndWait()

    watch = watch_cascade.detectMultiScale(gray,1.3, 5)    
    for (x14,y14,w14,h14) in watch:
        print(word14)
        engine.say(word14)
        engine.setProperty('rate',100)
        engine.runAndWait()


    umbrella = umbrella_cascade.detectMultiScale(gray,1.3, 5)    
    for (x15,y15,w15,h15) in umbrella:
        print(word15)
        engine.say(word15)
        engine.setProperty('rate',100)
        engine.runAndWait()

    sleeper = sleeper_cascade.detectMultiScale(gray,1.3, 5)    
    for (x16,y16,w16,h16) in sleeper:
        print(word16)
        engine.say(word16)
        engine.setProperty('rate',100)
        engine.runAndWait()
        
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

#engine = pyttsx3.init()
