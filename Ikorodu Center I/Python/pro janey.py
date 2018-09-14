#introduce yourself
print("Hi,my name is jane haruna")
print("welcome to akiya bakery")
#display the purpose for this program :
print("this is a program designed to help with your baking experience and troubles")
#list out options to pick from
list = int(input("Select a course from the following options options 1-3:\n\n1. Doughnuts\n2. meat pie\n3. pancakes\n"))
#using if statement
if ( list == 1):
    print("the following steps are to be followed in other to make delicious home made doughnuts\ningredients:\n-4cups of flour\n-2cups of sugar\n-10 tbs warm water\n-8 tbs melted butter\n-1tsp salt\n-2 litres vegetable oil\n-1 pack instant dry yeast\n\nmethod:\nstep1:sieve the flour in a bowl,add the baking powder,sugar and salt\nstep2:in another bowl pour the instant dried yeast,melted butter and warm water,add this mixture to the bowl of flour\nstep3:mix well till it forms a dough,then flour a surface where you can kneed the dough.\nstep4:cover the dough and store it in a warm place to make it rise for an hour.\nstep4:bring out the dough kneeed again,roll with a rolling pin and start cutting with a doughnut cutter\nstep5:live for another 30 t0 rise then fry.")
elif ( list == 2):
    print("the following steps are to be followed in other to make delicious home made meat pie\ningredients:\n-250g of butter\n-2 large eggs(1 for the dough and 1 for coating)\n-1 cup cold water\n-500g flour\n\nfor the sauce you are going to need the following ingredients:\n\n-200g of meat\n-6 big irish potatoes\n-5 large carrots\n-1 big green pepper\n-1 big bulb of onion\n-spring onions(optional)\n-1tbs baking powder\n-a pinch of salt\n\nMethod:\nstep 1:\nsift flour into a clean bowl and add the baking powder and salt.\n\nstep 2:\nAfter mixing the flour,baking powder and salt add the butter and 1 large egg,mix well till the mixture turns yellow.\n\nstep 3\nAdd the cold water and mix till the mixture forms a dough.\n\nstep 4\nMake the sauce by peeling the potatoes and onion and dicing them with other ingredients after washing(wash and blend the meat,you can pound the meat after boiling if you don't have a blender)")
elif ( list == 3):
    print("the following steps are to be followed in other to make delicious home made pancakes\ningredients:\n-100g of flour\n-20g sugar\n-1 tsp baking powder\n-1 egg\n-1 cup milk\n-1cup water\n-half 5g vegetable oil\n\nmethod:\nstep1:mix all the dry ingredient together\nstep2:add the liquid ingredient to the dried ingredient\nstep3:mix all the ingredient well,and fry on a scallet panS")
else:
    print("invalid selection\nplease choose between 1-3")
