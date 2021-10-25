import numpy as np


def extract_keypoints(results):
    if results.right_hand_landmarks:
        rh_centr_x = 0.5 - results.right_hand_landmarks.landmark[0].x
        rh_centr_y = 0.5 - results.right_hand_landmarks.landmark[0].y

        rh = np.array(
            [[res.x + rh_centr_x, res.y + rh_centr_y] for res in results.right_hand_landmarks.landmark]).flatten()
    else:
        rh = np.zeros(21 * 2)

    if results.left_hand_landmarks:
        lh_centr_x = 0.5 - results.left_hand_landmarks.landmark[0].x
        lh_centr_y = 0.5 - results.left_hand_landmarks.landmark[0].y

        lh = np.array(
            [[res.x + lh_centr_x, res.y + lh_centr_y] for res in results.left_hand_landmarks.landmark]).flatten()
    else:
        lh = np.zeros(21 * 2)
    return np.concatenate([rh, lh])
