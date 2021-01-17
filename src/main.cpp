#include <ros/ros.h> // include guard
//#include "rclcpp/rclcpp.hpp"

namespace N {
// code here
};

int main(int argc, char** argv)
{
    ros::init(argc, argv, "main_node");
    ros::NodeHandle nh;
    ros::AsyncSpinner spinner(1);
    spinner.start();
    ROS_INFO_STREAM("Running...");
    // rclcpp::init(argc, argv);

    ros::waitForShutdown();
}
