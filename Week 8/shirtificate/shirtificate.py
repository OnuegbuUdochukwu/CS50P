from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

top_text = "CS50 Shirtificate"
# text = "Udochukwu took CS50"
name = input("Name: ")
text = f"{name.title()} took CS50"

pdf.image("shirtificate.png", x=0, y=50)
pdf.set_font("Helvetica", size=36)
pdf.cell(text = top_text, center = True)


# Get the width of the page and the width of the text
page_width = pdf.w
text_width = pdf.get_string_width(text)

# Calculate the X position to center the text
x_position = (page_width - text_width) / 2

# Move to the center and print the text
pdf.set_xy(x_position, 100)  # 50 is the Y position (adjust as needed)
pdf.set_font("Times", size=24)
pdf.set_text_color(255, 255, 255)
pdf.cell(text_width, 10, text, align='C')  # 10 is the height of the cell

pdf.output("shirtificate.pdf")