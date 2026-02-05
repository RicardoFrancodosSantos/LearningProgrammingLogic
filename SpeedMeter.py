#**Project 3: Speed Meter**

'''Create a program that receives from the user a value representing the speed on a road where the maximum allowed speed is 80 km/h.

Based on this value, the program must inform whether the driver received a minor, serious, or very serious fine.

If the speed is less than or equal to 80 km/h, display: “no fine”.
If it is up to 10 km/h over the limit, display: “received a minor fine”.
If it is between 11 km/h and 20 km/h over the limit, display: “received a serious fine”.
If it is more than 20 km/h over the limit, display: “received a very serious fine”.'''
#

velocity =float(input('Insert the speed value: '))
maximum_speed = 80

if velocity <= maximum_speed:
            print ('no fine')

elif velocity  <= maximum_speed +10:
       print ('received a minor fine')

elif velocity  <= maximum_speed +20:
       print ('received a serious fine')

elif velocity  <= maximum_speed +30:
       print ('received a very serious fine')
else:         
        print ('received a very very serious fine')

