from fpdf import FPDF


def main():
    name = input("Name: ")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Times", "B", size=40)
    pdf.cell(190, 10, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.image("shirtificate.png", x=0, y=60)
    pdf.set_font("Times", size=30)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.cell(190, 240, name + " took CS50", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.output("shirtificate.pdf")
if __name__ == "__main__":
    main()