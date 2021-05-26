import pybullet
import time
import pybullet_data
import pybullet_utils.bullet_client as bullet_client

# 连接物理引擎
bullet_client.BulletClient(connection_mode=pybullet.GUI)