# Smart Canvas with Drowsiness Detection

This project combines a virtual drawing application with a real-time drowsiness detection system. It allows users to draw on a "canvas" using hand gestures captured by a webcam, while simultaneously monitoring for signs of user drowsiness and alerting them if detected.

## Features

* **Hand Gesture Drawing:** Draw on a virtual canvas using your finger movements.
* **Color Selection:** Choose from multiple colors (blue, green, red, yellow) for drawing.
* **Clear Canvas:** Easily clear the drawing on the canvas.
* **Real-time Drowsiness Detection:** Monitors your eye movements to detect if you are falling asleep.
* **Audible Drowsiness Alert:** Plays an alarm sound when drowsiness is detected.
* **Basic OCR (Optical Character Recognition):** Attempts to read text drawn on the canvas and evaluate it as a Python expression, displaying the result.

## Tech Stack

This project utilizes the following libraries and technologies:

* **OpenCV (`cv2`):** For real-time video capture, image processing, and drawing operations.
* **NumPy (`numpy`):** For numerical operations, especially with image arrays.
* **Mediapipe (`mediapipe`):** For hand landmark detection, enabling hand gesture recognition.
* **Dlib (`dlib`):** For robust face detection and facial landmark prediction (specifically for eye tracking).
* **SciPy (`scipy.spatial.distance`):** Used for calculating Euclidean distances, crucial for the Eye Aspect Ratio (EAR) calculation in drowsiness detection.
* **Pygame (`pygame`):** For playing the auditory alert sound when drowsiness is detected.
* **Pytesseract (`pytesseract`):** An OCR (Optical Character Recognition) tool used to extract text from the drawn canvas.
* **Python 3:** The core programming language.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Install the required libraries:**
    ```bash
    pip install opencv-python numpy mediapipe dlib scipy pygame pytesseract
    ```

3.  **Download Dlib's shape predictor model:**
    This project requires the `shape_predictor_68_face_landmarks.dat` file for facial landmark detection. You can download it from the dlib website or find it in various open-source dlib examples. **Place this file in the same directory as your script, or update the path in the script.**
    *(You currently have it at `/Users/abhijithmr/Downloads/shape_predictor_68_face_landmarks.dat`, consider placing it within your project directory for better portability.)*

4.  **Download an alert sound:**
    The project uses an MP3 file for the drowsiness alert. **Update the `ALERT_SOUND` variable in the script to point to your desired sound file.**
    *(You currently have it at `/Users/abhijithmr/Downloads/anthava.mp3`, consider placing it within your project directory for better portability.)*

5.  **Install Tesseract OCR Engine:**
    `pytesseract` is a Python wrapper for Google's Tesseract-OCR Engine. You need to install the Tesseract executable separately on your system.
    * **Windows:** Download the installer from [Tesseract-OCR GitHub](https://tesseract-ocr.github.io/tessdoc/Installation.html#windows)
    * **macOS:** `brew install tesseract`
    * **Linux (Debian/Ubuntu):** `sudo apt-get install tesseract-ocr`

    After installation, you might need to specify the path to the Tesseract executable if it's not in your system's PATH. You can do this by adding the following line at the beginning of your script (replace with your actual path):
    ```python
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # For Windows example
    ```

## How to Run

1.  Ensure your webcam is connected and accessible.
2.  Run the Python script:
    ```bash
   
    ```

## Usage

* A webcam feed window ("Output") and a drawing canvas window ("Paint") will appear.
* **Drawing:** Move your index finger in front of the camera to draw on the "Paint" window.
* **Color Selection:** Move your index finger over the colored rectangles at the top of the "Output" window to change the drawing color.
* **Clear Canvas:** Move your index finger over the "CLEAR" rectangle to wipe the canvas clean.
* **Drowsiness Detection:** The system will continuously monitor your eyes. If your eyes remain closed for a certain duration, an "DROWSINESS ALERT!" message will appear, and an alarm sound will play.
* **OCR:** Anything you draw on the canvas will periodically be analyzed by the OCR engine. If it recognizes a valid Python expression (e.g., "1 + 2", "5 * 3"), it will attempt to evaluate it and display the "Result" on the "Output" window.

## Contributing

Feel free to fork this repository, open issues, or submit pull requests.

## License

[ABHIJITH MR]
