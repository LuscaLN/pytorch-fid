import os
import shutil
import glob
import random
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("--seed", type=int, default=0, help="Seed for selecting images")

parser.add_argument(
    "--images_path",
    type=str,  
    help=("Paths to the original images"),
)
parser.add_argument(
    "--results_path",
    type=str,
    help=("Paths to the selected images folder images"),
)

args = parser.parse_args()
i = args.seed

sd = int(float(i))

print("Seed: ", sd)
path_images = args.images_path + "/*.png"
#print(path_images)
dest_images = args.results_path
aux_dest = args.results_path
random.seed(sd) #melhor até agora: 4 
val = []
to_be_moved = random.sample(glob.glob(path_images), 800)

#masks = "/home/lucas/datasets/kvasirseg_separado/selecao/original/masks"

print("Selecionando imagens aleatoriamente")
for f in enumerate(to_be_moved, 1):
    img = os.path.split(f[1])
    dest_images = aux_dest
    dest_images = os.path.join(dest_images, img[1])
    #print(dest_images)
    #dest_masks = os.path.join("/home/lucas/datasets/kvasirseg_separado/selecao/aux2/train/masks", img[1])
    #mask = os.path.join(masks, img[1])
    shutil.copy(f[1], dest_images)
    #shutil.copy(mask, dest_masks)
print("Seleção concluída")

'''
#Parte que seria usada para fazer um split de train - val 
for count, img in enumerate(glob.glob(path_images),1):
    if img not in to_be_moved:    
        val.append(img)

for f in enumerate(val, 1):
    img = os.path.split(f[1])
    dest_images = aux_dest
    dest_images = os.path.join(dest_images, img[1])
    #dest_masks = os.path.join("/home/lucas/datasets/kvasirseg_separado/selecao/aux2/val/masks", img[1])
    #mask = os.path.join(masks, img[1])
    shutil.copy(f[1], dest_images)
    #shutil.copy(mask, dest_masks)
'''
