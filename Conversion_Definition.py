__author__ = 'Brian M Anderson'
# Created on 2/14/2020
# With a large amount of help from Bastien Rigaud githut.com/guatavita

from subprocess import PIPE, Popen


def convert_niftii_to_dicom(image_file_path= 'K:\\Morfeus\\BMAnderson\\CNN\\Data\\Data_Liver\\Liver_Disease_Ablation_Segmentation\\Niftii_Data\\Train\\Overall_Data_LiTs_111.nii.gz',
                            out_path= 'C:\\Users\\bmanderson\\Desktop\\Lits_patients\\LiTs_111\\',
                            patient_desc='LiTs_111', is_structure=False):
    if not is_structure:
        args = 'plastimatch convert --input {} --output-dicom {} --patient-name {} --patient-id {}'.format(image_file_path, out_path, patient_desc, patient_desc)
    else:
        args = 'plastimatch convert --input-ss-img {}  --referenced-ct {}\ --output-dicom {}\ --patient-name {} --patient-id {}'.format(
            image_file_path, out_path, out_path, patient_desc, patient_desc)
    Popen(args, stdin=None, stdout=PIPE, stderr=None, shell=False, universal_newlines=True).communicate()


if __name__ == '__main__':
    pass
