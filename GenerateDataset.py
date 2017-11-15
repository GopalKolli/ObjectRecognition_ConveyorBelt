from CreateImages import ImageOperations

operations = ImageOperations()

template = operations.getTemplateReady()

sectionsList = operations.divideIntoSections(belt_start=16, belt_end=496, number_of_sections=16)

operations.generateImage(template, sectionsList)