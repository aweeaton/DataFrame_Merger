#Import the necessary modules
import pandas as pd
import xlsxwriter

#Print statement to introduce the script to the user
print("\nWelcome to the merging script!")

#Set the prompt variable equal to a constant value
prompt = "> "

#Print statement to get the first file the user is interested in merging
print('Please type in the full path to the first file you would like to merge.\n')

#Function to read in files and convert them to pandas data frames
def make_df(df):
    try:
        return pd.read_excel(df)
    except:
        return pd.read_csv(df)

#Store the first file inputted in a variable named "first_file"
first_file = input(prompt)

#Read the data frame into pandas and store the read file as a variable
first_file_read = make_df(first_file)

#Print statement
print('\nCongratulations! The file has been read. Here are the columns: \n')
print(list((first_file_read.columns)))

#Print statement to get the second file the user is interested in merging
print("\nPlease type in the full path to the second file you would like to merge.\n")

#Store the second file inputted in a variable named "second_file"
second_file = input(prompt)

#Read the data frame into pandas and store the read file as a variable
second_file_read = make_df(second_file)

#Print statement
print('\nCongratulations! The file has been read. Here are the columns:\n')
print(list((second_file_read.columns)))

#Print statement asking what column to merge the two data frames on
print('\nWhich column would you like to merge the two data frames on?')
print('The column must be shared between both data frames and be exactly the same.\n')

#Store the user input as a variable
merge_column = input(prompt)

#Print statements for letting the user choose the merge type
print('\nHow would you like to merge the two data frames?\n')
print('Type "left" to keep all of the values in the first data frame.')
print('Type "right" to keep all of the values in the second data frame.')
print('Type "inner" to keep all of the shared values in both data frames.')
print('Type "outer" to keep all of the values in both data frames\n')

#Store the type of join response as a variable
how_input = input(prompt)


#If-then statement to confirm the merge column is in both data frames
a = True
while a == True:
    if merge_column in (list((first_file_read.columns))) and (list((second_file_read.columns))):
        merged_df = pd.merge(first_file_read, second_file_read, how = how_input, on = merge_column)
        a = False
    else:
        print(f'\nThe entered column: "{merge_column}" is not present in both data frames.')
        print('Please type a column that is shared between both data frames.')
        merge_column = input(prompt)

#Print statement
print('\nWhat you like to name the outputted excel file?')
print('Make sure it ends in ".xlsx" or a similar extension!\n')

#Store the answer as a variable
excel_name = input(prompt)

#Write the new data frame to excel
output_file = pd.ExcelWriter(excel_name, engine = 'xlsxwriter')
merged_df.to_excel(output_file)
output_file.close()
