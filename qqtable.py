import win32gui
import win32con
import win32api
from pynput import keyboard, mouse
from pynput.mouse import Controller
from pynput.keyboard import Key, Listener



# 获取屏幕的设备上下文
hdc = win32gui.GetDC(0)
# 设置线段的起始和结束点坐标
start_x, start_y = 100, 100
end_x, end_y = 400, 400

# 绘制线段
    # win32gui.MoveToEx(hdc, start_x, start_y)
    # win32gui.LineTo(hdc, end_x, end_y)
    # # 释放设备上下文
    # win32gui.ReleaseDC(0, hdc)


# 创建一个鼠标控制器对象
mouse = Controller()

# 获取当前鼠标的坐标
current_position = mouse.position

def on_press(key):
    global start_x,start_y,end_x,end_y,hdc  # 使用 global 关键字声明变量
    try:
        if key == Key.esc:
            # 如果按下的是 "Esc" 键，则停止监听
            return False
        elif key.char == 'q':

            print("按下了 'q' 键")
            print("当前鼠标的坐标是",mouse.position)
            start_x=mouse.position[0]
            start_y=mouse.position[1]
            win32gui.MoveToEx(hdc, start_x, start_y)
        elif key.char == 'w':
            print("按下了 'w' 键")
            print("当前鼠标的坐标是",mouse.position)
            # win32gui.MoveToEx(hdc, start_x, start_y)
            end_x=mouse.position[0]
            end_y=mouse.position[1]
            win32gui.LineTo(hdc, end_x, end_y)
        elif key.char == 'e':
            print("按下了 'e' 键")
            print("当前鼠标的坐标是",mouse.position)
            win32gui.MoveToEx(hdc, start_x, start_y)
            win32gui.LineTo(hdc, end_x, end_y)

    except AttributeError:
        # 如果按下的不是普通字符键（例如功能键），则忽略
        pass

# 创建一个键盘监听器
with Listener(on_press=on_press) as listener:
    # 启动监听器
    listener.join()