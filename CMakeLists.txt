cmake_minimum_required(VERSION 3.0.2)

# // To use this command correctly, remember to remove the build/ directory before running "cmake .." again
# set(CMAKE_TOOLCHAIN_FILE "/home/dangtran/vcpkg/scripts/buildsystems/vcpkg.cmake" )

# /*************************************
#  * HANDLE NUMPYCONFIG.H MISSING FILE *
#  *************************************/
#  # https://github.com/ethz-asl/numpy_eigen/issues/3
#  set(PYTHON_INCLUDE_DIRS ${PYTHON_INCLUDE_DIRS} /usr/local/lib/python2.7/dist-packages/numpy/core/include/)
#  include_directories(
#      include
#      ${PYTHON_INCLUDE_DIRS}
#  )

project(pddl_ros_tutorial C CXX) # Languages used in the project

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)
# set(CMAKE_CXX_STANDARD 11) # or
# set(CMAKE_C_STANDARD 99) # for C

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
    ########### Activate this if want to construct a `msg` or `srv`
    ########### Look at: 
    ###########     a. add_xxx_files(...)
    ###########     b. generate_messages(...)
    ###########     c. catkin_package(...)
    ###########     d. package.xml(...)
    # message_generation

    ########### Activate this if want to construct a `action` 
    ########### Look at: 
    ###########     a. add_xxx_files(...)
    ###########     b. generate_messages(...)
    ###########     c. catkin_package(...)
    ###########     d. package.xml(...)
    # actionlib
    # actionlib_msgs


    ########### For Working with python script, Loot at:
    ###########     a. catkin_install_python(...)
    ###########     b. chmod +x <path_file>
    roscpp
    rospy

    ########### For common message that we regularly work with ROS:
    # std_msgs
    # geometry_msgs
    # nav_msgs

    ########### For Manipulation robot
    # geometry_msgs
    # moveit_core
    # moveit_visual_tools
    # moveit_ros_planning
    # moveit_ros_planning_interface

    # moveit_task_constructor_core
    # rosparam_shortcuts
    # moveit_task_constructor_core
    # moveit_task_constructor_msgs
    # rviz_marker_tools
    # moveit_task_constructor_visualization
    # actionlib

    ########### Mesh MoveIt handling
    # geometric_shapes

    ########### For Mobile robot
    # map_server
    # amcl
    # slam
    # move_base

    ########## For Complex PDDL planning
    # rosplan



    ########## Transformation between frames:
    # tf

    ########## If want to work with planning + LTL through ompl
    ########## Download ompl: https://github.com/ompl/ompl
    ##########      into workspace directory.
    # ompl 
    # 


    ########## Good Reference for bionic hand:
    # Schunk bionic hand: https://github.com/fzi-forschungszentrum-informatik/schunk_svh_driver
    )

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)
# find_package(Eigen3 REQUIRED )

# enable_testing()                                  # Do not use if working with "catkin_add_gtest"
# find_package(GTest REQUIRED COMPONENTS system)    # Do not use if working with "catkin_add_gtest"


# find_path(package_INCLUDE_DIR package)
# find_library(package_LIBRARY package)
# message("package_include: ${package_INCLUDE_DIR}")
# message("package_library: ${package_LIBRARY}")

# message("package_include: ${Boost_INCLUDE_DIRS}")
# message("package_include: ${Boost_LIBRARY_DIRS}")

## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

## To declare and build messages, services or actions from within this
## package, follow these steps:
## * Let MSG_DEP_SET be the set of packages whose message types you use in
##   your messages/services/actions (e.g. std_msgs, actionlib_msgs, ...).
## * In the file package.xml:
##   * add a build_depend tag for "message_generation"
##   * add a build_depend and a exec_depend tag for each package in MSG_DEP_SET
##   * If MSG_DEP_SET isn't empty the following dependency has been pulled in
##     but can be declared for certainty nonetheless:
##     * add a exec_depend tag for "message_runtime"
## * In this file (CMakeLists.txt):
##   * add "message_generation" and every package in MSG_DEP_SET to
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * add "message_runtime" and every package in MSG_DEP_SET to
##     catkin_package(CATKIN_DEPENDS ...)
##   * uncomment the add_*_files sections below as needed
##     and list every .msg/.srv/.action file to be processed
##   * uncomment the generate_messages entry below
##   * add every package in MSG_DEP_SET to generate_messages(DEPENDENCIES ...)

## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate actions in the 'action' folder
# add_action_files(
#   DIRECTORY action
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
############ Activate this if want to construct a `msg` or `srv`
############ If your generated message/service is complicated:
############ Ex: nav_msgs/Odometry.msg
############    Header header
############    string child_frame_id
############    geometry_msgs/PoseWithCovariance pose
############    geometry_msgs/TwistWithCovariance twist
############    
############ This depends on geometry_msgs
# generate_messages(
#   DEPENDENCIES
#   std_msgs  # Or other packages containing msgs
#   actionlib_msgs # when working with actionlib
# )

################################################
## Declare ROS dynamic reconfigure parameters ##
################################################

## To declare and build dynamic reconfigure parameters within this
## package, follow these steps:
## * In the file package.xml:
##   * add a build_depend and a exec_depend tag for "dynamic_reconfigure"
## * In this file (CMakeLists.txt):
##   * add "dynamic_reconfigure" to
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * uncomment the "generate_dynamic_reconfigure_options" section below
##     and list every .cfg file to be processed

## Generate dynamic reconfigure parameters in the 'cfg' folder
# generate_dynamic_reconfigure_options(
#   cfg/DynReconf1.cfg
#   cfg/DynReconf2.cfg
# )

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if your package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
 INCLUDE_DIRS include
#  LIBRARIES sample_package
 CATKIN_DEPENDS 
    ########### Activate this if want to construct a `msg` or `srv`
    # message_runtime

    # actionlib_msgs # when working with actionlib
    roscpp rospy
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
    include
    ${catkin_INCLUDE_DIRS}
)

## Declare a C++ library
# add_library(${PROJECT_NAME}
#   src/${PROJECT_NAME}/sample_package.cpp
# )

## Add cmake target dependencies of the library
## as an example, code may need to be generated before libraries
## either from message generation or dynamic reconfigure
# add_dependencies(${PROJECT_NAME} ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Declare a C++ executable
## With catkin_make all packages are built within a single CMake context
## The recommended prefix ensures that target names across packages don't collide
# add_executable(${PROJECT_NAME}_node src/sample_package_node.cpp)

## Rename C++ executable without prefix
## The above recommended prefix causes long target names, the following renames the
## target back to the shorter version for ease of user use
## e.g. "rosrun someones_pkg node" instead of "rosrun someones_pkg someones_pkg_node"
# set_target_properties(${PROJECT_NAME}_node PROPERTIES OUTPUT_NAME node PREFIX "")

## Add cmake target dependencies of the executable
## same as for the library above
# add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
# target_link_libraries(${PROJECT_NAME}_node
#   ${catkin_LIBRARIES}
# )

add_executable(main_node src/main.cpp)
target_link_libraries(main_node
  ${catkin_LIBRARIES}
)

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
########### Activate this if want to work with python
# catkin_install_python(PROGRAMS
#   scripts/main_module.py
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark executables for installation
## See http://docs.ros.org/melodic/api/catkin/html/howto/format1/building_executables.html
# install(TARGETS ${PROJECT_NAME}_node
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark libraries for installation
## See http://docs.ros.org/melodic/api/catkin/html/howto/format1/building_libraries.html
# install(TARGETS ${PROJECT_NAME}
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
# )

## Mark cpp header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_sample_package.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

####### CMake-style test writting
# enable_testing()
# add_executable(test_node test/test_cpp/test_minimal.cpp)
# target_link_libraries(test_node ${catkin_LIBRARIES} pthread)
# add_test(NAME test_node_name COMMAND test_node)

####### Catkin-style test writting
# catkin_add_gtest(test_minimal_ros_node test/test_launch/test_cpp_ros/test_minimal_ros.cpp)
# target_link_libraries(test_minimal_ros_node ${catkin_LIBRARIES} pthread)

# catkin_add_gtest(test_moveit_ros_node test/test_launch/test_cpp_ros/test_moveit_ros.cpp)
# target_link_libraries(test_moveit_ros_node ${catkin_LIBRARIES} pthread)
####### Can use "rosrun <package_name> test_node" for running specific test (not rostest)

####### Catkin-style test writting for Python
# catkin_add_nosetests(test/test_launch/test_python_ros/test_minimal_ros.py)
####### With "chmod +x ..." 
####### we can use "rosrun <package_name> test_minimal_ros.py" for running specific test (not rostest)

####### Not recommend
# find_package(rostest REQUIRED)
# add_rostest(path_to_dot_test_file)

