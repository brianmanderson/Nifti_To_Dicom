# A function to turn nifti files back into dicom
## Highly recommend to use the image processor here, and to use the Dicom_RT_and_Images_to_Mask.with_annotations() function to create RT structure.. much faster https://github.com/brianmanderson/Dicom_RT_and_Images_to_Mask

    from Nifti_To_Dicom.Conversion_Definition import convert_niftii_to_dicom
    
    image_path = 'K:\\Morfeus\\BMAnderson\\Overall_Data_LiTs_111.nii.gz'
    out_path = 'C:\\Users\\bmanderson\\Desktop\\Lits_patients\\LiTs_111\\'
    patient_name='LiTs_111'
    patient_id = 'LiTs_111'
    is_structure=False
    convert_niftii_to_dicom(image_path,out_path,patient_name,patient_id,is_structure)
