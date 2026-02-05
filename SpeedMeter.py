#**Project 3: Speed Meter**

'''Create a program that receives from the user a value representing the speed on a road where the maximum allowed speed is 80 km/h.

Based on this value, the program must inform whether the driver received a minor, serious, or very serious fine.

If the speed is less than or equal to 80 km/h, display: “no fine”.
If it is up to 10 km/h over the limit, display: “received a minor fine”.
If it is between 11 km/h and 20 km/h over the limit, display: “received a serious fine”.
If it is more than 20 km/h over the limit, display: “received a very serious fine”.'''
#

fine = True

while fine == True:
      speed = int(input( 'Insert the value of the speed: '))
      if speed == 90:
       print ('received a minor fine')

      elif speed > 90 and speed <= 110:
         print ('received a serious fine')

      elif speed > 110:
         print ('received a very serious fine')

      elif speed <= 80:
            print ('no fine')

fine = False
         

