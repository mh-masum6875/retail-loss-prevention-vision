# Self-Checkout Scanning Verification Architecture
import cv2
import numpy as np

class SelfCheckoutVerifier:
    def __init__(self, scanner_poly, alert_line_y):
        self.scanner_poly = np.array(scanner_poly, np.int32)
        self.alert_line_y = alert_line_y
        self.scanned_items = 0
        self.unscanned_alerts = 0
        self.scan_in_progress = False

    def process_hand_interaction(self, hand_point, is_holding_object):
        # Step 1: Hand enters scanner polygon with item
        in_scanner = cv2.pointPolygonTest(self.scanner_poly, hand_point, False) >= 0
        if in_scanner and is_holding_object:
            self.scan_in_progress = True

        # Step 2: Hand crosses alert line towards bagging zone
        if hand_point[1] > self.alert_line_y and is_holding_object:
            if self.scan_in_progress:
                self.scanned_items += 1
                self.scan_in_progress = False
                return "ITEM_SCANNED_SUCCESS"
            else:
                self.unscanned_alerts += 1
                return "ALERT_ITEM_NOT_SCANNED"

        return "IDLE"

if __name__ == "__main__":
    print("SelfCheckoutVerifier pipeline initialized successfully.")
