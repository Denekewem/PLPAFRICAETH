# Assignment 1 & Activity 2 - Python OOP Practice

# ---------------------------
# Assignment 1: Design Your Own Class
# ---------------------------

class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.installed_apps = []

    def install_app(self, app_name):
        self.installed_apps.append(app_name)
        print(f"{app_name} installed on {self.model} ✅")

    def show_info(self):
        print(f"📱 {self.brand} {self.model} with {self.storage}GB storage")
        print("Installed Apps:", self.installed_apps if self.installed_apps else "None")


# Child class using Inheritance
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system):
        super().__init__(brand, model, storage)  # Call parent constructor
        self.cooling_system = cooling_system

    # Method Overriding (Polymorphism)
    def show_info(self):
        super().show_info()
        print(f"🎮 Equipped with {self.cooling_system} cooling system for gaming!")


# ---------------------------
# Activity 2: Polymorphism Challenge
# ---------------------------

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")


class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water...")


# ---------------------------
# Example Usage
# ---------------------------

if __name__ == "__main__":
    # Assignment 1 Demo
    print("=== Assignment 1: Smartphone Class ===")
    phone1 = Smartphone("Apple", "iPhone 15", 256)
    phone1.install_app("WhatsApp")
    phone1.show_info()

    print("\n---\n")

    phone2 = GamingPhone("Asus", "ROG Phone 6", 512, "Liquid Cooling")
    phone2.install_app("PUBG Mobile")
    phone2.show_info()

    print("\n=== Activity 2: Polymorphism Challenge ===")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()
