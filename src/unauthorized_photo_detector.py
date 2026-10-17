# Unauthorized Smartphone Photography Detection
import numpy as np

def is_unauthorized_photo(phone_box, person_box):
    # Calculate phone orientation angle
    px1, py1, px2, py2 = phone_box
    width = px2 - px1
    height = py2 - py1
    angle = np.degrees(np.arctan2(height, width))
    
    # 50 to 150 degrees indicates upright camera shooting position
    is_upright = 50 <= angle <= 150
    
    # Verify phone is held in the upper torso (near eye/chest level)
    torso_top = person_box[1]
    torso_bottom = person_box[1] + (person_box[3] - person_box[1]) * 0.6
    phone_center_y = (py1 + py2) / 2
    
    is_chest_level = torso_top <= phone_center_y <= torso_bottom
    return is_upright and is_chest_level

if __name__ == "__main__":
    print("Unauthorized Photography Detector initialized.")
