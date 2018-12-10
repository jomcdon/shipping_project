#function to calculate ground cost
def shipping_cost_ground(weight):
    if weight <= 2:
      price_per_pound = 1.50
    elif weight <= 6:
      price_per_pound = 3.00
    elif weight <= 10:
      price_per_pound = 4.00
    else:
      price_per_pound = 4.75
    
    return 20 + (price_per_pound * weight)

#test  
print(shipping_cost_ground(8.4))\

shipping_cost_premium = 125.00

#function to calculate drone cost
def shipping_cost_drone(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  
  return (price_per_pound * weight)

# test drone
print(shipping_cost_drone(1.5))

#create function to print cheapest method
def print_optimal_shipping_method(weight):
  
  ground = shipping_cost_ground(weight)
  premium = shipping_cost_premium
  drone = shipping_cost_drone(weight)
  
  if ground < drone and ground < premium:
    method = "ground shipping"
    cost = ground
  elif drone < ground and drone < premium:
    method = "drone shipping"
    cost = drone
  else:
    method = "premium shipping"
    cost = premium
  
  print (
    "The cheapest shipping method is $%.2f with %s shipping."
  % (cost, method)
  )
  
#test function
print_optimal_shipping_method(4.8)
print_optimal_shipping_method(41.5)




