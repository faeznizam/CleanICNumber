import pandas as pd
import datetime
import calendar
import os


def validate_nat_id(national_id):
  # change data type
  national_id = str(national_id)

  # Remove hyphens and spaces
  national_id = national_id.replace("-", "").replace(" ", "")

  # Check if the cleaned national ID has a length of 12
  if len(national_id) == 12:
    if is_valid_date(national_id):
      return f"{national_id[:6]}-{national_id[6:8]}-{national_id[8:]}"

  return ''

def is_valid_date(national_id):

  if len(national_id) == 12:
    year = national_id[0:2]
    month = national_id[2:4]
    day = national_id[4:6]

    current_year = datetime.datetime.now().year % 100

    # Determine the century based on the last 2 digits in the year
    if int(year) <= current_year:
        century = 20
    else:
        century = 19

    # Check if the month is valid
    if 1 <= int(month) <= 12:
        # Check if the day is valid for the given month
        max_day = calendar.monthrange(century * 100 + int(year), int(month))[1]
        if 1 <= int(day) <= max_day:
            return True

    return False


def main():
   # folder path to get file
   folder_path = r'C:\Users\mfmohammad\OneDrive - UNICEF\Documents\Data Cleaning\2024\Feb\7'

   # file name
   file_name = 'Donor With Invalid IC.xlsx'
   
   # combine folder path and file name
   file_path = os.path.join(folder_path, file_name)
   
   df = pd.read_excel(file_path , dtype={'National ID': str})
   column_name = 'National ID'
   
   df[column_name] = df[column_name].astype(str)
   df['Updated National ID'] = df[column_name].apply(validate_nat_id)

   # rename file with new name
   new_file_name = 'Donor With Invalid IC - Edited.xlsx'
   
   # build output file path
   new_file_path = os.path.join(folder_path, new_file_name)

   # save to excel and download
   df.to_excel(new_file_path, index = False)

   # successfull attempt prompt
   print(f'File {new_file_name} been saved in the folder')


if __name__ == "__main__":
  main()