import random
money = 900
oxes = 0
wheels = 0
axles = 0
flour = 0
salt = 0
clothes = 0
import time
import pygame

#pygame initialize
pygame.init()

#welcome player
print('Welcome to the game Oregon Trail ')

front_wheel_color = (70, 70, 70)
back_wheel_color = (50, 50, 50)
car_color = (255, 255, 100)

input("Do you want to see a wagon that you are riding in?")
print("Tooo bad. You are!")
#windows
window = pygame.display.set_mode([400, 400])
window.fill((200, 200, 255))

# Draw the back wheels
pygame.draw.circle(window, back_wheel_color, (272,250), 25)
pygame.draw.circle(window, back_wheel_color, (147,250), 25)

# Draw the car
pygame.draw.circle(window,(255,255,255), (150,200), 50)
r = pygame.Rect(100,200,200,50)
pygame.draw.rect(window, car_color, r)


# Draw the front wheels
pygame.draw.circle(window, front_wheel_color, (253,250), 25)
pygame.draw.circle(window, front_wheel_color, (128,250), 25)

pygame.display.flip()

input("This is the wagon you are living in!(Enter to continue!)")

player1 = "Bill"
#asking name
player_name = input('What is your name:')
while player_name != "Bill":
  if player_name != "Bill":
    print(player_name + "? It is a good name.")
    print("You have another guy named Bill riding with you today!")
# Drawing bill    
    black = (0, 0, 0)
    white = (255, 255, 255)

    window = pygame.display.set_mode([400, 400])
    window.fill((50, 50, 50))

    # Outline each shape
    pygame.draw.circle(window, white, (200, 150), 200)


    pygame.draw.circle(window, white, (200, 200), 180)


    pygame.draw.circle(window, white, (130, 130), 40)
    
    
    pygame.draw.circle(window, white, (130, 130), 10)
    
    
    pygame.draw.circle(window, white, (270, 130), 40)
    
    
    pygame.draw.circle(window, white, (270, 130), 10)
    
    
    pygame.draw.polygon(window, white, [(200, 130), (200, 260), (250, 230)])
    
    
    rect = pygame.Rect(120, 290, 80, 40)
    pygame.draw.ellipse(window, white, rect)
    pygame.draw.circle(window, black, (200, 150), 200,3)
    
    
    pygame.draw.circle(window, black, (200, 200), 180,3)
    
    
    pygame.draw.circle(window, black, (130, 130), 40,3)
    
    
    pygame.draw.circle(window, black, (130, 130), 10,3)
    
    
    pygame.draw.circle(window, black, (270, 130), 40,3)
    
    
    pygame.draw.circle(window, black, (270, 130), 10,3)
    
    
    pygame.draw.polygon(window, black, [(200, 130), (200, 260), (250, 230)],3)
    
    
    rect = pygame.Rect(120, 290, 80, 40)
    pygame.draw.ellipse(window, black, rect,3)
    
    pygame.display.flip()

    input("Enter to close hideous picture.")
    print("Too bad. It's going to stay open")
    break
    
  else:
    print("You did not type anything, try again")
    player_name = input('What is your name:')

#easter eggs for name
if player_name == 'Meriwether Lewis':
  year_set = 1803
  mode_choice = 'impossible'
else:
  year_set = input('Enter a year whatever you like:')
  print()
  print('Which mode do you want to play?')
  mode_choice = input('(easy, normal, hard, impossible):')
  print("Too bad you are playing impossible")  
  
# Leap year
if (year_set % 4) == 0:
   if (year_set % 100) == 0:
       if (year_set % 400) == 0:
           print('leap year')
       else:
            print('no leap year')
   else:
        print('leap year')
else:
    print('no leap year')

#oregon shop:
while len(mode_choice) >= 0: 

    if mode_choice:
        print()
        print("Welcome to the Oregon Shop!")
        print()
        while money > 0:
            print("You have $" + str(money) + " left.")
            print()
            print("1) Oxen")
            print("2) Food")
            print("3) Parts")
            print("4) Clothes")
            num_input = input("What do you want to buy?(exit to exit) ")
            if num_input == "1":
                oxen = int(input("Oxen are $50 a yoke. How many would you like to buy?"))
                money -= oxen * 50
                oxes += oxen
            if num_input == "2":
                foo = input("Food is either flour or salt and pepper. Which are you buying? ")
                if foo == "flour":
                    flur = int(input("Flour is 10 dollars a pound."))
                    money -= flur * 10
                    flour += flur
                if foo == "salt and pepper":
                    pep = int(input("Salt is 5 dollars a pound. "))
                    salt += pep
                    money -= pep * 5
            if num_input == "3":
                co = input("Would you like to buy wheels or axles? ")
                if co == "wheels":
                    whes = int(input("How many wheels do you want?(wheels are $25 each) "))
                    wheels += whes
                    whes += whes * 25
                    money -= whes
                if co == "axles":
                    axes = int(input("How many axles do you want?(axles are $25 each) "))
                    axles += axes
                    axes += axes * 25
                    money -= axes
            if num_input == "4":
                cloth = int(input("How many sets of clothes do you want?( clothes are $5 a set.) "))
                clothes += cloth
                cloth += cloth * 5
                money -= cloth
            if num_input == "exit":
                break
        food_num = salt + flour
        health_num = 10
        break

