## Let's talk - ASL (American Sign Language) recognition

This project was completed in 10 days by:
- https://github.com/IlyaGaluzinskiy
- https://github.com/plazinho
- https://github.com/aabdysheva

### Let's talk was created in order to recogize and translate ASL gestures in real-time using computer vision
- Let's talk currently able to recognize 39 gestures: 26 letters, 10 words, 3 special signs. 12 of them are dynamic gestures
- Let's talk was created using MediaPipe, OpenCV, Keras, PyQt
- LSTM model for sign recognition was built using Keras and trained on dataset, that was collected during development (currently includes more than 5000 samples)
- Prediction model architecture: 3 LSTM layers with Relu activation and a fully-connected output layer with softmax activation.
- user guide and list of available signs are located in the UI


![Ilya (3)](https://user-images.githubusercontent.com/74296883/138891986-08f1fd14-2428-4983-b23b-ef513d64a22e.gif)
- Interface:
- Top left corner of the screen - Top 3 signs that model predicts currently
- Top of the screen - list of detected and written signs

### The process of sign recognition consists of following steps:
- Recieve video stream using OpenCV 
- Video frames are passed to MediaPipe Holistic model that detects hands, adds landmarks (21 landmarks per hand), recording their coordinates.
- Landmarks coordinates are extracted, organized and passed to the model for prediction.
- The visualization of model prediction is implemented in the top left corner of the program screen (see gif above). 
- Detected signs are translated to english and displayed on top of the screen (see gif above). 

### In order to start Let's talk on your machine:
- Clone repository
- Install required libraries (pip install -r requirements.txt)
- Run 'main_ui.py' to start the app

### Create your own dataset.
Folder "for_model_training" includes scripts that were used for creation of dataset.
- script 'for_checking_your_camera_and_mediapipe_model' - to check the visual component of MediaPipe working process and if it properly detects your hands.
#### Steps for dataset creation:
- script 'creating_folders_for_dataset' - for creation of signs data folders  
- script 'creating_dataset' - to record coordinates for a certain sign and place it in the previously created folder.
(dataset for the app was built by recording coordinates, specific for each gesture, including dynamic gestures (2 letters and 10 words). To widen the range of the dataset it was recorded by 3 people.)
- script 'preparing_data' - to organize and label data in order to pass it to the model
- script 'train_LSTM_model' - includes necessary functions to procces the data and pass it to the model
