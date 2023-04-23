#imports
from pathlib import Path
import sys
import os
#vars
intro = Path('zen.txt').read_text()
bonsai = Path('bonsai.txt').read_text()
waterfall = Path('waterfall.txt').read_text()
flowers = Path('flowers.txt').read_text()
matcha = Path('tea.txt').read_text()

#main
print(intro)
number = input("What do you want to see? Type the number below \n 1:bonsai 2:waterfall 3:flowers 4:tea ")
if number == ("1"):
    print(bonsai)
elif number == ("2"):
    print(waterfall)
elif number == ("3"):
    print(flowers)
elif number == ("4"):
    print (matcha)

restart = input('\n\n\n\n Press \'RETURN\' to go to the home page')


#restarting the app
os.system('clear')
os.execv(sys.executable, ['python'] + sys.argv)

