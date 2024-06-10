cmake_minimum_required(VERSION 3.5)
project(scene_segmentation_pillar)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Require that dependencies from package.xml be available
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(cv_bridge REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Install Python scripts
install(PROGRAMS
  scene_segmentation_pillar/scene_segmentation_node.py
  scene_segmentation_pillar/scene_segmentation.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install other files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)


# Install samples
install(DIRECTORY samples
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
