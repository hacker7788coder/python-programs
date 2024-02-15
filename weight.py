weight  = int(input('weight:'))
unit  =  input('(l)bs  or  (k)gs')
if unit.upper()  == "L":
    converted  = weight   *  0.45
    print(f"You are {converted} into kilos")
else:
    converted  = weight / 0.45
    print(f"you are {converted} into pounds")