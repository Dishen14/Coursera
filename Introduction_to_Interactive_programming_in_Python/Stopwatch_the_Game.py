# template for "Stopwatch: The Game"

import simplegui

# define global variables
name = ""
t = 0; x = 0; y = 0; s = 0; interval = 100
v = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global a, b, c, d
    a = (int(t)//600)%10
    b = (int(t)//100)%6
    c = (t//10)%10
    d = (t%10)
    return str(a)+":"+str(b)+str(c)+"."+str(d)
    
# define event handlers for buttons; "Start", "Stop", "Reset", "Quit"
def start():
    global v
    timer.start()
    v = True
    
def stop():
    global v, x, y, s
    if v == True:
        timer.stop()
        v = False
        y += 1
        if t%10 == 0:
            x += 1
    s = x*100//y

def reset():
    global t, x, y, s
    t = 0; x = 0; y = 0; s = 0
    timer.stop()
    
    
def quit():
    timer.stop()
    frame.stop()
    
# define event handler for timer with 0.1 sec interval
def increment():
    global t
    t += 1
 
# print user user name
def print_name(text):
    global name
    name = text
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(t),(100,150),40,'Red')
    canvas.draw_text("STOPWATCH",(91,100),20,'White')
    canvas.draw_text("Name: "+name,(160,20),20,'Blue')
    canvas.draw_text("Score:"+str(x)+"/"+str(y),(160,40),20,'Blue')
    canvas.draw_text("Success:"+str(s)+"%",(160,60),20,'Blue')    
    
# create frame
frame = simplegui.create_frame("Stopwatch",300,200)

# register event handlers
timer = simplegui.create_timer(interval, increment)
frame.set_draw_handler(draw)
frame.add_input("Input Player Name:",print_name,100)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)
frame.add_button("Quit",quit,100)

# start frame
frame.start()

