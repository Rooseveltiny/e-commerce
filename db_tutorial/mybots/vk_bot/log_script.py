def log_info(*info):

    with open('log_file.txt', 'a') as file:

        all_data = ''
        for each in info:

            all_data += ' '+ str(each)
        
        file.write(all_data+ '\n')

