import cv2
import numpy
from PIL import ImageGrab

def screenRecorder():
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1920, 1080))
    while True:
        img = ImageGrab.grab()
        img_np = numpy.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow("Screen Recorder", img_final)
        out.write(img_final)

        if cv2.waitKey(1) == 27:
            break

    out.release()
    cv2.destroyAllWindows()

screenRecorder()
