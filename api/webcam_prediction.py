import numpy as np
import cv2
from PyQt5 import QtWidgets

from api.mediapipe_model import mp_holistic, mediapipe_detection, draw_styled_landmarks
from api.extract_keypoints import extract_keypoints
from api.LSTM_model import model
from api.loader import actions, colors
from api.vizualization import prob_viz

from ui_editor.start_ui import Ui_Start

sentence = []
start_pause_predictions = []


def camera_start():
    global sentence, start_pause_predictions
    # 1. New detection variables
    text = []
    sequence = []

    predictions = []
    threshold = 0.7

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)

    # Set mediapipe model
    cv2.namedWindow("Let's talk")  # Create a named window
    cv2.moveWindow("Let's talk", 0, 0)

    # Initiation of widget
    Form = QtWidgets.QWidget()
    ui_start = Ui_Start()
    ui_start.setupUi(Form)
    Form.show()

    with mp_holistic.Holistic(model_complexity=1, min_detection_confidence=0.5,
                              min_tracking_confidence=0.5) as holistic:
        while cap.isOpened():

            # Read feed
            ret, frame = cap.read()
            # Make detections
            image, results = mediapipe_detection(frame, holistic)

            # Draw landmarks
            draw_styled_landmarks(image, results)

            # 2. Prediction logic
            keypoints = extract_keypoints(results)
            sequence.append(keypoints)
            sequence = sequence[-30:]

            if len(start_pause_predictions) == 0 or start_pause_predictions[-1] == 'model_start':
                cv2.circle(image, (1190, 90), 24, (0, 0, 255), -1)
            else:
                cv2.circle(image, (1190, 90), 24, (0, 255, 0), -1)
            if len(sequence) == 30:
                res = model.predict(np.expand_dims(sequence, axis=0))[0]
                current_prediction = np.argmax(res)
                name_current_prediction = actions[current_prediction]

                if res[current_prediction] > threshold:
                    predictions.append(current_prediction)
                    last_predictions = np.unique(predictions[-12:])

                    if len(last_predictions) == 1 and last_predictions[0] == current_prediction:

                        if name_current_prediction == 'model_start' or name_current_prediction == 'model_stop':
                            start_pause_predictions.append(name_current_prediction)

                        if len(start_pause_predictions) == 0 or start_pause_predictions[-1] == 'model_start':
                            if actions[current_prediction] == 'NaN':
                                if len(sentence) > 0:
                                    fixed = [i if len(i) == 1 else f' {i} ' for i in sentence]
                                    text.extend(''.join(fixed).strip().replace('  ', ' ').split())
                                    text[-1] = text[-1] + '.'
                                    ui_start.start_window.setPlainText(' '.join(text))  # update 'prediction window'
                                    sentence = []

                            elif name_current_prediction != 'model_start':
                                if len(sentence) > 0:
                                    if name_current_prediction.lower() != sentence[-1].lower():
                                        sentence.append(name_current_prediction)
                                else:
                                    sentence.append(
                                        name_current_prediction.capitalize())  # first letter/word capitalize

                # Viz probabilities
                image = prob_viz(res, actions, image, colors)

            cv2.rectangle(image, (0, 0), (1280, 40), (188, 143, 143), -1)
            cv2.putText(image, ' '.join(sentence[-15:]), (3, 30),  # last 15 elements
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            # Show to screen
            cv2.imshow("Let's talk", image)
            # Break gracefully
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            if cv2.getWindowProperty("Let's talk", cv2.WND_PROP_VISIBLE) < 1:
                break

        cap.release()
        cv2.destroyAllWindows()
        Form.close()
