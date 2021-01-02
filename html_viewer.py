from urllib.request import urlopen
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from time import sleep
from tkinter import ttk
from tkinter.messagebox import *
import pyperclip


root = Tk()
root.title("html viewer")
root.geometry('800x600')
root.config(background = "black")
root.resizable(False, False)

entry = Entry(root, width = 30)
entry.pack()
view = ScrolledText(root, wrap = WORD, width = 63, height = 25)
view.place(x = 150, y = 50)
show_btn = Button(root, text = "Show HTML")
show_btn.place(x = 150, y = 530)
copy_btn = Button(root, text = "Copy Html")
copy_btn.place(x = 400, y = 530)
#'http://python.org/'
progress_bar = ttk.Progressbar(root, orient = "horizontal", length = 286, mode  = 'determinate')
progress_bar.place(x = 340, y = 500)

def run_progressbar():
	progress_bar['maximum'] = 100
	for i in range(101):
		sleep(0.05)
		progress_bar['value'] = i
		progress_bar.update()
	progress_bar['value'] = 0

def get_html():
	link = entry.get()
	try:
		http_rsp = urlopen(link)
		#print(http_rsp)
		html = http_rsp.read()
		#print(html)
		html_decoded = html.decode()
		#print(html_decoded)
		run_progressbar()
		showinfo("Success", "succesfully gathered html!")
		view.config(state = NORMAL)
		view.delete(0.0, END)
		view.insert(END, html_decoded)
		view.config(state = DISABLED)
	except Exception as e:
		showerror("An Error Occured", e)
	else:
		return html_decoded
def copy_html():
	text = view.get(0.0, END)
	pyperclip.copy(text)

show_btn.config(command = get_html)
copy_btn.config(command = copy_html)
