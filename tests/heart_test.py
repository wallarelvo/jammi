
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))

import jammi
import socket
import rospy
import zlib


def test_start():
    rospy.init_node("jammi_test", anonymous=False)
    host, port = "localhost", 5005
    rate = 20
    heart = jammi.Heart(host, port, rate)
    heart.data["name"] = "test"
    heart.start()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    i = 0
    while i < 20:
        i += 1
        data_zip, addr = sock.recvfrom(1024)
        data = zlib.decompress(data_zip)
        print i, data, addr
    heart.kill()


if __name__ == "__main__":
    test_start()