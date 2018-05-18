import openpyxl, subprocess, time

class Save():
    def __init__(self, workbook):
        self.workbook = workbook

    def saving(self):
        wb = openpyxl.load_workbook(self.workbook)
        wb.save(self.workbook)

class Update(Save):
    def __init__(self, workbook, opener):
        Save.__init__(self, workbook)
        self.opener = 'open'

    def save(self):
        wb = openpyxl.load_workbook(self.workbook)
        wb.save(self.workbook)

    def openXL(self):
        print('Opening...')
        time.sleep(2)
        subprocess.call([self.opener, self.workbook])
        
