from fpdf import FPDF

def main():
    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_font('Arial', 'B', 16)
    pdf.add_page()
    text = "CS50 Shirtificate"
    text_width = pdf.get_string_width(text)
    start_x = (pdf.w - text_width) / 2
    y = 50
    image_path = "shirtificate.png"
    image_width = 50
    pdf.image(image_path, x=start_x, y=y, w=image_width)
    pdf.set_xy(start_x, y)
    pdf.cell(text_width, 10, txt=text, ln=True, align='C')
    start_x = (pdf.w - image_width) / 2

    pdf.output("shirtificate.pdf")


main()
