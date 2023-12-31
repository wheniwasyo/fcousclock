import time

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        minutes_remaining = seconds // 60
        seconds_remaining = seconds % 60
        print(f"倒计时：{minutes_remaining:02d}:{seconds_remaining:02d}")
        time.sleep(1)
        seconds -= 1
    print("专注时间结束！")

pomodoro_timer(25)  # 设置专注时间为25分
