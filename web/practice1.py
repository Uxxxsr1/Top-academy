from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        return 'file is opened'
    def save(self):
        return 'file is saved'
class SpreadSheetDocument(Document):
    def open(self):
        pass
    def save(self):
        pass
    def show0(self):
        return 'open presentation'
class TextDocument(Document):
    def open(self):
        pass
    def save(self):
        pass
    def show1(self):
        return 'open text document'
class DocumentFactory:
    def createDocument(self, fileType):
        if fileType == 'text':
            return TextDocument()
        if fileType == 'presentation':
            return SpreadSheetDocument()
        else: 
            raise ValueError('unknow')
factory = DocumentFactory()
document = factory.createDocument('text')
document1 = factory.createDocument('presentation')
print(document.open())
print(document1.save())