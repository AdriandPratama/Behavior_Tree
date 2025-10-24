import tkinter as tk
import random
import time
import threading

class AGV:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x, self.y = 50, 200
        self.battery = 100
        self.position = "route"
        self.status_text = canvas.create_text(250, 20, text="", font=("Arial", 12))
        self.battery_bar = canvas.create_rectangle(350, 10, 450, 30, fill="green")
        self.agv_shape = canvas.create_oval(self.x-10, self.y-10, self.x+10, self.y+10, fill="blue")
        self.alive = True

    def update_battery(self, amount):
        self.battery = max(0, min(100, self.battery + amount))
        color = "green" if self.battery > 50 else "yellow" if self.battery > 20 else "red"
        self.canvas.coords(self.battery_bar, 350, 10, 350 + self.battery, 30)
        self.canvas.itemconfig(self.battery_bar, fill=color)

    def move_to(self, target_x, target_y, speed=5):
        while abs(self.x - target_x) > 2 or abs(self.y - target_y) > 2:
            # kalau baterai <10, perlambat gerakan
            if self.battery < 10:
                speed = 2

            dx = speed if self.x < target_x else -speed if self.x > target_x else 0
            dy = speed if self.y < target_y else -speed if self.y > target_y else 0
            self.x += dx
            self.y += dy
            self.canvas.coords(self.agv_shape, self.x-10, self.y-10, self.x+10, self.y+10)
            self.update_battery(-0.5)
            self.canvas.update()
            time.sleep(0.05)

            # kalau baterai kritis tapi belum di charging, panggil auto rescue
            if self.battery <= 5 and self.position != "charge":
                self.set_status("Baterai kritis! Otomatis menuju tempat pengisian...")
                self.auto_to_charge()
                return False

            if not self.alive:
                return False
        return True

    def auto_to_charge(self):
        """Jalan pelan ke charging point kalau nyawa kritis."""
        charge_x, charge_y = 100, 350
        while abs(self.x - charge_x) > 2 or abs(self.y - charge_y) > 2:
            dx = 2 if self.x < charge_x else -2 if self.x > charge_x else 0
            dy = 2 if self.y < charge_y else -2 if self.y > charge_y else 0
            self.x += dx
            self.y += dy
            self.canvas.coords(self.agv_shape, self.x-10, self.y-10, self.x+10, self.y+10)
            self.canvas.update()
            time.sleep(0.1)
        self.position = "charge"
        self.set_status("Selamat! AGV berhasil mencapai charging station.")
        self.charge_battery()

    def charge_battery(self):
        """Isi ulang baterai sampai penuh."""
        self.set_status("Mengisi baterai...")
        while self.battery < 100:
            self.update_battery(+5)
            self.canvas.update()
            time.sleep(0.1)
        self.set_status("Baterai penuh. Kembali bekerja!")

    def set_status(self, text):
        self.canvas.itemconfig(self.status_text, text=text, fill="black")
        print(text)


class BehaviorTree:
    def __init__(self, agv):
        self.agv = agv
        self.points = {
            "pickup": (200, 100),
            "delivery": (400, 300),
            "charge": (100, 350),
        }

    def run(self):
        while self.agv.alive:
            if self.low_battery():
                self.handle_low_battery()
            else:
                self.main_task()

    def low_battery(self):
        return self.agv.battery < 20

    def handle_low_battery(self):
        self.agv.set_status("Baterai rendah, menuju charging station...")
        self.agv.move_to(*self.points["charge"])
        self.agv.position = "charge"
        self.agv.charge_battery()

    def main_task(self):
        # ke pickup
        self.agv.set_status("Menuju titik pengambilan barang...")
        if not self.agv.move_to(*self.points["pickup"]):
            return
        self.agv.position = "pickup"
        self.agv.set_status("Mengambil barang...")
        time.sleep(1)

        # ke delivery
        self.agv.set_status("Menuju titik pengiriman...")
        if not self.agv.move_to(*self.points["delivery"]):
            return
        self.agv.position = "delivery"
        self.agv.set_status("Mengirim barang...")
        time.sleep(1)

        self.agv.set_status("Tugas selesai. Kembali ke rute.")
        self.agv.position = "route"


def start_simulation():
    agv.set_status("Memulai simulasi AGV...")
    tree = BehaviorTree(agv)
    tree.run()


root = tk.Tk()
root.title("Simulasi AGV - Behavior Tree")
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

canvas.create_text(200, 80, text="Pickup", font=("Arial", 10))
canvas.create_oval(190, 90, 210, 110, fill="orange")

canvas.create_text(400, 280, text="Delivery", font=("Arial", 10))
canvas.create_oval(390, 290, 410, 310, fill="lightblue")

canvas.create_text(100, 330, text="Charging", font=("Arial", 10))
canvas.create_oval(90, 340, 110, 360, fill="green")

agv = AGV(canvas)

thread = threading.Thread(target=start_simulation, daemon=True)
thread.start()

root.mainloop()