#other basic strating value setting
player_move_distance = 0
month_num = 3
days_pass = 1
total_days = 0
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
random_result = 0
health_d1 = random.randint(1, 31)
health_d2 = random.randint(1, 31)
acident_appear = random.randint(1, 30)
travel_total_num = 0
rest_total_num = 0
hunt_total_num = 0
status_total_num = 0
month_appear = 'March'

#add days:
def add_days(min, max):
  global days_pass
  global month_num
  global MONTHS_WITH_31_DAYS
  global random_result
  global food_num
  global health_num
  global health_d1
  global health_d2
  global total_days
  global acident_appear

  random_result = random.randint(min, max)
  print('Now',random_result,"days passed..")
  days_pass_min = days_pass
  check_big = days_pass + random_result

  #accident
  if acident_appear >= days_pass and acident_appear <= check_big:
    a_number = random.randint(1, 3)
    a_health_num = random.randint(1, 2)
    if a_number == 1:
      print('During this time, you crossed a river.')
    if a_number == 2:
      print("During this time, " + player1 + " had a dysentery.")
    if a_number == 3:
      print('During this time, you saw a beautiful girl and had a good time with her.')
    random_result2_food = random.randint(1, 10)
    random_result2_day = random.randint(1, 10)
    print('As a result, you eat '+str(random_result2_food)+' lbs extra food.')
    print('It also took up extra '+str(random_result2_day)+' days.')
    if a_health_num == 1:
      print('And you also lose 1 health')
      health_num -= 1
    food_num = food_num - random_result2_food - random_result2_day*5
    days_pass += random_result2_day
    total_days += random_result2_day
  #health decrease randomly  
  check_big = days_pass + random_result
  if health_d1 >= days_pass_min and health_d1 <= check_big:
    health_num -= 1
    print('Unfortunately, you lose 1 health during this time.')
  if health_d2 >= days_pass_min and health_d2 <= check_big:
    health_num -= 1
    print('Unfortunately, you lose 1 health during this time.')


  days_pass += random_result
  total_days += random_result
  food_num -= random_result * 5

  if days_pass >= 30:
    if month_num not in MONTHS_WITH_31_DAYS:
      if days_pass > 30:
        days_pass -= 30
        month_num += 1
        health_d1 = random.randint(1, 30)
        health_d2 = random.randint(1, 30)
        acident_appear == random.randint(1, 30)
    else:
      if days_pass > 31:
        days_pass -= 31
        month_num += 1
        health_d1 = random.randint(1, 30)
        health_d2 = random.randint(1, 30)
        acident_appear == random.randint(1, 30)

#function part
def travle1(movedistance):
  global days_pass
  global travel_total_num
  add_days(3,7)
  movedistance = movedistance + random.randint(30, 60)
  travel_total_num += 1
  return movedistance

def rest(health):
  global days_pass
  global rest_total_num
  add_days(2,5)
  health = health + 1
  rest_total_num += 1
  return health

def hunt(hunting_food):
  global days_pass
  global hunt_total_num
  add_days(2,5)
  hunting_food = hunting_food + 100
  print("You caught a wild buffalo!")
  print('Gain: 100 lbs food')
  hunt_total_num += 1
  sl = input("Do you want to preserve it? ")
  if sl == "yes":
    if sl > 25:
        print("Ok you can preserve it for 25 pounds of salt. ")
        
  else:
      print("You cant preserve it!")
      print("It will rot soon!")
      
  return hunting_food

#month_appear
def month_appear_fun():
  global month_appear
  if month_num == 1:
    month_appear = 'January'
  elif month_num == 2:
    month_appear = 'February'
  elif month_num == 3:
    month_appear = 'March'
  elif month_num == 4:
    month_appear = 'April'
  elif month_num == 5:
    month_appear = 'May'
  elif month_num == 6:
    month_appear = 'June'
  elif month_num == 7:
    month_appear = 'July'
  elif month_num == 8:
    month_appear = 'August'
  elif month_num == 9:
    month_appear = 'September'
  elif month_num == 10:
    month_appear = 'October'
  elif month_num == 11:
    month_appear = 'November'
  elif month_num == 12:
    month_appear = 'December'
  return month_appear

