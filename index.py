from PIL import Image
import os

dir = 'data'
os.makedirs(dir)

main_path = '1.jpg'
main = Image.open(main_path).convert('RGBA')

sub1_path = '2.png'
sub1 = Image.open(sub1_path).convert('RGBA')

sub2_path = '2.png'
sub2 = Image.open(sub2_path).convert('RGBA')

for i in range(1440):
    main_copy = main.copy()
    sub1_copy = sub1.copy()

    sub1_copy = sub1_copy.rotate(-i)
    main_copy.paste(sub1_copy, (0, 0), sub1_copy)

    name = "data/{:04}.png".format(i)
    print(name)
    main_copy.save(name)
