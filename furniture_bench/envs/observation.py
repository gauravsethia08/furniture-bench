FULL_OBS = [
    "robot_state/ee_pos",
    "robot_state/ee_quat",
    "robot_state/ee_pos_vel",
    "robot_state/ee_ori_vel",
    "robot_state/gripper_width",
    "robot_state/joint_positions",
    "robot_state/joint_velocities",
    "robot_state/joint_torques",
    "robot_state/gripper_finger_1_pos",
    "robot_state/gripper_finger_2_pos",
    "color_image1",
    "depth_image1",
    "color_image2",
    "depth_image2",
    "color_image3",
    "depth_image3",
    "parts_poses",
    "obstacle_pose",
]

DEFAULT_VISUAL_OBS = [
    "robot_state/ee_pos",
    "robot_state/ee_quat",
    "robot_state/ee_pos_vel",
    "robot_state/ee_ori_vel",
    "robot_state/gripper_width",
    "color_image1",
    "color_image2",
]

DEFAULT_STATE_OBS = [
    "robot_state/ee_pos",
    "robot_state/ee_quat",
    "robot_state/ee_pos_vel",
    "robot_state/ee_ori_vel",
    "robot_state/gripper_width",
    "parts_poses",
]

FULL_BIMANUAL_OBS = [
    "robot_state/ee_pos",
    "robot_state/ee_quat",
    "robot_state/ee_pos_vel",
    "robot_state/ee_ori_vel",
    "robot_state/gripper_width",
    "robot_state/joint_positions",
    "robot_state/joint_velocities",
    "robot_state/joint_torques",
    "robot_state/gripper_finger_1_pos",
    "robot_state/gripper_finger_2_pos",
    # 2nd Arm
    "robot_state_2/ee_pos",
    "robot_state_2/ee_quat",
    "robot_state_2/ee_pos_vel",
    "robot_state_2/ee_ori_vel",
    "robot_state_2/gripper_width",
    "robot_state_2/joint_positions",
    "robot_state_2/joint_velocities",
    "robot_state_2/joint_torques",
    "robot_state_2/gripper_finger_1_pos",
    "robot_state_2/gripper_finger_2_pos",
    # Camera and other observations
    "color_image1",
    "depth_image1",
    "color_image2",
    "depth_image2",
    "color_image3",
    "depth_image3",
    "parts_poses",
    "obstacle_pose",
]

