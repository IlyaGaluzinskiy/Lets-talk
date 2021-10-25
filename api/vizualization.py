import cv2


def prob_viz(res, actions, input_frame, colors):
    output_frame = input_frame.copy()

    # viz top3
    i = 0
    for num, prob in sorted(enumerate(res), key=lambda x: x[1], reverse=True)[:3]:
        cv2.putText(output_frame, 'Top3 predictions', (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
                    cv2.LINE_AA)
        cv2.putText(output_frame, 'Probability', (300, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
                    cv2.LINE_AA)
        cv2.rectangle(output_frame, (10, 95 + i), (10 + int(prob * 200), 125 + i), colors[num], -1)
        cv2.putText(output_frame, actions[num], (10, 120 + i), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
                    cv2.LINE_AA)
        cv2.putText(output_frame, str(round(prob, 2)), (300, 120 + i), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
                    cv2.LINE_AA)
        i += 40

    return output_frame
