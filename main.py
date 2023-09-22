from translate import Translator


def writingFile(file_path, content):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(content+"\n")


def readingFile(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        index = 989
        for line in lines:
            translateData = merge(tags(line), translate(stringBuild(line), targetLanguage))
            writingFile("path.txt", translateData)
            print(translateData)


        return lines


def stringBuild(line):

    if len(line) > 9:
        strValue = ""
        i = len(line)-1
        if i != 1:
# .txt files
#            if line[0:15] == '\t<string name="':
            if line[0:18] == '    <string name="':
                j = 18

                while line[j] != '>':
                    j += 1
                strValue += line[j+1:len(line)-10]
# .txt files end
        return strValue


def tags(line):
    if len(line) > 9:
        strValue = '<string name="'
        j=0
        # .txt files start to read
#        if line[0:15] == '\t<string name="':
        if line[0:18] == '    <string name="':
            j = 18
            while line[j] != '>':
                strValue += line[j]
                j += 1
                if line[j] == '>':
                    strValue += line[j]
        if (len(line) > 9):
            i = len(line)-1
            if line[i-9:i-1] == '</string':
                j = i
                strValue += line[j-9:j-1]
                if line[j-1] == '>':
                    strValue += '>'
                i = len(line)-1
        return strValue


def merge(tags , sentence):
    if tags != None and sentence != '<strring name=':
        i = len(tags)
        j = 0
        strLine =""
        strLine += tags[j:i-9]
        strLine += sentence
        strLine += tags[i-9:]
        return strLine
    else:
        return ""


def translate(translatedsentence, targetLanguage):
    # translate api
    if translatedsentence != None and translatedsentence != '' and translatedsentence != '<strring name=': # strring name is debugging
        translator = Translator(from_lang='en', to_lang=targetLanguage)
        translated_text = translator.translate(translatedsentence)
        return translated_text
    # google translate api
#        translator = Translator()
#        translated_text = translator.translate(translatedsentence, dest=targetLanguage)
#        return translated_text.text
    else:
        return ""






globalFile = "input path"
targetFile = "target path"
targetLanguage = 'tr'
readingFile(globalFile)
# <string name="{......}">SENTENCE</string>
