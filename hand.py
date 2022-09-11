import cv2
from handUtils import HandDetector
from ssh import check_ssh
import paramiko
import os
from paramiko.ssh_exception import AuthenticationException

host_username = "mi"
host_password = "123"
camera = cv2.VideoCapture(-1)
hand_detector = HandDetector()

if __name__ == "__main__":
    # ssh - success
    t = check_ssh()
    try:
        a = t.connect(username=host_username, password=host_password)
    except AuthenticationException as e:
        print("账号或密码错误!")
    if a is None:
        sftp = paramiko.SFTPClient.from_transport(t)
        while True:
            success, img = camera.read()
            if success:
                img = cv2.flip(img, 1)
                h, w, c = img.shape
                hand_detector.process(img, draw=False)
                position = hand_detector.find_position(img)
                left_fingers = hand_detector.fingers_count('Left')
                print('left: ', left_fingers)
                with open("./temp/data.txt", "w") as f:
                    f.writelines(str(left_fingers))
                    f.close()
                sftp.put('./temp/data.txt', '/home/mi/temp/temp.txt')
                os.remove('./temp/data.txt')
                cv2.putText(img, str(left_fingers), (100, 150), cv2.FONT_HERSHEY_DUPLEX, 5, (0, 255, 0))

                #right_fingers = hand_detector.fingers_count('Right')
                #print('右手：', right_fingers)
                #cv2.putText(img, str(right_fingers), (w-200, 150), cv2.FONT_HERSHEY_DUPLEX, 5, (255, 0, 0))
                cv2.imshow('Video', img)
            k = cv2.waitKey(1)
            if k == ord('q'):
                break
        camera.release()
        cv2.destroyAllWindows()
        t.close()

