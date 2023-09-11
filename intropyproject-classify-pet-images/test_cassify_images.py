from classify_images import classify_images

results_dic = {'Boston_terrier_02303.jpg':['boston terrier'],'Poodle_07927.jpg':['poodle'],'cat_07.jpg':['cat']}
images_dir = "pet_images"
model = "vgg"

classify_images(images_dir,results_dic,model)




# from classifier import classifier 

# # Defines a dog test image from pet_images folder
# #test_image="pet_images/Collie_03797.jpg"
# test_image="pet_images/Rabbit_002.jpg"

# # Defines a model architecture to be used for classification
# # NOTE: this function only works for model architectures: 
# #      'vgg', 'alexnet', 'resnet'  
# model = "resnet"

# # Demonstrates classifier() functions usage
# # NOTE: image_classication is a text string - It contains mixed case(both lower
# # and upper case letter) image labels that can be separated by commas when a 
# # label has more than one word that can describe it.
# image_classification = classifier(test_image, model)

# # prints result from running classifier() function
# print("\nResults from test_classifier.py\nImage:", test_image, "using model:",
#       model, "was classified as a:", image_classification)
