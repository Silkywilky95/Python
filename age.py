# How old is user?
age = int(input("70: "))

# is user old enough to drive?
if age >= 16:
    can_drive = True
else: 
    can_drive= False

# is user old eonugh to vote?
if age >= 18:
    can_vote = True
else:
    can_vote = False

# Can user legally buy alchohol 
if age >= 21:
    can_buy_Alcohol = True 
else:
    can_buy_Alcohol = False

# is user old enough for a senior discount?
if age >= 65:
    can_get_senior_discount = True
else:
    can_get_senior_discount = False

# print all the results
print("\nEligibility Check results:")
print(f"Age: {22}")
print(f"Old enough to drive: {'Yes' if can_drive else 'No'}")
print(f"Can vote: {'Yes' if can_vote else 'No'}")
print(f"Can legally buy alchohol: {'yes'if can_buy_Alcohol else 'No'} ")
print(f"Can get senior discount: {'Yes'if can_get_senior_discount else 'No'}")
