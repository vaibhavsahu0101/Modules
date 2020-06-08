import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator




# Provide the same seed and keyword arguments to the fit and flow methods

def augmentation(image,mask):

    # we create two instances with the same arguments
    data_gen_args = dict(featurewise_center=True,
                     featurewise_std_normalization=True,
                     rotation_range=90,
                     width_shift_range=0.1,
                     height_shift_range=0.1,
                     zoom_range=0.2)
    image_datagen = ImageDataGenerator(**data_gen_args)
    mask_datagen = ImageDataGenerator(**data_gen_args)

    seed=5
   # image_datagen.flow(image, augment=True, seed=seed)
   # mask_datagen.flow(mask, augment=True, seed=seed)
    image_generator = image_datagen.flow(image)
    mask_generator = mask_datagen.flow(mask)
    train_generator = zip(image_generator, mask_generator)
    return train_generator