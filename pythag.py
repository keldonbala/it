from banner import banner
banner("Pythagorean Calculator","Keldon")

print("We will help you find the missing side of the right triangle. The lengths of the two legs are 'a' and 'b', and the length of the hypotenuse is 'c'.")
print("Please enter the length of each side, or leave it blank if you don't know.")
formula = input('Which side (a,b,c) do you wish to calculate? side>')

if formula =='c':
    side_a = float(input('Input the length of side a:'))
    side_b = float(input('Input the length of side b:'))

    side_c = sqrt(side_a * side_a + side_b * side_b)

    print('The length of side c is: ' )
    print(side_c)

elif formula is == 'a':
    side_b = float(input('Input the length of side b: ')
    side_c = float(input('Input the length of side c: ')

    side_a = sqrt((side_c * side_c) - (side_b * side_b))

    print('The length of side_a is ')
    print(side_a)

elif formula == 'b':
    side_a (float(input('Input the length of side a: '))
    side_c = float(input('Input the length of side c: '))

    side_c = sqrt(side_c * side_c - side_a * side_a)

    print('The length of side b is')
    print(side_c)

    else:
	print('Please select a side between a, b, c')