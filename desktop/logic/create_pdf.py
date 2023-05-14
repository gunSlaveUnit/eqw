from fpdf import FPDF

class PDFCreator:
    def create_pdf(self, first_column, second_column):
        pdf = FPDF()
        pdf.add_page()
        header = 'Ваши проверки'
        # Шрифты
        pdf.add_font('PTSans', '', 'C:\eqw\desktop\materials\PT_Sans-Regular.ttf', uni=True)
        pdf.set_font('PTSans', '', 14)
        pdf.cell(40, 10, header)
        pdf.ln()

        pdf.set_font('PTSans', '', 12)
        # Ширина колонок
        col_width = pdf.w / 2.2
        # Выравнивание
        pdf.ln(1)
        th = pdf.font_size

        # Шапка таблицы
        header1 = 'Дата'
        header2 = 'Результат'
        pdf.cell(col_width, 2 * th, header1, border=0)
        pdf.cell(col_width, 2 * th, header2, border=0)
        pdf.ln()

        # Данные таблицы
        pdf.set_font('PTSans', '', 12)
        for row in zip(first_column, second_column):
            # Определяем высоту ячейки на основе текста
            # Устанавливаем высоту ячейки для переноса строки
            pdf.cell(col_width, th, str(row[0]), border=0)
            pdf.multi_cell(col_width, th, str(row[1]), border=0)
            pdf.ln()

        # Сохраняем PDF-файл
        pdf.output('check.pdf', 'F')