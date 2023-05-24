import time

def pomodoro_timer(total_time, focus_time, break_time):
    print("Pomodoro Timer started!\n")
    
    while total_time > 0:
        print("Focus time remaining: {} seconds".format(focus_time))
        time.sleep(1)
        focus_time -= 1
        total_time -= 1
        
        if focus_time == 0:
            print("\nFocus time over. Take a break!\n")
            
            while break_time > 0:
                print("Break time remaining: {} seconds".format(break_time))
                time.sleep(1)
                break_time -= 1
                total_time -= 1
                
        if break_time == 0:
            print("\nBreak time over. Back to focus!\n")
            focus_time = input("Enter the focus time (in seconds): ")
            break_time = input("Enter the break time (in seconds): ")
    
    print("\nTimer completed!")

# 输入总时长、专注时间和休息时间（以秒为单位）
total_time = int(input("Enter the total time (in seconds): "))
focus_time = int(input("Enter the focus time (in seconds): "))
break_time = int(input("Enter the break time (in seconds): "))

pomodoro_timer(total_time, focus_time, break_time)
