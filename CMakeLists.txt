cmake_minimum_required(VERSION 3.0.2)
project(raspicat_description)

find_package(catkin REQUIRED)

catkin_package()

#############
## Install ##
#############

install(DIRECTORY launch meshes urdf robots
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
