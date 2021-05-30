''' weight converter:
Input the weight of a person in either kg or lbs. if the person provides his/her weight
in the kg convert it into lbs else convert into kg'''
weight=float(input("enter the weight:"))
choose=input("kg or lbs:")


if choose=="kg":
    weight_convert= weight*2.205
    print(f'the {weight}kg ={weight_convert}lb')
else:
    weight_convert= weight/2.205
    print(f"the {weight }lbs={weight_convert}kg")