class FileMaster():
    
    def __init__(self, filepath):
        #Your code here

        self.filepath = filepath
        
    def extension(self):
        loc = self.filepath.split('.')
        extension = loc[-1]
        return extension
    def filename(self):
        #Your code here
        loc = self.filepath.split('/')
        filename = self.filepath[-9:-4]
        return loc[-1].split('.')[0]
    def dirpath(self):
        loc = self.filepath.split('/')
        loc.pop(-1)     
        return "/".join(loc)+"/"
        #Your code here


master = FileMaster('/Users/person1/Pictures/house.png')

print(master.extension())
print(master.filename())
print(master.dirpath())