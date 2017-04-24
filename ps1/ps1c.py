annual_salary= float(input("Enter the starting salary: "))

total_cost= 1000000
increment = 0.07
r = 0.04
months = 36
portion_down_payment = 0.25
down_payment= total_cost*portion_down_payment

# portion_saved = guess
ps_low = 0
ps_high = 10000
previous_guess= 0
steps=0

while 1:

    steps += 1
    guess= int((ps_low + ps_high)/2)
    if abs(guess - previous_guess)<1:
        break
    counter= 0
    current_saving = 0
    ms = annual_salary / 12
    for i in range(36):
        if counter is 6:
            counter = 0
            ms += ms*increment
        current_saving = current_saving + (guess*ms)/10000 + (current_saving*r/12)
        counter += 1

    if abs(current_saving - down_payment)<=100:
        break
    elif current_saving < down_payment:
        ps_low= guess
    else: ps_high = guess
    previous_guess= guess
    # print("ps_low: ",ps_low , "||| ps_high:", ps_high)
    # print("guess:", guess)
    # print("saving:", int(current_saving))
    # print("\n \n")

if abs(current_saving - down_payment)<=100:
    print("Best savings rate:", guess/10000)
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to pay the down payment in three years.")