import cv2
# tracker = cv2.legacy.TrackerBoosting_create()
tracker = cv2.TrackerMIL_create()
# tracker = cv2.legacy.TrackerKCF_create()
# tracker = cv2.legacy.TrackerTLD_create()
# tracker = cv2.legacy.TrackerMedianFlow_create()
    
tracker_name = str(tracker).split()[0][1:]
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
ret, frame = cap.read()

roi = cv2.selectROI(frame, False)
ret = tracker.init(frame,roi)

while True:
    ret, frame = cap.read()
    success, roi = tracker.update(frame)
    (x,y,w,h) = tuple(map(int,roi))
    if success:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),3)
    else:
        cv2.putText(frame, "failed",(200,200),cv2.FONT_HERSHEY_SIMPLEX,5,color=(255,255,255), thickness=3, lineType=cv2.LINE_AA)
    cv2.imshow(tracker_name,frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
