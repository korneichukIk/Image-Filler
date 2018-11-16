from PIL import Image, ImageDraw, ImageFont
import random
import sys, os

strings = [
    'Calories',
    'Total Fat',
    'Sodium',
    'Total Carbohydrate',
    'Protein',
    'Iron',
    'Potassium',
]

values = [
    '',
    'g',
    'mg',
    'g',
    'g',
    '%',
    '%',
]

def write_file(data):
    # get first number of file
    first_number = int(data[0]["path"].split('.')[0])

    # check if 'data.txt' is empty
    old_data = []
    if first_number > 1:
        with open('data.txt', 'r') as file:
            for line in file.readlines():
                try:
                    # if not read every single line
                    old_data.append(line)
                except:
                    break

    # write data to file
    with open('data.txt', 'w') as file:
        # adding already existing data if they are
        if len(old_data) > 0:
            for old_line in old_data:
                file.write(old_line)
        for line in data:
            file.write(str(line) + '\n')

def create_image(index):
    # create image
    img = Image.new('RGB', (250, 150), color=(255, 255, 255))
    # set default font
    font = ImageFont.load_default()
    d = ImageDraw.Draw(img)
    # shuffle list with arguments in strings
    list = [i for i in range(len(strings))]
    random.shuffle(list)
    width = []
    marks = []



    for i in range(len(strings)):
        iter = list[i]
        d.text((5, (5 + i * 20)), strings[iter], fill=(0, 0, 0), font=font)
        if values[iter] == '%':
            value = str(random.randint(1, 100)) + values[iter]
        elif values[iter] == 'mg':
            value = str(random.randint(1, 1000)) + values[iter]
        else:
            value = str(random.randint(1, 1500)) + values[iter]

        d.text((180, (5 + i * 20)), value, fill=(0, 0, 0), font=font)
        # get width of value
        width.append(font.getsize(value)[0])
        # get value
        marks.append(value)



    # create new file name
    file = '{}.jpg'.format(index)

    # set data appearence
    data = {"path":file, "objects":
        [{"cat": strings[list[0]], "value":marks[0],"box":[180, 5, 14, width[0]]},
         {"cat": strings[list[1]], "value": marks[1], "box": [180, 25, 14, width[1]]},
         {"cat": strings[list[2]], "value": marks[2], "box": [180, 45, 14, width[2]]},
         {"cat": strings[list[3]], "value": marks[3], "box": [180, 65, 14, width[3]]},
         {"cat": strings[list[4]], "value": marks[4], "box": [180, 85, 14, width[4]]},
         {"cat": strings[list[5]], "value": marks[5], "box": [180, 105, 14, width[5]]},
         {"cat": strings[list[6]], "value": marks[6], "box": [180, 125, 14, width[6]]}
        ]
    }

    # save image
    img.save('images/' + file)
    return data

def check_file_existance():
    counter = 0
    for i in range(1, 999999):
        if os.path.isfile('images/' + create_6_ditits_index(i) + '.jpg'):
            counter += 1
        else:
            return counter

def create_6_ditits_index(number):
    index = str(number)

    digits_amount = len(index)
    for i in range(6 - digits_amount):
        index = '0' + index

    return indexg

def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def main():
    # get amount of images
    number = sys.argv[1]
    if not is_int(number):
        print('Bad number.')
        exit(0)

    # check if 'data.txt' exists
    if not os.path.isfile('data.txt'):
        os.system('touch data.txt')

    # check if 'images' folder exists
    if not os.path.isdir('images'):
        os.system('mkdir images')

    # create list of data
    datas_list = []
    # get integer from arg
    number_int = int(number)
    # get amount of already existing images
    counter = check_file_existance() + 1


    for i in range(number_int):
        # create 6-digits index for image title
        index = create_6_ditits_index(i + counter)
        # add meta data from image
        datas_list.append(create_image(index))

    # write data to file
    write_file(datas_list)

if __name__ == '__main__':
    main()