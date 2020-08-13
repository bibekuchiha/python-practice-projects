train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

#Write a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius.
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

#Define a variable f100_in_celsius and set it equal to the value of f_to_c with 100 as an input.
f100_in_celsius = f_to_c(100)
print('100 fahrenheit is '+ str(f100_in_celsius) +' degree celsius')

#Write a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit.
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

#Define a variable c0_in_fahrenheit and set it equal to the value of c_to_f with 0 as an input.
c0_in_fahrenheit = c_to_f(0)
print('0 degree is '+str(c0_in_fahrenheit)+' fahrenheit')

#Define a function called get_force that takes in mass and acceleration. It should return mass multiplied by acceleration.

def get_force(mass, acceleration):
  force = mass * acceleration
  return force

#Test get_force by calling it with the variables train_mass and train_acceleration.
#Save the result to a variable called train_force and print it out.

train_force = get_force(train_mass, train_acceleration)
#Print the string “The GE train supplies X Newtons of force.”, with X replaced by train_force.

print('The GE train supplies '+ str(train_force) + ' Newtons of force')

#Define a function called get_energy that takes in mass and c.

#c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8.

def get_energy(mass, c = 3*10**8):
  return mass * c**2
#Test get_energy by using it on bomb_mass, with the default value of c. Save the result to a variable called bomb_energy.
bomb_energy = get_energy(bomb_mass)
print('bomb energy  for bomb mass is '+str(bomb_energy))
#Print the string “A 1kg bomb supplies X Joules.”, with X replaced by bomb_energy.

print('A 1kg bomb supplies '+ str(bomb_energy)+' Joules')
#Define a final function called get_work that takes in mass, acceleration, and distance.
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) 
  result = force * distance
  return result

#Test get_work by using it on train_mass, train_acceleration, and train_distance. Save the result to a variable called train_work.
train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)

#Print the string "The GE train does X Joules of work over Y meters.", with X replaced with train_work and Y replaced with train_distance.

print("The GE train does {0} Joules of work over {1} meters.".format(train_work, train_distance))








