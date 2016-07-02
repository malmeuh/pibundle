"""
@author: Blefaudeux
"""
import cv2           # OpenCV
import frameGrabber  # Wrap the frame grabbing process


def run():

    # Get the inputs
    frame_source = frameGrabber.PictsFile('ref_picts/padding')

    import Queue
    pict_queue = Queue.Queue()
    frame_source.populate(pict_queue, 1)

    cv2.namedWindow("Picture viewer")

    while True:
        try:
            pic = pict_queue.get(block=True, timeout=50)

        except Queue.Empty:
            print "No more frames"
            break

        cv2.imshow("Picture viewer", pic)

        print "Got a new frame"

    print "Bybye.."

    frame_source.release()


if __name__ == "__main__":
    run()