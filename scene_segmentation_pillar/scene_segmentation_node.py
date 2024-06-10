import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import os
import sys
from ament_index_python.packages import get_package_share_directory

# Initialize package path
# package_path = get_package_share_directory('scene_segmentation_pillar')
# scene_segmentation_path = os.path.join(package_path, 'scripts')
# sys.path.append(scene_segmentation_path)
# from scene_segmentation import SceneSegmenterNode as SegmentationNode
from scene_segmentation_pillar.scene_segmentation import SceneSegmenter


class SceneSegmenterNode(Node):
    def __init__(self):
        super().__init__('scene_segmentation_node')
        
        # Initialize the CvBridge and SceneSegmenter
        self.bridge = CvBridge()
        self.scene_segmenter = SceneSegmenter()
        
        # Subscribe to the input video feed and publish annotated images
        self.image_sub = self.create_subscription(
            Image, '/xtion/rgb/image_raw', self.image_callback, 10)
        self.image_pub = self.create_publisher(Image, '/scene_segmentation/image', 10)

    def image_callback(self, data):
        try:
            # Convert the ROS image message to a CV2 image
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            self.get_logger().error('CvBridgeError: {0}'.format(e))
            return

        print("Received image", cv_image.shape)
        # Perform scene segmentation on the converted CV2 image
        results = self.scene_segmenter.track(cv_image, verbose=True)
        for result in results:
            self.get_logger().info("Boxes: %s" % result.boxes)
            self.get_logger().info("Masks: %s" % result.masks)

        # Optionally, to publish the result as a ROS Image message
        # Annotate `cv_image` here if you want to visualize the tracking results
        # Then convert it back to a ROS Image message and publish it
        try:
            ros_image = self.bridge.cv2_to_imgmsg(cv_image, "bgr8")
            self.image_pub.publish(ros_image)
        except CvBridgeError as e:
            self.get_logger().error('CvBridgeError: {0}'.format(e))


def main(args=None):
    rclpy.init(args=args)
    node = SceneSegmenterNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
