__author__ = 'Brian M Anderson'
# Created on 2/15/2020
from Dicom_RT_and_Images_to_Mask.Image_Array_And_Mask_From_Dicom_RT import Dicom_to_Imagestack, sitk, os
from Dicom_RT_and_Images_to_Mask.Plot_And_Scroll_Images.Plot_Scroll_Images import plot_scroll_Image
from tensorflow.python.keras.utils.np_utils import to_categorical


class Niftii_To_Annotation(object):

    def __init__(self, ROI_Names=None):
        self.ROI_Names = ROI_Names
        self.Dicom_reader = Dicom_to_Imagestack()

    def niftii_to_annotation(self,dicom_path,nifti_annotation_path,out_path):
        self.Dicom_reader.make_array(dicom_path)
        annotations = sitk.ReadImage(nifti_annotation_path)
        annotations = sitk.GetArrayFromImage(annotations)
        annotations = to_categorical(annotations)
        # annotations[..., 1] += annotations[..., 2]
        self.Dicom_reader.with_annotations(annotations, out_path, ROI_Names=self.ROI_Names)


if __name__ == '__main__':
    pass