import cv2

def Eye_tracker(result,resize_img,penalty,fluctuation):
    print('\nHitted Eyes tracker!')

    left_eye = result[0]['keypoints']['left_eye']
    right_eye = result[0]['keypoints']['right_eye']

    bounding_box = result[0]['box']
    eye_width = bounding_box[2] / 4
    eye_height = bounding_box[3] * 0.06

    w, h= int(eye_width) - 12, int(eye_height)
    x, y = left_eye
    x1, y1 = x - int(w / 2), y - 6
    left_eye = resize_img[abs(y1):abs(y1+h),abs(x1):abs(x1+w)]

    gray_left_eye = cv2.cvtColor(left_eye,cv2.COLOR_BGR2GRAY)
    _, gray_left_threshold = cv2.threshold(gray_left_eye,70,255,cv2.THRESH_BINARY)

    h, w = gray_left_threshold.shape
    left_side_threshold = gray_left_threshold[0:h , 0:int(w/2)]
    left_side_whiteL = cv2.countNonZero(left_side_threshold)

    right_side_threshold = gray_left_threshold[0:h , int(w/2):w]
    right_side_whiteL = cv2.countNonZero(right_side_threshold)

    w, h= int(eye_width) - 12, int(eye_height)
    x, y = right_eye
    x1, y1 = x - int(w / 2), y - 6
    right_eye = resize_img[abs(y1):abs(y1+h),abs(x1):abs(x1+w)] #left_top:height, 

    gray_right_eye = cv2.cvtColor(right_eye,cv2.COLOR_BGR2GRAY)
    _, gray_right_threshold = cv2.threshold(gray_right_eye,90,255,cv2.THRESH_BINARY)

    h, w = gray_right_threshold.shape
    left_side_threshold = gray_right_threshold[0:h , 0:int(w/2)]
    left_side_whiteR = cv2.countNonZero(left_side_threshold)

    right_side_threshold = gray_right_threshold[0:h , int(w/2):w]
    right_side_whiteR = cv2.countNonZero(right_side_threshold)

    gaze_ratio = 0
    if right_side_whiteL > 0 and right_side_whiteR > 0:
        left_eye_ratio = left_side_whiteL / right_side_whiteL 
        right_eye_ratio = left_side_whiteR / right_side_whiteR 

        gaze_ratio = ( left_eye_ratio + right_eye_ratio ) / 2

    print("*&*&*Gaze: ",gaze_ratio)
    if gaze_ratio >= 4:

        penalty = penalty + 1
        print('Looking at your Actual Right!',gaze_ratio)

    elif gaze_ratio <= 0.35:

        penalty = penalty + 1
        print('Looking at your Actual Left!',gaze_ratio)

    elif 2 < gaze_ratio > 0.25:
        penalty = 0

    return penalty,fluctuation