from tkinter import *

# Create the main window
window = Tk()
window.title('Instagram Profile Downloader')
window.geometry('600x600')
window.maxsize(600, 600)
window.minsize(600, 600)

window.title("Sum Calculator")


def calculate_sum():
    try:
        value1 = float(input1.get())
        value2 = float(input2.get())
        result = value1 + value2
        lableAnwer.config(text=f"Result: {result}")
    except ValueError:
        lableAnwer.config(text="Please enter valid numeric values.")

# Create input fields
input1 = Entry(window)
input2 = Entry(window)

# Create a label to display the result
lableAnwer = Label(window, text=" ")

# Create a button to trigger the calculation
button = Button(window, text="Calculate", command=calculate_sum)

# Pack widgets
input1.pack()
Label(window, text=" + ").pack()
input2.pack()
button.pack()
lableAnwer.pack()

# Start the main event loop
window.mainloop()

