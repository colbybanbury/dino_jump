# Dino Jump



## Getting setup

*   Code setup
    *   Clone the repository
    *   Open AIoT-Dev-Summit-2019/ArduinoSketches/IMU_Classifier/ in your IDE
    *   Compile and upload the project to your device
*   Test the model
    *   Open the serial monitor
    *   Check to see that the classifier is working by moving the Arduino up or down
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

This project is heavily based on [https://github.com/arduino/AIoT-Dev-Summit-2019](https://github.com/arduino/AIoT-Dev-Summit-2019).
Credit to Don Coleman, Sandeep Mistry, and Arduino.
