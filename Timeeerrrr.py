import customtkinter
import pygame

class MyTimer:
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry("170x155")
        self.app.title("Timer")

        self.is_running = False
        self.z = 10
        self.p = 6
        self.y = 1
        

        self.Zeitfenster = customtkinter.CTkLabel(self.app,font=("Arial", 40), text=":", fg_color="transparent",width=100, height=50, corner_radius=50)
        self.Zeitfenster.grid(row=0, column=0, columnspan=2, padx=30, pady=10)

        #self.NewTimebutton = customtkinter.CTkButton(
           # self.app, text="Time", width=20, height=20,corner_radius=30,
           # font=("Arial", 16,)) 
        #self.NewTimebutton.grid(row=3, column=1, padx=10, pady=10)


        self.Resetbutton = customtkinter.CTkButton(
            self.app, text="Reset", width=20, height=20,corner_radius=30,
            font=("Arial", 16,)) 
        self.Resetbutton.grid(row=3, column=0, padx=10, pady=10)

        self.startbutton = customtkinter.CTkButton(
            self.app, text="Start", width=20, height=20,corner_radius=30,
            font=("Arial", 16), command=self.count) 
        self.startbutton.grid(row=2, column=0, padx=10, pady=3)

        self.pausebutton = customtkinter.CTkButton(
            self.app, text="Pause", width=20, height=20,corner_radius=30, command=self.stop, 
            font=("Arial", 16)
        )
        self.pausebutton.grid(row=2, column=1, padx=10, pady=3)



    def count(self): 
            
            if self.z > 0:
                self.z -= 1
                self.Zeitfenster.configure(text=str(self.z))
                self.y = self.Zeitfenster.after(1000, self.count)
                self.breaktime()
                        

    def breaktime(self):
      
        if self.z == 0 and self.p > 0:
           
            self.p -= 1
            self.Zeitfenster.configure(text=str(self.p))
            self.y =self.Zeitfenster.after(1000, self.breaktime)
            if self.p == 0:
                self.count()
            
    # falls ich diese Funktion später noch einbauen will 
    #def NewTimebutton(self):      
       # pass     


    def stop(self):
        
        self.Zeitfenster.configure(text=str(self.z))
        self.Zeitfenster.after_cancel(self.y)


        
    def buildApp(self):
        self.app.mainloop()



countdown = MyTimer()
countdown.buildApp()



