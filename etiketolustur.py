from fpdf import FPDF

# Etiket verileri
pin_labels = [
    ("0", "RX0"), ("1", "TX0"), ("2", "INT4/PWM"), ("3", "INT5/PWM"), ("4", "PWM"), ("5", "PWM"), 
    ("6", "PWM"), ("7", "PWM"), ("8", "DIO"), ("9", "PWM"), ("10", "PWM/SS"), ("11", "PWM/MOSI"), 
    ("12", "MISO"), ("13", "SCK/LED"), ("14", "TX3"), ("15", "RX3"), ("16", "TX2"), ("17", "RX2"), 
    ("18", "TX1/INT3"), ("19", "RX1/INT2"), ("20", "SDA/INT1"), ("21", "SCL/INT0"), ("22", "DIO"), 
    ("23", "DIO"), ("24", "DIO"), ("25", "DIO"), ("26", "DIO"), ("27", "DIO"), ("28", "DIO"), 
    ("29", "DIO"), ("30", "DIO"), ("31", "DIO"), ("32", "DIO"), ("33", "DIO"), ("34", "DIO"), 
    ("35", "DIO"), ("36", "DIO"), ("37", "DIO"), ("38", "DIO"), ("39", "DIO"), ("40", "DIO"), 
    ("41", "DIO"), ("42", "DIO"), ("43", "DIO"), ("44", "PWM"), ("45", "PWM"), ("46", "PWM"), 
    ("47", "DIO"), ("48", "DIO"), ("49", "DIO"), ("50", "MISO"), ("51", "MOSI"), ("52", "SCK"), 
    ("53", "SS"), ("A0", "AI0"), ("A1", "AI1"), ("A2", "AI2"), ("A3", "AI3"), ("A4", "AI4"), 
    ("A5", "AI5"), ("A6", "AI6"), ("A7", "AI7"), ("A8", "AI8"), ("A9", "AI9"), ("A10", "AI10"), 
    ("A11", "AI11"), ("A12", "AI12"), ("A13", "AI13"), ("A14", "AI14"), ("A15", "AI15"), 
    ("VIN", "Vss"), ("GND", "Ground"), ("5V", "Vcc"), ("3.3V", "Vdd"), ("RESET", "Reset"), 
    ("IOREF", "IO Ref"), ("AREF", "ADC Ref"), ("GND", "Ground"), ("5V", "Vcc"), ("GND", "Ground"),
    ("5V", "Vcc"), ("5V", "Vcc"), ("GND", "Ground"), ("5V", "Vcc"), ("5V", "Vcc"), ("GND", "Ground"),
    ("5V", "Vcc"), ("5V", "Vcc"), ("GND", "Ground"), ("CE", "CE"), ("CLK", "CLK"), 
    ("TRIG", "Trigger"), ("ECHO", "Echo"),
]

# PDF ayarları
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.add_font("RobotoMono","", "Roboto-Regular.ttf")
pdf.set_font("RobotoMono", size=9)

# Yerleşim ayarları
cols = 3
rows = 32
margin = 10
gap = 1  # mm
usable_width = 210 - 2 * margin - (cols - 1) * gap
usable_height = 297 - 2 * margin - (rows - 1) * gap
box_width = usable_width / cols
box_height = usable_height / rows

# Etiketleri yerleştir
for idx, (pin, desc) in enumerate(pin_labels):
    col = idx % cols
    row = idx // cols
    if row >= rows:
        break

    x = margin + col * (box_width + gap)
    y = margin + row * (box_height + gap)

    # Hücre kenarlığı
    pdf.rect(x, y, box_width, box_height)

    # Hücre ortasına dikey çizgi
    pdf.line(x + box_width / 2, y, x + box_width / 2, y + box_height)

    # Sol hizalı metin
    pdf.set_xy(x + 1, y + 2)
    pdf.cell((box_width / 2) - 2, 4, f"{pin}{" "}:{" "}{desc}", align='L')

    # Sağ hizalı tekrar metni
    pdf.set_xy(x + box_width / 2 + 1, y + 2)
    pdf.cell((box_width / 2) - 2, 4, f"{desc}{" "}:{" "}{pin}", align='R')

# PDF çıktısı
pdf.output("arduino_mega_pin_etiketleri_hizali2.pdf")
