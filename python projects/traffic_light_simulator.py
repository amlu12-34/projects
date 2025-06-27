import tkinter as tk
import time

class TrafficLightSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light Simulator")
        self.root.geometry("200x500")
        self.root.configure(bg="black")

        self.canvas = tk.Canvas(self.root, width=150, height=400, bg="black")
        self.canvas.pack(pady=20)

        self.red_light = self.canvas.create_oval(30, 30, 120, 120, fill="grey")
        self.yellow_light = self.canvas.create_oval(30, 150, 120, 240, fill="grey")
        self.green_light = self.canvas.create_oval(30, 270, 120, 360, fill="grey")

        self.start_button = tk.Button(self.root, text="Start", font=("Arial", 14), command=self.start_simulation, bg="lightblue")
        self.start_button.pack(pady=20)

    def start_simulation(self):
        while True:
            self.set_light("red")
            self.root.update()
            time.sleep(3)

            self.set_light("yellow")
            self.root.update()
            time.sleep(1)

            self.set_light("green")
            self.root.update()
            time.sleep(3)

    def set_light(self, color):
        self.canvas.itemconfig(self.red_light, fill="red" if color == "red" else "grey")
        self.canvas.itemconfig(self.yellow_light, fill="yellow" if color == "yellow" else "grey")
        self.canvas.itemconfig(self.green_light, fill="green" if color == "green" else "grey")

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficLightSimulator(root)
    root.mainloop()
