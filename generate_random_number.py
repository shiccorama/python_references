import string
import random

class RandomSerial():

    def generate_serials(size):
        all_char = string.ascii_lowercase + string.ascii_uppercase + string.digits
        # print(all_char)

        char_size = len(all_char)

        serial_list = []

        while size > 0:
            random_char = random.randint(0, char_size-1)
            # print(random_char)
            serial_list.append(all_char[random_char])
            # print(serial_list)
            result = "".join(serial_list)

            size -= 1
        print(result)


    generate_serials(12)