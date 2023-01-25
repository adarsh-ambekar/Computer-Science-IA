
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import messagebox

class Cataloguer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry("500x500")
        self.title("The Cataloguer")

        # Center window
        self.update_idletasks()
        width = self.winfo_width()
        frm_width = self.winfo_rootx() - self.winfo_x()
        win_width = width + 2 * frm_width
        height = self.winfo_height()
        titlebar_height = self.winfo_rooty() - self.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.winfo_screenwidth() // 2 - win_width // 2
        y = self.winfo_screenheight() // 2 - win_height // 2
        self.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.deiconify()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LoginPage, HomePage, AccountInfo, ObjectsPage, CollectionsPage, ObjectSearchPage, IndividualCollectionPage, IndividualObjectPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=500)
        self.controller = controller
        label = tk.Label(self, text="Login", font=controller.title_font)
        label.pack(side="top", fill="x", pady=30)

        inputContainer = tk.Frame(self)
        inputContainer.pack(side="top")

        usernameLabel = tk.Label(inputContainer, text="Username")
        self.usernameTxt = tk.Entry(inputContainer, width=40)
        usernameLabel.grid(sticky="w", pady=5)
        self.usernameTxt.focus()
        self.usernameTxt.grid(sticky="w")

        whiteSpace = tk.Label(inputContainer)
        whiteSpace.grid(pady=20)


        passwordLabel = tk.Label(inputContainer, text="Password")
        self.passwordTxt = tk.Entry(inputContainer, show="*", width=40)
        passwordLabel.grid(sticky="w", pady=5)
        self.passwordTxt.grid(sticky="w")


        moreWhitespace = tk.Label(inputContainer)
        moreWhitespace.grid(pady=20)

        submitContainer = tk.Frame(inputContainer)
        submitContainer.grid()
        signInButton = tk.Button(submitContainer, text="Sign In",
                            command=self.signIn)
        signUpButton = tk.Button(submitContainer, text="Sign Up",
                            command=self.signUp)
        signInButton.grid(sticky="E", row=0, column=0, padx=50)
        signUpButton.grid(sticky="W", row=0, column=1, padx=50)

    def signIn(self, username, password):
        try:
            hashed_pwd = self.studentDb.loc[self.studentDb['username'] == username].iloc[0, 3]
            if 
                frame = self.frames["StudentHomepage"]
                frame.loadStudent(username)
                frame.tkraise()
                return True
            else:
                messagebox.showerror("Login Error", "Incorrect Username or Password")
        except:
            messagebox.showerror("Login Error", "Incorrect Username or Password")

    def signUp(self):
        pass

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=500)
        self.controller = controller


class AccountInfo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=500)
        self.controller = controller
        label = tk.Label(self, text="Account Info", font=controller.title_font)
        label.pack(side="top", fill="x", pady=30)

        inputContainer = tk.Frame(self)
        inputContainer.pack(side="top")

        usernameLabel = tk.Label(inputContainer, text="Username")
        self.usernameTxt = tk.Entry(inputContainer, width=40)
        usernameLabel.grid(sticky="w", pady=5)
        self.usernameTxt.focus()
        self.usernameTxt.grid(sticky="w")

class ObjectsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=500)
        self.controller = controller


class CollectionsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=500)
        self.controller = controller

class ObjectSearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=500)
        self.controller = controller


class IndividualCollectionPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=500)
        self.controller = controller


class IndividualObjectPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=500, height=500)
        self.controller = controller


if __name__ == "__main__":
    app = Cataloguer()
    app.mainloop()

