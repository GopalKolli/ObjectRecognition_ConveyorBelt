from PIL import Image
import numpy as np

class ImageOperations:

    numberOfBoxesRegulator = 0.6

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
            ls.append(int(belt_start + (sec_width*i)))
        return ls


    def generateImage(self, template, sectionsList):

        panel = 1

        while panel <= 16:
            r = np.random.uniform(low=0.0,high=1.0)
            if r > self.numberOfBoxesRegulator:
                box_size = np.random.uniform(low=0.0, high=1.0)
                if box_size < 0.5:
                    #paste a small image
                    template = self.pasteObjectOnBelt(template, "S", sectionsList, panel)
                    panel = panel+1
                elif box_size<0.8 and box_size >=0.5:
                    #paste a medium size image
                    template = self.pasteObjectOnBelt(template, "M", sectionsList, panel)
                    panel = panel+2
                elif box_size>0.8:
                    #paste a large image
                    template = self.pasteObjectOnBelt(template, "L", sectionsList, panel)
                    panel = panel+3
            else:
                panel = panel + 1

        #template.show()
        return template


    def pasteNoiseOnImage(self,template, sectionsList, portion):

        object = ""
        panel = 1

        while panel <= 5:
            place_random  = np.random.uniform(low=0.0,high=1.0)
            if place_random > 0.4:
                object_random = np.random.uniform(low=0.0, high=1.0)
                if object_random < 0.4:
                    object = "H"
                elif object_random >=0.4 and object_random < 0.7:
                    object = "T"
                else:
                    object = "C"
            else:
                panel = panel + 1
                continue


            if object == "H":
                h_margin = 48
                w_margin = 64
                maxsize = (64,48)
                facing_random = np.random.uniform(low=0.0, high=1.0)
                if facing_random > 0.4:
                    if panel == 1:
                        if portion == "Top":
                            noise_image = Image.open("ImageLab/images/N-Human_Top_Front_L2.jpg")
                        else:
                            noise_image = Image.open("ImageLab/images/N-Human_Bottom_Front-L2.jpg")
                    elif panel == 2:
                        if portion == "Top":
                            noise_image = Image.open("ImageLab/images/N-Human_Top_Front-L1.jpg")
                        else:
                            noise_image = Image.open("ImageLab/images/N-Human_Botton_Front-L1.jpg")
                    elif panel == 3:
                        if portion == "Top":
                            noise_image = Image.open("ImageLab/images/N-Human_Top_Front-Center.jpg")
                        else:
                            noise_image = Image.open("ImageLab/images/N-Human_Bottom_Front-center.jpg")
                    elif panel == 4:
                        if portion == "Top":
                            noise_image = Image.open("ImageLab/images/N-Human_Top_Front-R1.jpg")
                        else:
                            noise_image = Image.open("ImageLab/images/N-Human_Bottom_Front-R1.jpg")
                    else:
                        if portion == "Top":
                            noise_image = Image.open("ImageLab/images/N-Human_Top_Front-R2.jpg")
                        else:
                            noise_image = Image.open("ImageLab/images/N-Human_Bottom_Front-R2.jpg")

                else:
                    if portion == "Top":
                        if panel == 1:
                            noise_image = Image.open("ImageLab/images/N-Human_Top_side-L2.jpg")
                        elif panel == 2:
                            noise_image = Image.open("ImageLab/images/N-Human_Top_side-L1.jpg")
                        elif panel == 3:
                            noise_image = Image.open("ImageLab/images/N-Human_Top_side-center.jpg")
                        elif panel == 4:
                            noise_image = Image.open("ImageLab/images/N-Human_Top_side-R1.jpg")
                        else:
                            noise_image = Image.open("ImageLab/images/N-Human_Top_side-R2.jpg")
                    else:
                        panel = panel + 1
                        continue

            elif object == "T":
                h_margin = 48
                w_margin = 64
                maxsize = (64, 48)
                if panel == 1:
                    noise_image = Image.open("ImageLab/images/Tables-L2-edited.jpg")
                elif panel == 2:
                    noise_image = Image.open("ImageLab/images/Tables-L1-edited.jpg")
                elif panel == 3:
                    noise_image = Image.open("ImageLab/images/Tables-Center.jpg")
                elif panel == 4:
                    noise_image = Image.open("ImageLab/images/Tables-R1-edited.jpg")
                else:
                    noise_image = Image.open("ImageLab/images/Tables-R2-edited.jpg")

            elif object == "C":
                h_margin = 8
                w_margin = 16
                maxsize = (16,8)
                if panel == 1:
                    noise_image = Image.open("ImageLab/images/N-ciderBlock-Left.jpg")
                elif panel == 2:
                    noise_image = Image.open("ImageLab/images/N-ciderBlock-Left.jpg")
                elif panel == 3:
                    noise_image = Image.open("ImageLab/images/N-ciderBlocks-Center.jpg")
                elif panel == 4:
                    noise_image = Image.open("ImageLab/images/N-ciderBlocks-Right.jpg")
                else:
                    noise_image = Image.open("ImageLab/images/N-ciderBlocks-Right.jpg")

            else:
                panel = panel + 1
                continue


            if portion == "Top":
                y_min = 226 - 80
                y_max = 224 - h_margin
            else:
                y_min = 300
                y_max = 380 - h_margin

            x_min = sectionsList[panel - 1]
            x_max = sectionsList[panel] - w_margin

            x = np.random.uniform(low=x_min, high=x_max)
            y = np.random.uniform(low=y_min, high=y_max)

            x = int(x)
            y = int(y)

            noise_image.thumbnail(maxsize, Image.ANTIALIAS)
            template.paste(noise_image, (x, y))
            panel = panel + 1

        return template







    def pasteObjectOnBelt(self,current_Template, size, sectionsList, panelNumber):

        l1 = Image.open("images/Left_1.jpg")
        r1 = Image.open("images/Right_1.jpg")
        l2 = Image.open("images/Left_2.jpg")
        r2 = Image.open("images/Right_2.jpg")
        center = Image.open("images/Center.jpg")

        if panelNumber >=1 and panelNumber<=3:
            box_image = l2
        elif panelNumber >3 and panelNumber<=6:
            box_image = l1
        elif panelNumber >6 and panelNumber<=10:
            box_image = center
        elif panelNumber >10 and panelNumber<=13:
            box_image = r1
        elif panelNumber >13 and panelNumber<=16:
            box_image = r2
        else:
            return

        y_min = 226
        y_max = 288

        scaled_box_image = box_image
        if size=="S":
            maxsize = (24, 12)
            y_min = 226
            y_max = 276
            x_max = sectionsList[panelNumber] - 24
            x_min = sectionsList[panelNumber - 1]
        elif size=="M":
            maxsize = (32, 16)
            y_min = 226
            y_max = 272
            if panelNumber<=15:
                x_max = sectionsList[panelNumber+1] - 32
            else:
                return current_Template
            x_min = sectionsList[panelNumber - 1]
        elif size == "L":
            maxsize = (48, 24)
            y_min = 226
            y_max = 264
            if panelNumber<=14:
                x_max = sectionsList[panelNumber + 2] - 48
            else:
                return current_Template
            x_min = sectionsList[panelNumber - 1]
        else:
            return
        scaled_box_image.thumbnail(maxsize, Image.ANTIALIAS)

        x = np.random.uniform(low=x_min, high=x_max)
        y = np.random.uniform(low=y_min, high=y_max)

        x = int(x)
        y = int (y)


        #til = Image.new("RGB", (923, 662))
        #im1 = Image.open("layout.jpg")  # 25x25
        #til.paste(im1, (0, 0))

        #im2 = Image.open("object.jpg")  # 25x25
        #til.paste(im2, (80, 80))

        current_Template.paste(scaled_box_image, (x,y))
        return current_Template

        #til.show()





