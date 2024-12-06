
import math
import turtle

class UniversalGravity:
    G = 6.67430e-11  

class Sun:
    def __init__(self, name, mass, radius, temp):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.temp = temp
        self.x = 0.0
        self.y = 0.0

    def get_mass(self):
        return self.mass

    def get_x_pos(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def __str__(self):
        return f"Sun {self.name}: mass={self.mass}, radius={self.radius}, temperature={self.temp}"

class Planet:
    def __init__(self, name, radius, mass, distance, vel_x, vel_y, color):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.x = distance
        self.y = 0.0
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.color = color
        self.turtle = self.initialize_turtle()

    def initialize_turtle(self):
        planet_turtle = turtle.Turtle()
        planet_turtle.shape("circle")
        planet_turtle.color(self.color)
        planet_turtle.shapesize(self.radius / 10)  
        planet_turtle.penup()  # Don't draw when moving
        planet_turtle.goto(self.x, self.y)  # Set initial position
        return planet_turtle

    def get_mass(self):
        return self.mass

    def get_distance(self):
        return self.distance

    def get_x_pos(self):
        return self.x

    def get_x_vel(self):
        return self.vel_x

    def get_y_pos(self):
        return self.y

    def get_y_vel(self):
        return self.vel_y

    def set_x_vel(self, new_x_vel):
        self.vel_x = new_x_vel

    def set_y_vel(self, new_y_vel):
        self.vel_y = new_y_vel

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.turtle.goto(new_x, new_y)  

    def draw_planet(self):
        self.turtle.clear()  # Clear previous drawings
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)  
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(self.radius)
        self.turtle.end_fill()

    def __str__(self):
        return f"Planet {self.name}: mass={self.mass}, radius={self.radius}, distance={self.distance}"

class SolarSystem:
    def __init__(self):
        self.the_sun = None
        self.planets = []

    def add_planet(self, new_planet):
        self.planets.append(new_planet)

    def add_sun(self, the_sun):
        self.the_sun = the_sun

    def show_planets(self):
        for planet in self.planets:
            print(planet)

    def move_planets(self):
        dt = 0.001  
        for planet in self.planets:
            # Move the distance covered in the interval dt
            new_x = planet.get_x_pos() + dt * planet.get_x_vel()
            new_y = planet.get_y_pos() + dt * planet.get_y_vel()
            planet.move_to(new_x, new_y)
            
            dist_x = self.the_sun.get_x_pos() - planet.get_x_pos()
            dist_y = self.the_sun.get_y_pos() - planet.get_y_pos()
            new_distance = math.sqrt(dist_x**2 + dist_y**2)

            acc_x = UniversalGravity.G * self.the_sun.get_mass() * dist_x / new_distance**3
            acc_y = UniversalGravity.G * self.the_sun.get_mass() * dist_y / new_distance**3
            
            planet.set_x_vel(planet.get_x_vel() + dt * acc_x)
            planet.set_y_vel(planet.get_y_vel() + dt * acc_y)

class Simulation:
    def __init__(self, solar_system, width, height, num_periods):
        self.solar_system = solar_system
        self.width = width
        self.height = height
        self.num_periods = num_periods
        turtle.setup(width, height)  

    def run(self):
        for period in range(self.num_periods):
            self.solar_system.move_planets()
            
            # Draw each planet after moving it
            for planet in self.solar_system.planets:
                planet.draw_planet()

            print(f"Period: {period + 1}")
            self.solar_system.show_planets()

if __name__ == '__main__':
    turtle.tracer(0, 0)  

    solar_system = SolarSystem()
    
    the_sun = Sun("SOL", 5000, 10000000, 5800)
    solar_system.add_sun(the_sun)

    earth = Planet("EARTH", 1.0, 5.972e24, 150, 0, 30, "blue")
    solar_system.add_planet(earth)
    
    mars = Planet("MARS", 0.5, 0.64171e24, 228, 0, 24, "red")
    solar_system.add_planet(mars)

    simulation = Simulation(solar_system, 800, 600, 500)
    simulation.run()
    
    turtle.done()  
