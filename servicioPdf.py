from fpdf import FPDF


class PDF(FPDF):
    pass

    def texts(self, text):
        self.set_xy(10.0, 80.0)
        self.set_text_color(76.0, 32.0, 250.0)
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, text)


pdf = PDF()
pdf.add_page()
pdf.texts('Hola como te llamas? mas texto a ver si le gusta esto')
pdf.set_author('Sebastian Diaz Torres')
pdf.output('test.pdf', 'F')
