from adjust_results4_isadog import adjust_results4_isadog
from classify_images import classify_images

results_dic = {'Boston_terrier_02303.jpg':['boston terrier'],'Poodle_07927.jpg':['poodle'],'cat_07.jpg':['cat']}
images_dir = "pet_images"
model = "vgg"
dogfile = "dognames.txt"




classify_images(images_dir,results_dic,model)



adjust_results4_isadog(results_dic, dogfile)