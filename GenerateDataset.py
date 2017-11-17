from CreateImages import ImageOperations

operations = ImageOperations()



for i in range(100):
    template = operations.getTemplateReady()

    sectionsList = operations.divideIntoSections(belt_start=16, belt_end=496, number_of_sections=16)
    Boxes_Image = operations.generateImage(template, sectionsList)

    sectionsList = operations.divideIntoSections(belt_start=16, belt_end=496, number_of_sections=5)
    NoiseImageTop = operations.pasteNoiseOnImage(Boxes_Image, sectionsList, "Top")
    NoiseImageBottom = operations.pasteNoiseOnImage(NoiseImageTop, sectionsList, "Bottom")

    generatedImage = NoiseImageBottom

    generatedImage.save("results/img_" + str(i) + ".jpg", "JPEG")