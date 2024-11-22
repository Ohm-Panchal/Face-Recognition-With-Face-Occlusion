
# Final Project: Face Recognition with Occlusion Handling

## Project Overview
This project implements a face recognition system capable of handling occlusions and storing results effectively. It leverages Python for image processing, face detection, and recognition tasks, with modular scripts designed for different functionalities.

---

## Features
1. **Face Detection**:
   - Robust to occlusions.
   - Utilizes modern face detection algorithms.
2. **Face Recognition**:
   - Accurate recognition for stored identities.
3. **Storage Management**:
   - Efficient handling and retrieval of processed data.
4. **Result Visualization**:
   - Stores and displays processed images and results.
   
---

## Project Structure
- **images/**: Contains input image files.
- **results/**: Stores output and processed images.
- **config.py**: Configurations for thresholds, directories, and other settings.
- **f_face_detector_occlusion.py**: Handles face detection with occlusion support.
- **f_face_recognition.py**: Processes and identifies faces in input images.
- **f_main.py**: Central script connecting detection and recognition functionalities.
- **f_storage.py**: Manages the saving and retrieval of results.
- **main.py**: Primary script to run the application.

---

## Requirements
To set up and run the project, ensure the following dependencies are installed. Use the command:
```bash
pip install -r requirements.txt
```

---

## Installation
1. Clone the repository or extract the project files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## Configuration
Modify `config.py` to customize settings:
- **Thresholds**: Adjust for face detection sensitivity.
- **Directories**: Change paths for `images` and `results` directories.

---

## Usage
1. Place input images in the `images/` directory.
2. Run `main.py` to process the images.
3. Check the `results/` directory for output files.

---

## Future Enhancements
- Add support for video-based face recognition.
- Improve recognition under severe occlusions.
- Integrate with cloud storage for scalable storage management.

---

## Authors
Developed by the project team. For any queries or issues, contact [ohmpanchal99@gmail.com].

## Results
![image](https://github.com/Ohm-Panchal/Face-Recognition-With-Face-Occlusion/blob/main/results/res1.jpg)
![image](https://github.com/Ohm-Panchal/Face-Recognition-With-Face-Occlusion/blob/main/results/res5.jpg)

