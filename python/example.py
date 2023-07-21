from kukavarproxy import *
import time
robot = KUKA('172.31.1.147')
pos_cur = robot.read("$POS_ACT")
print(pos_cur)
robot.write("C3BI_JOG_FRAME","{FRAME: X 1.0, Y 0.0, Z 0.0, A 0.0, B 0.0, C 0.0}")
robot.write("C3BI_JOG_FRAME","{FRAME: X 0.0, Y 0.0, Z 0.0, A 0.0, B 0.0, C 0.0}")
print (robot.read("C3BI_JOG_FRAME"))