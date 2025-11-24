
#  tasks for learning ros2 humble

---------------------------------------------------------

TASK 1 — Basic Publisher & Subscriber 

Create a simple ROS2 pipeline with:
- a publisher that publishes a string message 
- a subscriber that reads and prints the message
- both nodes display the message number and text

How to Run
Terminal 1:
cd ~/ros2_ws
source install/setup.bash
ros2 run task1_first_try publisher_node

Terminal 2:
cd ~/ros2_ws
source install/setup.bash
ros2 run task1_first_try subscriber_node

---------------------------------------------------------

TASK 2 — Publisher & Subscriber Point

Repeat Task 1 but use geometry_msgs instead of String.

Point message structure:
float64 x
float64 y
float64 z

Publisher Behavior
Publishing Point #1 -> x=0.21, y=-1.5, z=3.0

Subscriber Behavior
Received Point #1 -> x=0.21, y=-1.5, z=3.0

How to Run
Terminal 1:
cd ~/ros2_ws
source install/setup.bash
ros2 run task2 publisher_node

Terminal 2:
cd ~/ros2_ws
source install/setup.bash
ros2 run task2 subscriber_node

---------------------------------------------------------

TASK 4 — Publisher & Subscriber Service


Create a complete ROS2 pipeline that:
1. Publishes random shapes & colors 
2. Subscribes and detects a specific color
3. Provides a service /next_color to change target color dynamically

How to Run

Terminal 1 — Publisher
cd ~/ros2_ws
source install/setup.bash
ros2 run task4 publisher_node

Terminal 2 — Subscriber + Service
cd ~/ros2_ws
source install/setup.bash
ros2 run task4 subscriber_node

Terminal 3 — Service Call
ros2 service list
ros2 service call /next_color example_interfaces/srv/Trigger "{}"



---------------------------------------------------------

