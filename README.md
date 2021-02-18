# CS 249r, Motion Controller Competition


# Learning Objectives



*   Demonstrate the many layers of a tinyML application pipeline and allow students to optimize different aspects of that pipeline for latency and accuracy.


# Relevant Chapters



*   Chapter 11, 12, 15


# Prerequisite(s) 



*   Previous assignments and ??


# Getting setup



*   Code setup
    *   Clone the repository
    *   Open AIoT-Dev-Summit-2019/ArduinoSketches/IMU_Classifier/ in your IDE
    *   Compile and upload the project to your device
*   Test the model
    *   Open the serial monitor
    *   Check to see that the classifier is working by moving the Arduino as shown in the video *insert video* 
    *   (Note: This will likely take numerous attempts due to the network being trained on data collected from a different board and a different user)
*   Connect the controller to the game
    *   Open dino_game_interface.py and change “port” to the port listed in the serial monitor
    *   Close the Arduino serial monitor
    *   Run “pip install pyautogui” and “pip install pyserial” in you terminal
    *   Open the game at this link: [http://www.trex-game.skipser.com/](http://www.trex-game.skipser.com/)
    *   Run “python dino_game_interface.py” in your terminal
    *   Click on the game window
    *   Try it out! (See video for an example)
    *   (Note: There is a significant input delay that makes playing the game almost impossible! You can do better!)


# Assignment 

The goal of this assignment is to get a high score in the dino jump game. To achieve this goal you must improve the motion controller pipeline, optimizing for latency and accuracy. You may optimize whichever section or sections of the pipeline you choose.



*   Possible areas for optimizations:
    *   Data
    *   Training
    *   Model design
    *   Feature engineering
    *   Inference
*   Restrictions:
    *   The controller must use ML inference
    *   The controller must data captured by the Arduino
    *   If you have an idea for an optimization and are unsure if it is allowed, please contact the staff. We will try to keep a FAQ up to date related to allowed modifications.
*   A good first step to improve accuracy is to collect your own motion data and retrain the model:
    *   Follow these instructions (Intro -> Exercise 7): [https://github.com/arduino/AIoT-Dev-Summit-2019](https://github.com/arduino/AIoT-Dev-Summit-2019)
        *   In “Exercise 5: Gather the Training Data” you can capture whatever type of motion you like to use as your inputs. (The baseline uses up and down motion)

# Submission Details



*   A video of you achieving your high score
    *   Must show the Arduino capturing the input and the game
*   Your modified project
    *   All files used in your pipeline
    *    A doc that lists all of your modifications and their purpose (Bonus if you demonstrate the latency/accuracy gain from that modification, can be qualitative or quantitative)
    *    All data collected and models trained.
*   Indicate collaborator

## Lingering Questions & Suggestions

Detail any questions you have about the material covered. Also, feel free to make suggestions for how this lab might be improved in the future.


# Supplementary Materials



*   References, links?
