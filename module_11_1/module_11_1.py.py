import openpyxl

from take_information_from_drom import array

def writer(parametr):
    """Функция принимает итерируемый объект и записывает получаемые данные в Excel фаил"""
    book = openpyxl.Workbook()

    wb = book.worksheets[0]
    wb.title = "Веста дром"
    
    wb["A1"] = "Имя"
    wb["B1"] = "Цена"
    wb["C1"] = "Пробег"
    wb["D1"] = "Ссылка"
        
    row = 2
    column = 0
    

    for item in parametr:
        wb[row][column].value = item[0]
        wb[row][column + 1].value = item[1]
        wb[row][column + 2].value = item[2]
        wb[row][column + 3].value = item[3]
        
        row += 1

    book.save("./module_11_1/Vesta.xlsx")
    book.close()



writer(array())
