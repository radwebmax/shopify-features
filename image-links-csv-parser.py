"""
Before running the script you should put 
ready product.csv and empty product_new.csv files in the same file directory
"""

import csv


with open("products.csv", newline='') as r_file:
    # Creates object reader, with separator in you csv file ";"
    file_reader = csv.reader(r_file, delimiter = ";")
    #Be carefull with encoding, set the needed (utf-8 by default)
    with open("products_new.csv", mode="w", newline='') as w_file:
        file_writer = csv.writer(w_file, delimiter = ";")
        # Counter for products(rows in file)
        count = 0
        # Loop through products(rows) in file
        for row in file_reader:
            #if 24th row(Image Src) contains ";"(you can specify the separator with yours) - it means that we have more than one image src
            if row[24].find(';') != -1:
                img_srcs =  row[24].split(';')
                handle = row[0]
                #We left first row with whole info about the product but we change the Image Src node to contain first link only
                row[24] = img_srcs[0] 
                file_writer.writerow(row)
                index = 0
                for img in img_srcs:
                    #In my template if there's only one link, nevertheless empty separated links may occur so I prevent this
                    if img != " ":
                        #As we already wrote first row with first image link, we don't need to repeat it
                        if index != 0:
                            new_row = ['%s'%handle, '', '', '', '', '', '', '', '', '', '', '', '', '', '', 
                            '', '', '', '', '', '', '', '', '', '%s'%img, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
                            file_writer.writerow(new_row)
                    index += 1
            else:
                #if we dont have any link in Image Src we just add this row to the new file
                file_writer.writerow(row)
            count += 1


            #If you have empty rows just specify this value with the real amount of rows in your template
            if count == 3158:
                break
        print(f'Total products in file: {count}')

r_file.close()
w_file.close()
