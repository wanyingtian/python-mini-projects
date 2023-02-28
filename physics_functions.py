'''
some easy functions that help calculate some fundamental physical properties.
'''

# example values for parameters
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

#Temperature calculation
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp
f100_in_celcius = f_to_c(100)
print(f"100 Fahrenheit in Celcius is {f100_in_celcius}")

def c_to_f(c_temp):
    f_temp = c_temp * 9/5 + 32
    return f_temp
c0_in_fahrenheit = c_to_f(0)
print(f"0 Celcius in Fahrenheit is {c0_in_fahrenheit}")

#calculate force
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration) 
print(f"The GE train supplies {train_force} Newtons of force.")

#calculate energy
def get_energy(mass, c=3*10**8):
    energy = mass * c**2
    return energy
bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

#calculate work
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")