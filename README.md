## Let's talk - ASL (American Sign Language) recognition

This project was completed in 10 days by:
https://github.com/plazinho
https://github.com/IlyaGaluzinskiy
https://github.com/aabdysheva

### Let's talk was build in order to recogize and translate ASL gestures in real-time using computer vision
- Let's talk currently able to recognize 39 gestures (26 letters, 10 words, 3 special signs)
- Let's talk was build using MediaPipe, OpenCV, Keras, Qt
- LSTM model for sign recognition was build using Keras and trained on dataset, that was collected during development (currently includes more than 5000 samples)
- user guide and list of available signs are located in the UI
- required libraries can be installed using requirements.txt file

Folder "for_model_training" includes scripts, that will allow you to create your own dataset.

![Ilya (3)](https://user-images.githubusercontent.com/74296883/138891986-08f1fd14-2428-4983-b23b-ef513d64a22e.gif)
