

weight = 1.5

if weight <= 2:
    cost_ground = weight*1.5 + 20 
    cost_drone = weight*4.5
elif weight <= 6:
    cost_ground = weight*3 + 20
    cost_drone = weight*9
elif weight <= 10:
    cost_ground = weight*4 + 20 
    cost_drone = weight*12 
elif weight > 10:
    cost_ground = weight*4.75 + 20 
    cost_drone = weight*14.25

print("Ground Shipping $", cost_ground)
print("Premium Shipping $", cost_ground+125)
print("Drone Shipping $", cost_drone)
