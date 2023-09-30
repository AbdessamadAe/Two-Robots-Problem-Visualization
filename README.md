# Two Robots Problem Visualization

![Thumbnail Image](thumbnail.png)

This repository contains a visualization of the "Two Robots Problem" using the Manim library. In this problem, two robots land on an infinite one-dimensional number line and need to meet using a specific set of functions.

## Problem Description
The problem statement is as follows:

Two robots land with their parachutes on an infinite one-dimensional number line. They both release their parachutes as soon as they land and start moving. They are allowed only to make use of the following functions:

1. `moveLeft()`: Robot moves to the left by 1 unit in 1 unit of time.
2. `moveRight()`: Robot moves to the right by 1 unit in 1 unit of time.
3. `noOperation()`: Robot does not move and takes 1 unit of time.
4. `onTopOfParachute()`: Returns true if the robot is standing on top of either of the parachutes, else false.
5. `didWeMeet()`: Returns true if the robot meets the other robot, else false.

## Visualization
This visualization demonstrates how the two robots use the provided functions to meet on the number line. The Manim library is used to animate their movements and visualize their progress.

## Usage
To run this visualization, you can use Manim. Here are the steps to render the video:

1. **Install Manim**: You can install Manim by following the instructions in the [Manim documentation](https://docs.manim.community/en/stable/installation.html).

2. **Run the Script**: Use the following command to render the video: ``manim -p -ql TwoRobots.py TwoRobotsProblem``

## Video Preview
[![Video Preview](video_preview.png)](link_to_your_video.mp4)

You can watch the full video on [YouTube](link_to_your_youtube_video).

## Author
- [Abdessamad Ait Elmouden](https://github.com/AbdessamadAe)
