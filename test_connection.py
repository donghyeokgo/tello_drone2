from djitellopy import Tello
import time

def test_connection():
    tello = Tello()
    try:
        print("드론에 연결 중...")
        tello.connect()
        print("✓ 연결 성공!")
        
        battery = tello.get_battery()
        print(f"✓ 배터리 잔량: {battery}%")
        
        if battery < 10:
            print("경고: 배터리가 너무 부족합니다")
            
    except Exception as e:
        print(f"❌ 연결 실패: {str(e)}")
    finally:
        tello.end()

if __name__ == "__main__":
    test_connection() 