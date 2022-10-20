import mss
import cv2
import numpy as np
import time


def screen_record(): 
    
    last_time = time.time()
    m = mss.mss()
    
    while(True):

        screen = np.array(m.grab((0,40,800,640)))
        
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        
        cv2.imshow('window',screen)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        
screen_record()