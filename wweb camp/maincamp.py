import cv2
import time
import os
import glob
from emailling import send_email
from threading import Thread
video = cv2.VideoCapture(0)
time.sleep(1)
first_frame = None
status_list=[]
count =1

def clean_folder():
    print("clean folder startd")
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)
    print("clean folder ended")
while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    del_frame = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(del_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle=cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png",frame)
            count = count +1 
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) // 2)
            image_object = all_images[index]

    status_list.append(status)
    status_list=status_list[-2:]



    if status_list[-2:] == [0, 1]:
        email_thread = Thread(target=send_email, args=(image_object,))
        email_thread.daemon = True
        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True
 
        email_thread.start()
       
        # print("📩 Sending Email...")
        # send_email(image_object)
        # print("🧹 Cleaning folder...")
        # clean_folder()
    cv2.imshow("Video", frame)
    #rint(status_list)  
    key = cv2.waitKey(1)
    if key == ord("q"):
        break


clean_thread.start()

video.release()
cv2.destroyAllWindows()
