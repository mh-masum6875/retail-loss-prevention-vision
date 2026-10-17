# Shoplifting Temporal Action State Machine Demo
class ShopliftingStateMachine:
    def __init__(self):
        self.state = "IDLE"
        self.shelf_touch_frames = 0
        self.pocket_touch_frames = 0

    def update(self, wrist_dist_shelf, wrist_dist_hip, is_holding):
        if self.state == "IDLE" and wrist_dist_shelf < 80:
            self.state = "HAND_IN_SHELF"
        elif self.state == "HAND_IN_SHELF" and is_holding:
            self.state = "TOOK_OBJECT"
        elif self.state == "TOOK_OBJECT" and wrist_dist_hip < 20:
            self.pocket_touch_frames += 1
            if self.pocket_touch_frames >= 10:
                self.state = "THEFT_ALERT"
                return "THEFT_DETECTED"
        return self.state

if __name__ == "__main__":
    detector = ShopliftingStateMachine()
    print("Shoplifting Action State Machine initialized.")
