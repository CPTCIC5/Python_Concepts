x1=input("Hey, u need comparision on which bases \n Age or Year").upper().strip()
current_year=2022
if x1  == "YEAR":
    year=int(input("ur birth year"))
    if year>current_year:
        print("SIR HOW CAN UR AGE BE BIGGER THEN YEAR R U IN FUTURE")
    age_rn=current_year-year
    if age_rn>=150:
        print('u r the oldest human alive')
    print(f'Ur age rn is {age_rn}')
    if age_rn<100:
        left_to_hit_hundred=100-age_rn
        print(f'after {left_to_hit_hundred} u will be 100')
    elif age_rn ==100:
        print('u r just 100 years old')
    else:
        print('damn u r already 100+')
elif x1  == "AGE":
    age=int(input('whats ur age'))
    if age>=150:
        print('u r the oldest human alive')
    birth_year=current_year-age
    if birth_year > current_year:
        print('u r the oldest person alive saar')
    print(f'ur rn age is {age}')
    if age<100:
        left_to_hit_hundred2=100-age
        print(f"{left_to_hit_hundred2} more years to hit 100")
    elif age == 100:
        print('u r just 100 years old')
    else:
        print("damn u r already 100+")
else:
    print("wrong input")