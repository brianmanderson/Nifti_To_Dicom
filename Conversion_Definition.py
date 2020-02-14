__author__ = 'Brian M Anderson'
# Created on 2/14/2020
# With a large amount of help from Bastien Rigaud githut.com/guatavita

from subprocess import PIPE, Popen


def convert_niftii_to_dicom(image_file_path= 'K:\\Morfeus\\BMAnderson\\CNN\\Data\\Data_Liver\\Liver_Disease_Ablation_Segmentation\\Niftii_Data\\Train\\Overall_Data_LiTs_111.nii.gz',
                            out_path= 'C:\\Users\\bmanderson\\Desktop\\Lits_patients\\LiTs_111\\',
                            patient_name='LiTs_111',patient_id='LiTs_111', is_structure=False):
    '''
    :param image_file_path: path to nii.gz file
    :param out_path: path to put dicom files
    :param patient_name: patient name
    :param patient_id: patient id
    :param is_structure: is this to be made into a structure file?
    :return: Creates a folder with the dicom files or RT structure
    '''
    if not is_structure:
        args = 'plastimatch convert --input {} --output-dicom {} --patient-name {} --patient-id {}'.format(image_file_path, out_path, patient_name, patient_id)
    else:
        args = 'plastimatch convert --input-ss-img {}  --referenced-ct {}\ --output-dicom {}\ --patient-name {} --patient-id {}'.format(
            image_file_path, out_path, out_path, patient_name, patient_id)
    Popen(args, stdin=None, stdout=PIPE, stderr=None, shell=False, universal_newlines=True).communicate()


if __name__ == '__main__':
    pass
