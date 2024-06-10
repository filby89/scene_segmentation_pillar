from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='scene_segmentation_pillar',
            executable='scene_segmentation_node',
            name='scene_segmentation_node',
            output='screen'
        )
    ])
