__author__ = 'Brian M Anderson'
# Created on 2/15/2020

'''
Because the Prep_Dicom_GUI.exe needs images and RTs to be in separate folders, we will move all of the image files
into another folder called 'Images'
'''
import os


def Separate_Images_into_Images_Folder(input_path):
    files = []
    folders = []
    for root, folders, files in os.walk(input_path):
        break
    found_dicom = False
    for val in files:
        if val.find('.dcm') != -1:
            found_dicom = True
            break
    if found_dicom and folders:
        print(input_path)
        if 'Images' not in folders:
            os.makedirs(os.path.join(input_path,'Images'))
        for file in files:
            os.rename(os.path.join(input_path,file),os.path.join(input_path,'Images',file))
    else:
        for folder in folders:
            Separate_Images_into_Images_Folder(os.path.join(input_path,folder))
    return None


if __name__ == '__main__':
    pass
