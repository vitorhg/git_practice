premium_ship = 120


def ship_cost_ground(weight):
    if weight <= 2:
        price_pound = 1.5
    elif weight <= 6:
        price_pound = 3
    elif weight <= 10:
        price_pound = 4
    else:
        price_pound = 4.75
    return 20 + (weight * price_pound)


print(ship_cost_ground(8.4))


def ship_cost_drone(weight):
    if weight <= 2:
        price_pound = 4.5
    elif weight <= 6:
        price_pound = 9
    elif weight <= 10:
        price_pound = 12
    else:
        price_pound = 14.25
    return weight * price_pound


print(ship_cost_drone(1.5))


def print_cheapest(weight):
    ground = ship_cost_ground(weight)
    drone = ship_cost_drone(weight)
    premium = premium_ship
    if ground < drone and ground < premium:
        method = "standard ground"
        cost = ground
    elif drone < premium and drone < ground:
        method = "drone"
        cost = drone
    else:
        method = "premium ground"
        cost = premium
    print("The cheapest is $%s with %s shipping." % (cost, method))


print_cheapest(1)
print_cheapest(4.8)
print_cheapest(41.5)
