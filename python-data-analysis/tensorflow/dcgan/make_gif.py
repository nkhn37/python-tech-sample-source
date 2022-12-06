"""GIF画像の生成

[説明ページ]
https://tech.nkhn37.net/tensorflow-keras-dcgan/#GIF
"""
import glob
import imageio

gif_filename = "dcgan_mnist.gif"

with imageio.get_writer(gif_filename, mode="I") as writer:
    filenames = glob.glob("generated_imgs_*.png")
    filenames = sorted(filenames)
    for filename in filenames:
        image = imageio.v3.imread(filename)
        writer.append_data(image)
