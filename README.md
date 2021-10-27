## Let's talk - ASL (American Sign Language) recognition

This project was completed in 10 days by:
- https://github.com/IlyaGaluzinskiy
- https://github.com/plazinho
- https://github.com/aabdysheva

### Let's talk was build in order to recogize and translate ASL gestures in real-time using computer vision
- Let's talk currently able to recognize 39 gestures (26 letters, 10 words, 3 special signs)
- Let's talk was build using MediaPipe, OpenCV, Keras, Qt
- LSTM model for sign recognition was build using Keras and trained on dataset, that was collected during development (currently includes more than 5000 samples)
- user guide and list of available signs are located in the UI
- required libraries can be installed using requirements.txt file


![Ilya (3)](https://user-images.githubusercontent.com/74296883/138891986-08f1fd14-2428-4983-b23b-ef513d64a22e.gif)
Interface:
Top left corner of the screen - Top 3 signs that model predicts currently
Top of the screen - list of detected and written signs

## The process of sign recognition consists of following steps:
- Recieve video stream using OpenCV 
- Video frames are passed to MediaPipe Holistic model that detects hands and adds landmarks (21 landmarks per hand).
- MediaPipe recieves coordiantes for each landmark.
- Landmarks coordinates are extracted, organized and, if hands are detected, - passed to the model for prediction.
(Current prediction model build: 3 lstm layers and 1 fully-connected layer with softmax activation.)
- The visualization of model prediction is implemented in the top left corner of the program screen (see gif above). 
- Detected signs are translated to english and displayed on top of the screen (see gif above). 

## Create your own dataset.
Folder "for_model_training" includes scripts that were used for creation of dataset
- In order to build dataset for model training we used OpenCV (to work with video data) and MediaPipe (to extract key points)
- script 'for_checking_your_camera_and_mediapipe_model' - will allow you to check the visual component of MediaPipe and if it properly detects your hands.
### Steps for dataset creation:
- script 'creating_folders_for_dataset' can be used for creation of data folders for signs 
- script 'creating_dataset' is used to record coordinates for a certain sign and place it in previously created folder.
(dataset for the program was build by recording coordinates, specific for each gesture, including dynamic gestures (2 letters and 10 words). To widen the range of the dataset it was recorded by 3 pairs of hands.)
- script 'preparing_data' was build to organize and label data in order to pass it to the model
- script 'train_LSTM_model' - includes necessary functions to procces the data and pass it to the model