#loading part
print('--------------------------------------')
print('Now Loading...')
time.sleep(0.5)
print('Now loading the player setting...')
print()
time.sleep(2)
print('Successfully!')
print()
time.sleep(0.5)
print('Now loading the game setting...')
print()
time.sleep(2)
print('Successfully!')
print()
time.sleep(0.5)
print('Prepearing the trip for Oregon...')
print()
time.sleep(2)
print('Successfully!')
time.sleep(0.5)
print()
print('Now game is ready!')
print('--------------------------------------')
print('Attention:')
print('We will be recreating Oregon Trail! The goal is to travel from NYC to')
print('Oregon (2000 miles) by Dec 31st. However, the trail is arduous. Each')
print('day costs you food and health. You can hunt and rest, but you have to')
print('get there before winter. GOOD LUCK!')
print('--------------------------------------')
print()

#main
while player_move_distance < 2000 and food_num > 0 and health_num > 0 and month_num < 13:
  month_appear_fun()
  if food_num <= 50:
    print('Warning! You only have '+ str(food_num) + " lbs food now.")
    print('You need hunt now.')
    print()
  if health_num <= 2:
    print('Warning! You only have '+ str(health_num) + " health now.")
    print('You need a rest.')
    print()
  print(str(player_name) + ', now it is ' + month_appear + ' '+str(days_pass) + ', ' + str(year_set) + ", and you have travled " + str(player_move_distance) + " miles.")
  print()
  choice = input('Your choice (Travel, Rest, hunt, status, help, quit): ')
  print()
  if choice == 'travel':
    player_move_distance = travle1(player_move_distance)
  elif choice == 'rest':
    if health_num < 5:
      print("You get 1 heath!")
      print()
      health_num = rest(health_num)
    if health_num >= 5:
      print("Your health is full, the maximum number for health is 5!")
      print()
  elif choice == 'hunt':
    food_num = hunt(food_num)
  elif choice == 'status':
    print('-Dear ' + str(player_name) + ', now is '+str(month_num)+'/'+str(days_pass)+'/'+str(year_set)+".")
    print('-Food:',food_num,"lbs")
    print('-Health:',health_num)
    print('-Distance traveled:',player_move_distance)
    distance_left = 2000 - player_move_distance
    print('-'+str(total_days) +' days have passed.')
    print()
    print('-You have travled ' + str(player_move_distance) + " miles, there is still " + str(distance_left) + ' miles left.')
    print()
    status_total_num += 1
  elif choice == 'help':
    print("[travel]: moves you randomly between 30-60 miles and takes 3-7 days (random).")
    print("[rest]: increases health 1 level (up to 5 maximum) and takes 2-5 days (random).")
    print("[hunt]: adds 100 lbs of food and takes 2-5 days (random).")
    print("[status]: lists food, health, distance traveled, and day.")
    print("[quit]: will end the game.")
    print()
  elif choice == "quit":
    quit_choice = input("Are you sure that you want to quit?(y/n)")
    print()
    if quit_choice == "y":
      print("Game over...I cannot believe that you quit...")
      break
  elif choice == "suicide":
    quit_choice2 = input("Are you sure?(y/n)")
    if quit_choice2 == "y":
      print("Game over...You kill youslf...")
      break
  elif choice == "easter egg":
    print("Nice job! you have arrived in Oregon")
    print()
    print("Thanks for playing!")
    break
  else:
    print("This Choice is not available, please try again.")
    print("--------------------------------------")
    print()
#succeed!
if player_move_distance >= 2000:
  print("Nice job! you have arrived in Oregon")
  print()

#game over
if food_num <= 0:
  print("Game over, you have no food now.")
  print()
    
if health_num <= 0:
  print("Game over, you have no health now.")
  print()
if month_num >= 13:
  print("Game over, you run out of time!")
  print() 
print("During the whole game, you:")
print("Travel " + str(travel_total_num) +" times.")
print("Rest " + str(rest_total_num) +" times.")
print("Hunt " + str(hunt_total_num) +" times.")
print("Status " + str(status_total_num) +" times.")


<============================================|==============================================>
count = 0
a = 0
b = 0
c = 0
d = 0
e = "ERROR 404 PAGE NOT FOUND... PLEASE CHECK YOUR INPUT AGAIN"
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0 
z = 0

print()
print()
print("WELCOME TO JALIGAS CHEMISTRY GAME!")
print()
print("WE HAVE LOTS OF FUN IN STORE FOR YOU TODAY!")
print()
while True:
    a = input("How many Players are playing today...(Please give a number answer of '1' or '2')  ")
    if a == "1":
        print()
        print("You have said that there is only " + str(a) + " player...")
        b = input("Is this correct?(please answer 'y' or 'n') ")
        print()
        if b == "y":
            break
        elif b == "n":
            print("Okay Lets try this again...")
        else:
            print(e)
    elif a == "2":
        print()
        print("You have said that there are only " + str(a) + " players...")
        b = input("Is this correct?(please answer 'y' or 'n') ")
        print()
        if b == "y":
            break
        elif b == "n":
            print("Okay Lets try this again...")
        else:
            print(e)        
    else:
        print(e)


if a == "1":
    print("Welcome Player 1!")
    print()
    print()