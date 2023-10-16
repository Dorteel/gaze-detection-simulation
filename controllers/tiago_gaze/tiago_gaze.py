
from controller import Robot, Camera, Motor

robot = Robot()

timestep = int(robot.getBasicTimeStep())

camera = robot.getDevice('camera')
camera.enable(timestep)

YAW_MAX = 1.24
YAW_MIN = -1.24
PITCH_MAX = 0.79
PITCH_MIN = -0.98

look_yaw = head_1_joint
look_pitch = head_2_joint


while robot.step(timestep) != -1:
    val = camera.getImage()
    pass


