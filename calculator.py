import tkinter 

#Setup buttons
button_values = [             
    ["AC", "<", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "+/-", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "<", "%"]

#Dimension of buttons
row_count=len(button_values)
column_count=len(button_values[0])

#Color value 
color_light_gray="#D4D4D2"
color_black="#1C1C1C"
color_dark_gray="#505050"
color_orange="#FF9500"
color_white="#FFFFFF"

#setup up the window
window=tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame=tkinter.Frame(window)
lable=tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black, foreground=color_white, anchor="e", width=column_count)
lable.grid(row=0, column=0, columnspan=column_count, sticky="we")

#window structure and styling
for row in range(row_count):
    for column in range(column_count):
        value=button_values[row][column]
        button=tkinter.Button(frame, text=value, font=("Arial", 20), height=1, width=column_count-1,  command=lambda values=value: button_click(values)) 
        button.grid(row=row+1, column=column)
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)
frame.pack()

# Enable keyboard input: map physical keys to calculator buttons
def on_key(event):
    """Map keyboard events to button values and invoke button_click."""
    key = event.keysym
    ch = event.char

    # special keys
    if key in ("Return", "KP_Enter"):
        val = "="
    elif key == "BackSpace":
        val = "<"
    elif key == "Escape":
        val = "AC"
    else:
        # printable characters
        if ch == '*':
            val = '×'
        elif ch == '/':
            val = '÷'
        elif ch == '%':
            val = '%'
        elif ch == '.':
            val = '.'
        elif ch in '0123456789':
            val = ch
        elif ch == '+':
            val = '+'
        elif ch == '-':
            val = '-'
        else:
            return  # ignore other keys

    try:
        button_click(val)
    except Exception:
        # swallow unexpected errors from key handling to avoid crashing
        pass

# ensure the window has focus so it receives key events
window.bind('<Key>', on_key)
window.focus_set()

#Giving the value to Buttons
A="0"
Operator=None
B=None

#Clear function to clear from the lable
def clear_all():    
    global A, B, Operator
    A="0"
    Operator=None
    B=None
#Remove zeros after any digit
def remove_zero_decimal(num):
    if num%1==0:
        num=int(num)
    return str(num)

#Most logic for buttons
def button_click(value):
   global right_symbols, top_symbols, lable, A, B, Operator

   if value in right_symbols:
       if value == "=":
           if A is not None and Operator is not None:
               B=lable["text"]
               numA=float(A)
               numB=float(B)
               
               if Operator=="+":
                   lable["text"]=remove_zero_decimal(numA + numB)
               elif Operator=="-":
                   lable["text"]=remove_zero_decimal(numA - numB)
               elif Operator=="×":
                   lable["text"]=remove_zero_decimal(numA * numB)
               elif Operator=="÷":
                   lable["text"]=remove_zero_decimal(numA / numB)

               clear_all()
                   
       elif value in "+-×÷":
           # If no operator yet, start a new operation
           if Operator is None:
               A = lable["text"]
               lable["text"] = "0"
               B = "0"
               Operator = value
           else:
               # If user changed their mind before entering second number (display still '0'),
               # just override the operator.
               if lable["text"] == "0":
                   Operator = value
               else:
                   # If a second operand exists, perform the pending operation, show result
                   # and start the next operation (chain calculations).
                   B = lable["text"]
                   try:
                       numA = float(A)
                       numB = float(B)
                       if Operator == "+":
                           result = numA + numB
                       elif Operator == "-":
                           result = numA - numB
                       elif Operator == "×":
                           result = numA * numB
                       elif Operator == "÷":
                           result = numA / numB
                       else:
                           result = numB

                       lable["text"] = remove_zero_decimal(result)
                       # prepare for next operation
                       A = lable["text"]
                       lable["text"] = "0"
                       B = "0"
                       Operator = value
                   except Exception:
                       # ignore errors (e.g., invalid float conversion or division by zero)
                       pass
   elif value in top_symbols:
       if value=="AC":
           clear_all()
           lable["text"]="0"
       elif value=="<":
           # backspace/delete: remove the last character from the label
           text = lable["text"]
           # if display is default '0', do nothing
           if text == "0":
               pass
           # if only one char left (or a lone '-' and one digit), reset to '0'
           elif len(text) <= 1 or (text.startswith("-") and len(text) == 2):
               lable["text"] = "0"
           else:
               lable["text"] = text[:-1]
               if lable["text"] in ("", "-0"):
                   lable["text"] = "0"
       elif value=="%":
           result=float(lable["text"])/100
           lable["text"]=remove_zero_decimal(result)
   else:
       if value == ".":
           if value not in lable["text"]:
               lable["text"] += value
       elif value=="+/-":
           result=float(lable["text"])*-1
           lable["text"]=remove_zero_decimal(result)
       elif value in "0123456789":
           if lable["text"] == "0":
               lable["text"] = value
           else:
               lable["text"] += value

#Window alighment to Center
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# calculate position x, y
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()