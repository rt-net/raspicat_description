# Copyright 2022-2023 RT Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import Command
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace


def generate_launch_description():
    lidar_frame = LaunchConfiguration('lidar_frame')
    namespace = LaunchConfiguration('namespace')
    use_rviz = LaunchConfiguration('use_rviz')
    
    declare_lidar = DeclareLaunchArgument(
        'lidar',
        default_value='none',
        description='Set "none", "urg", "lds", or "rplidar".')
    declare_lidar_frame = DeclareLaunchArgument(
        'lidar_frame',
        default_value='laser',
        description='Set lidar link name.')
    declare_namespace = DeclareLaunchArgument(
        'namespace',
        default_value='',
        description='Set namespace for tf tree.')
    declare_use_rviz = DeclareLaunchArgument(
        'use_rviz',
        default_value='true',
        description='Set "true" to launch rviz.')

    xacro_file = os.path.join(get_package_share_directory(
        'raspicat_description'), 'urdf', 'raspicat.urdf.xacro')
    params = {'robot_description':
              Command(['xacro ', xacro_file,
                       ' lidar_frame:=', lidar_frame, ]),
                        'frame_prefix': [namespace, '/']}

    push_ns = PushRosNamespace([LaunchConfiguration('namespace')])

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='both',
        parameters=[params])

    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen',
        condition=IfCondition(use_rviz))

    rviz_config_file = os.path.join(get_package_share_directory(
        'raspicat_description'), 'rviz', 'urdf.rviz')
    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='log',
        arguments=['-d', rviz_config_file],
        condition=IfCondition(use_rviz))

    ld = LaunchDescription()

    ld.add_action(declare_lidar)
    ld.add_action(declare_lidar_frame)
    ld.add_action(declare_namespace)
    ld.add_action(declare_use_rviz)
    
    ld.add_action(push_ns)
    ld.add_action(robot_state_publisher)
    ld.add_action(joint_state_publisher_gui)
    ld.add_action(rviz2)

    return(ld)
