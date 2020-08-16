from Tkinter import *
from PIL import ImageGrab
import TrainAndCheck as network
import SpeakOutput
import os


count = 0


def redraw(event):
    canvas.delete('all')


def setval(event):
    global click_flag
    click_flag = True


def holdval(event):
    global click_flag
    click_flag = False


def motion(event):
    """This function track mouse pointer."""
    global i
    global click_flag
    if click_flag:
        x.set(event.x)
        y.set(event.y)
        canvas.create_oval(x.get(), y.get(), x.get()+12, y.get()+12, fill='black')
        i += 1


def getter(widget):
    global count
    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save('temp.jpg')
    text_area.configure(state=NORMAL)
    num_1, num_2 = network.initiate_operation(False, 'temp.jpg')
    os.remove('temp.jpg')

    if num_2 != 9 and num_1 != num_2:
        text_area.insert('end', 'More Probably: '+ str(num_1)+'\n')
        text_area.insert('end', 'Less Probably: ' + str(num_2)+'\n')
        x = 'Output is More Probably: ' + SpeakOutput.number_to_string(
            num_1) + 'Less Probably: ' + SpeakOutput.number_to_string(num_2)
    elif num_1 == num_2:
        x = 'output is ' + SpeakOutput.number_to_string(num_1)
        text_area.insert('end', str(num_1)+'\n')
    elif num_2 == 9:
        text_area.insert('end', 'More Probably: ' + str(num_2)+'\n')
        text_area.insert('end', 'Less Probably: ' + str(num_1)+'\n')
        x = 'Output is More Probably: ' + SpeakOutput.number_to_string(
            num_2) + 'Less Probably: ' + SpeakOutput.number_to_string(
            num_1)
    text_area.see('end')
    text_area.configure(state=DISABLED)
    SpeakOutput.speak_output(x)

    redraw(canvas)


def enterPressed(event):
    """This function checks if enter is pressed"""
    if event.keysym == 'Return':
        getter(canvas)


if __name__ == '__main__':

    l = ['navy', 'Dark Slate Blue', 'blue', 'green', 'yellow', 'orange', 'red']
    i = 0
    click_flag = False

    root = Tk()
    root.geometry('128x128+400+200')
    root.bind('<Button-3>', redraw)
    root.bind('<Motion>', motion)
    root.bind('<Button-1>', setval)
    root.bind('<ButtonRelease-1>', holdval)
    root.bind('<Return>', enterPressed)

    x = IntVar(root, 10)
    y = IntVar(root, 10)

    canvas = Canvas(root, bg='white', bd=10, height=128, width=128, cursor='dot')
    canvas.pack()

    text_area_provider = Toplevel(root)
    text_area_provider.resizable(width=False, height=False)
    text_area_provider.title("Output")
    text_area_provider.geometry('200x200+600+200')

    text_area = Text(text_area_provider, width=200, height=200)
    text_area.configure(state=DISABLED)

    v_scroll = Scrollbar(text_area_provider, orient=VERTICAL, command=text_area.yview)
    text_area['yscroll'] = v_scroll.set

    v_scroll.pack(side="right", fill="y")

    text_area.pack(side="left", fill="both", expand=True)


    root.mainloop()
