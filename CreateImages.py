from PIL import Image
import numpy as np

class ImageOperations:

    def getTemplateReady(self):
        basicImage = Image.open("images/ConveyorBelt.jpg")
        maxsize = (512, 256)
        basicImage.thumbnail(maxsize, Image.ANTIALIAS)
        Template = Image.new("RGB", (512, 512),color="#A4A4A4")
        Template.paste(basicImage, (0, 128))

        t_width, t_height = Template.size
        print(str(t_width) + "," + str(t_height))

        Template.save("template.png", "PNG")

        return Template


    def divideIntoSections(self,belt_start, belt_end, number_of_sections):
        width = belt_end-belt_start
        sec_width = width/number_of_sections
        ls = []
        for i in range(number_of_sections+1):
            ls.append(belt_start + (sec_width*i))
        return ls


    def generateImage(self, template):
        center = Image.open("images/Center.jpg")

        center_small = center
        maxsize = (512, 256)
        center_small.thumbnail(maxsize, Image.ANTIALIAS)

        center_small = center
        maxsize = (512, 256)
        center_small.thumbnail(maxsize, Image.ANTIALIAS)

        center_small = center
        maxsize = (512, 256)
        center_small.thumbnail(maxsize, Image.ANTIALIAS)

        l1     = Image.open("images/Left_1.jpg")
        r1     = Image.open("images/Right_1.jpg")
        l2     = Image.open("images/Left_2.jpg")
        r2     = Image.open("images/Right_2.jpg")

        panel = 1

        while panel < 16:
            r = np.random.uniform(low=0.0,high=1.0)
            if r > 0.8:
                box_size = np.random.uniform(low=0.0, high=1.0)
                if box_size < 0.5:
                    #paste a small image
                    panel = panel+1
                elif box_size<0.8 and box_size >=0.5:
                    #paste a medium size image
                    panel = panel+2
                elif box_size>0.8:
                    #paste a large image
                    panel = panel+3


    def pasteObjectOnBelt(self,currentBelt,object,start_x,start_y):
        til = Image.new("RGB", (923, 662))
        im1 = Image.open("layout.jpg")  # 25x25
        til.paste(im1, (0, 0))

        im2 = Image.open("object.jpg")  # 25x25
        til.paste(im2, (80, 80))

        til.show()





