from setuptools import setup

package_name = 'scene_segmentation_pillar'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/scene_segmentation_launch.py']),
        ('share/' + package_name + '/samples', ['samples/test_video.mp4']),
    ],
   install_requires=[
        'setuptools',
        'cv_bridge',  
        'rclpy',
        'sensor_msgs',
        'std_msgs',
        'ultralytics', 
    ],
    zip_safe=True,
    maintainer='Panagiotis P. Filntisis',
    maintainer_email='pfilntisis@athenarc.gr',
    description='The scene_segmentation_pillar package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'scene_segmentation_node = scene_segmentation_pillar.scene_segmentation_node:main'
        ],
    },
)
