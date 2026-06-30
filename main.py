import cv2
import mediapipe as mp

def is_peace_gesture(hand_landmarks):
    index_up = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y
    middle_up = hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y
    ring_down = hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y
    pinky_down = hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y
    return index_up and middle_up and ring_down and pinky_down

def process_frame(frame, hands, mp_hands, mp_draw):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    blur_active = False
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            if is_peace_gesture(hand_landmarks):
                blur_active = True
                break
                
    return frame, blur_active

def run_camera():
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils
    hands = mp_hands.Hands(
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7,
        max_num_hands=2
    )
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Kamera tidak dapat diakses.")
        return

    cv2.namedWindow("Foto Kita Blur", cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL)
    blur_weight = 0.0

    while True:
        success, frame = cap.read()
        if not success:
            break
            
        frame = cv2.flip(frame, 1)
        frame, blur_active = process_frame(frame, hands, mp_hands, mp_draw)
        
        blur_weight = min(1.0, blur_weight + 0.4) if blur_active else max(0.0, blur_weight - 0.4)
        
        if blur_weight > 0:
            ease = blur_weight * blur_weight * (3.0 - 2.0 * blur_weight)
            k = int(99 * ease)
            k = k if k % 2 != 0 else k + 1
            if k >= 3:
                blurred_frame = cv2.GaussianBlur(frame, (k, k), 0)
                frame = cv2.addWeighted(blurred_frame, ease, frame, 1.0 - ease, 0)
                        
        cv2.imshow("Foto Kita Blur", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_camera()
