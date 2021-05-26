import pybullet
import pybullet_data
import numpy as np
# https://www.guyuehome.com/22591
class Cheetah(object):
    def __init__(self):
        '''
        初始化参数
        pybullet客户端：pybullet的使用标准
        motor_id：用于设置电机角度，需要区分各个关节类型，这里为了方便直接给出了对应的编号。
        设置重力
        设置参数：addUserDebugParameter这个api提供用户自定义的参数，我这里设置成 髋关节角度
        设置视角：resetDebugVisualizerCamera这个api可以设置相机姿态
        当我们的类初始化的时候需要调用一次reset()函数来设置mini cheetah的姿态
        '''
        # self.pybullet_client = self._pybullet_client = bc.BulletClient(connection_mode=pybullet.GUI)
        self.pybullet_client = pybullet
        self.pybullet_client.connect(self.pybullet_client.GUI)
        self.pybullet_client.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.motor_id_list = [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14]
        self.pybullet_client.setGravity(0, 0, -9.8)
        # self.upper_angle = self.pybullet_client.addUserDebugParameter("upper_angle", 0, 1, 0.4)
        self.pybullet_client.resetDebugVisualizerCamera(0.2, 45, -30, [1, -1, 1])
        self.reset()

    def reset(self):
        '''
        环境复位
        导入地面
        导入mini_cheetah模型
        打印关节信息：getNumJoints用于获取关节信息
        调用reset_pos（）函数来设置每一条腿姿态
        '''
        init_position = [0, 0, 0.5]
        self._ground_id = self.pybullet_client.loadURDF('plane.urdf')
        self.quadruped = self.pybullet_client.loadURDF(
            "mini_cheetah/mini_cheetah.urdf",
            init_position,
            useFixedBase=False)

        num_joints = self.pybullet_client.getNumJoints(self.quadruped)
        for i in range(num_joints):
            print(self.pybullet_client.getJointInfo(self.quadruped, i))
        for i in range(4):
            self.reset_pos(i, 0.7853982)



    def step(self):
        '''
        执行动作
          由于这里只是演示，所以没有采用更高级的动作指令，这里实现的功能是根据时间动态调整mini_cheetah的离地高度(sin函数)。
          readUserDebugParameter这个api适用于读取用户自定的参数的，在__init__函数中已经初始化过了，
          我们可以通过滑块来调整离地高度，注意不能喝sin函数同时使用。
        '''
        t = 0
        while 1:
            t += 0.001
            angle = 0.4 * np.sin(t) + 0.5
            # angle = self.pybullet_client.readUserDebugParameter(self.upper_angle)
            for i in range(4):
                self.reset_pos(i, angle)
            self.pybullet_client.stepSimulation()

    def reset_pos(self, leg_id, angle):
        '''
        设置腿部姿态，setJointMotorControl2这个api是pybullet中最为常用的，
        因为控制关节都是通过这个api进行的。这里利用该api分别对髋关节和膝关节进行角度控制。
        '''
        l1 = 208
        l2 = 180
        hip_angle = 0.0
        upper_angle = -angle
        # 离地高度L与髋关节角度alpha的关系，在数学问题-初始姿态这篇文章介绍过该公式

        L = l1 * np.cos(angle) + np.sqrt(-l1 ** 2 * np.sin(angle) ** 2 + l2 ** 2)
        gamma = np.arccos((-l1 ** 2 + L ** 2 + l2 ** 2) / (2 * L * l2))
        beta = angle + gamma

        self.pybullet_client.setJointMotorControl2(self.quadruped,
                                                   jointIndex=self.motor_id_list[3 * leg_id],
                                                   controlMode=self.pybullet_client.POSITION_CONTROL,
                                                   targetPosition=hip_angle)
        self.pybullet_client.setJointMotorControl2(self.quadruped,
                                                   self.motor_id_list[3 * leg_id + 1],
                                                   self.pybullet_client.POSITION_CONTROL,
                                                   targetPosition=upper_angle)
        self.pybullet_client.setJointMotorControl2(self.quadruped,
                                                   self.motor_id_list[3 * leg_id + 2],
                                                   self.pybullet_client.POSITION_CONTROL,
                                                   targetPosition=beta)


if __name__ == '__main__':
    env = Cheetah()
    env.step()