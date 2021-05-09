import os
categorys = os.listdir("database/")
def addCategory(categoryName):
    newCategory = categoryName
    newCategory = newCategory.lower()
    categoryIsReal = False
    for i in range(len(categorys)):
        if(categorys[i] == newCategory):
            categoryIsReal = True
    if(categoryIsReal != True):
        os.mkdir("database/" + newCategory)
    else:
        print("Error! That category exists!")
def addElement(element, content, category):
    elementExists = False
    elementsId = os.listdir("database/" + category)
    for i in range(len(elementsId)):
        if(elementsId[i] == element):
            elementExists = True
    if(elementExists == True):
        print("The element '{}' exists!".format(element))
    elif elementExists == False:
        elementFile = open("database/" + category + "/" + element, "w")
        elementFile.write(content)
        elementFile.close()
def verifyElement(element, category):
    elementExists = False
    elements = os.listdir("database/" + category)
    for elementI in range(len(elements)):
        if(elements[elementI] == element):
            elementExists = True
    return elementExists
def verifyContent(element, content, category):
  elementExists = False
  elementsCategory = os.listdir("database/" + category + "/")
  for i in range(len(elementsCategory)):
    if(elementsCategory[i] == element):
      elementExists = True
  if(elementExists):
    openElement = open("database/" + category + "/" + element, "r")
    return openElement.read() == content
def modifyContent(element, newContent, category):
  elementExists = False
  categoryDir = os.listdir("database/" + category + "/")
  for i in range(len(categoryDir)):
    if(categoryDir[i] == element):
      elementExists = True
  if(elementExists):
    elementModify = open("database/" + category + "/" + element, "w")
    elementModify.write(newContent)
    elementModify.close()
def getElement(element, category):
  categoryDir = os.listdir("database/" + category)
  elementExists = False
  for i in range(len(categoryDir)):
    if(categoryDir[i] == element):
      elementExists = True
  if(elementExists):
    elementInfo = open("database/{}/{}".format(category, element), "r")
    return elementInfo.read()
  else:
    print("The element " + element + " no exists!")
