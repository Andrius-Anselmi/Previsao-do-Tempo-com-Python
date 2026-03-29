from fpdf import FPDF

def exportar_pdf(cidade, pais, datas, maximas, minimas, media):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, f"Previsao do Tempo - {cidade}, {pais}", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 10, f"Periodo: {datas[0][5:]} a {datas[-1][5:]}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Temperatura media: {media:.1f}C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, f"Maxima: {max(maximas)}C  |  Minima: {min(minimas)}C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    for i in range(len(datas)):
        data_fmt = datas[i][5:].replace("-", "/")
        pdf.cell(0, 8, f"{data_fmt}  Min: {minimas[i]}C  Max: {maximas[i]}C", new_x="LMARGIN", new_y="NEXT")
    pdf.output(f"previsao_{cidade.lower().replace(' ', '_')}.pdf")
    print("PDF exportado!")
