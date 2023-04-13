# raspicat_description

ROS 2 package with URDF description macro for Raspberry Pi Cat

![](https://rt-net.github.io/images/raspberry-pi-cat/display_launch.png)

## Installation

```sh
# Clone raspicat_description and install dependencies
cd ~/catkin_ws/src
git clone -b ros2 https://github.com/rt-net/raspicat_description.git
rosdep install -r -y -i --from-paths .

# Build the package
cd ~/catkin_ws
colcon build --symlink-install
source ~/catkin_ws/install/setup.bash
```

## Usage

Display the Raspberry Pi Cat robot model on RViz with the following comand:

```sh
ros2 launch raspicat_description display.launch.py
```

See [RT Software Tutorials](https://rt-net.github.io/tutorials/raspicat/) for more detailed information.

## LICENSE

(C) 2021-2022 RT Corporation

This repository is licensed under the Apache License, Version 2.0, see [LICENSE](./LICENSE).  
Unless attributed otherwise, everything in this repository is under the Apache License, Version 2.0.

### Acknowledgements

Special thanks to https://gbiggs.github.io/rosjp_urdf_tutorial_text/index.html
