import cv2
import selscript as S 




def getObjects(img,draw=True,objects=[]):
    
    classNames= []
    classFile='coco.names'
    with open(classFile,'rt') as f:
        classNames= f.read().rstrip('\n').split('\n')

    configPath='ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath='frozen_inference_graph.pb'

    net= cv2.dnn_DetectionModel(weightsPath,configPath)
    net.setInputSize(320,320)
    net.setInputScale(1.0/127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)


    classIds, confs, bbox = net.detect(img,confThreshold=0.5,nmsThreshold=0.2)
    objectInfo=[]
    if len(objects) == 0: objects= classNames
    if len(classIds) !=0:
        for classId, confidence, box in zip(classIds.flatten(),confs.flatten(),bbox):
            className=classNames[classId-1]
            if className in objects:
                    
                objectInfo.append([className])
                if(draw):
                    cv2.rectangle(img,box,color=(0,255,0),thickness=2)
                    cv2.putText(img,classNames[classId-1].upper(), (box[0]+10,box[1]+30), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

    return img,objectInfo




  
def main():

    #cap =cv2.VideoCapture('http://edonkey:8887/video', cv2.CAP_FFMPEG)
    cap =cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    i=0
    while True:
        success, img = cap.read()
        result, objectInfo = getObjects(img,True,['book'])
        if len(objectInfo) != 0:
            if i < 1:
                i+=1
                S.driDonkeyConst()
                
        elif len(objectInfo) == 0: 
            if i > 0:
                i=0
                S.stopDonkey()
        cv2.imshow("Output",img)
        cv2.waitKey(1)

main()