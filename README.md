# raspicat_description

ROS package with URDF description macro for Raspberry Pi Cat

![](https://rt-net.github.io/images/raspberry-pi-cat/display_launch.png)

## Installation

```sh
# Clone raspicat_description and install dependencies
cd ~/catkin_ws/src
git clone https://github.com/rt-net/raspicat_description.git
rosdep install -r -y -i --from-paths .

# Build the package
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

## Usage

Display the Raspberry Pi Cat robot model on RViz with the following comand:

```sh
roslaunch raspicat_description display_xacro.launch 
```

See [RT Software Tutorials](https://rt-net.github.io/tutorials/raspicat/) for more detailed information.

## LICENSE

(C) 2021-2022 RT Corporation

This repository is licensed under the Apache License, Version 2.0, see [LICENSE](./LICENSE).  
Unless attributed otherwise, everything in this repository is under the Apache License, Version 2.0.

### Acknowledgements

Special thanks to https://gbiggs.github.io/rosjp_urdf_tutorial_text/index.html
