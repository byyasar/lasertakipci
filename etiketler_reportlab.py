from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def mm(val):
    return val * 2.83465  # 1 mm = 2.83465 point

# Etiket verileri - Gruplandırılmış halde
pin_labels = [
    # GND Etiketleri
    ("GND", "Ground"), ("GND", "Ground"), ("GND", "Ground"),
    ("GND", "Ground"), ("GND", "Ground"), ("GND", "Ground"),
    ("GND", "Ground"), ("GND", "Ground"), ("GND", "Ground"),
    ("GND", "Ground"), ("GND", "Ground"), ("GND", "Ground"),
    ("GND", "Ground"), ("GND", "Ground"), ("GND", "Ground"),
    
    # 5V Etiketleri
    ("5V", "Vcc"), ("5V", "Vcc"), ("5V", "Vcc"),
    ("5V", "Vcc"), ("5V", "Vcc"), ("5V", "Vcc"),
    ("5V", "Vcc"), ("5V", "Vcc"), ("5V", "Vcc"),
    ("5V", "Vcc"), ("5V", "Vcc"), ("5V", "Vcc"),
    ("5V", "Vcc"), ("5V", "Vcc"), ("5V", "Vcc"),
    ("5V", "Vcc"), ("5V", "Vcc"), ("5V", "Vcc"),
    ("5V", "Vcc"), ("5V", "Vcc"), ("5V", "Vcc"),

    # 3.3V Etiketi
    ("3.3V", "Vdd"), ("3.3V", "Vdd"), ("3.3V", "Vdd"),
    ("3.3V", "Vdd"), ("3.3V", "Vdd"), ("3.3V", "Vdd"),
    ("3.3V", "Vdd"), ("3.3V", "Vdd"), ("3.3V", "Vdd"),
    ("3.3V", "Vdd"), ("3.3V", "Vdd"), ("3.3V", "Vdd"),
   
    ("3.3V", "Vdd"), ("3.3V", "Vdd"), ("3.3V", "Vdd"),
   
    
    # Diğer Güç ve Referans Pinleri
    ("VIN", "Vss"), ("IOREF", "IO Ref"), ("AREF", "ADC Ref"),
    ("RESET", "Reset"),
    
    # Analog Pinler
    ("A0", "AI0"), ("A1", "AI1"), ("A2", "AI2"), ("A3", "AI3"), 
    ("A4", "AI4"), ("A5", "AI5"), ("A6", "AI6"), ("A7", "AI7"), 
    ("A8", "AI8"), ("A9", "AI9"), ("A10", "AI10"), ("A11", "AI11"), 
    ("A12", "AI12"), ("A13", "AI13"), ("A14", "AI14"), ("A15", "AI15"),
    
    # PWM Pinleri
    ("2", "INT4/PWM"), ("3", "INT5/PWM"), ("4", "PWM"), ("5", "PWM"),
    ("6", "PWM"), ("7", "PWM"), ("9", "PWM"),
    ("44", "PWM"), ("45", "PWM"), ("46", "PWM"),
    
    # UART Pinleri (RX/TX)
    ("0", "RX0"), ("1", "TX0"), 
    ("14", "TX3"), ("15", "RX3"), 
    ("16", "TX2"), ("17", "RX2"), 
    ("18", "TX1/INT3"), ("19", "RX1/INT2"),
    
    # SPI Pinleri
    ("50", "MISO"), ("51", "MOSI"), ("52", "SCK"), ("53", "SS"),
    ("50", "MISO"), ("51", "MOSI"), ("52", "SCK"), ("53", "SS"),
    ("50", "MISO"), ("51", "MOSI"), ("52", "SCK"), ("53", "SS"),
    ("10", "PWM/SS"), ("11", "MOSI"), ("12", "MISO"), ("13", "SCK/LED"),
    
    # I2C Pinleri
    ("20", "SDA/INT1"), ("21", "SCL/INT0"),
    ("20", "SDA/INT1"), ("21", "SCL/INT0"),
    ("20", "SDA/INT1"), ("21", "SCL/INT0"),
    ("20", "SDA/INT1"), ("21", "SCL/INT0"),
    ("20", "SDA/INT1"), ("21", "SCL/INT0"),
    ("20", "SDA/INT1"), ("21", "SCL/INT0"),
    
    # Dijital I/O Pinler
    ("8", "DIO"),
    ("22", "DIO"), ("23", "DIO"), ("24", "DIO"), ("25", "DIO"),
    ("26", "DIO"), ("27", "DIO"), ("28", "DIO"), ("29", "DIO"),
    ("30", "DIO"), ("31", "DIO"), ("32", "DIO"), ("33", "DIO"),
    ("34", "DIO"), ("35", "DIO"), ("36", "DIO"), ("37", "DIO"),
    ("38", "DIO"), ("39", "DIO"), ("40", "DIO"), ("41", "DIO"),
    ("42", "DIO"), ("43", "DIO"), ("47", "DIO"), ("48", "DIO"),
    ("49", "DIO"),
    ("8", "DIO"),
    ("22", "DIO"), ("23", "DIO"), ("24", "DIO"), ("25", "DIO"),
    ("26", "DIO"), ("27", "DIO"), ("28", "DIO"), ("29", "DIO"),
    ("30", "DIO"), ("31", "DIO"), ("32", "DIO"), ("33", "DIO"),
    ("34", "DIO"), ("35", "DIO"), ("36", "DIO"), ("37", "DIO"),
    ("38", "DIO"), ("39", "DIO"), ("40", "DIO"), ("41", "DIO"),
    ("42", "DIO"), ("43", "DIO"), ("47", "DIO"), ("48", "DIO"),
    ("49", "DIO"),
    
    # Sensör Pinleri
    ("CE", "CE"), ("CLK", "CLK"), ("TRIG", "Trigger"), ("ECHO", "Echo"),
   ("CE", "CE"), ("1", "1"), ("2", "2"),("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), 
]

# Sayfa ve etiket ayarları
PAGE_WIDTH, PAGE_HEIGHT = A4
cols = 6
rows = 30
margin_top = 15
margin_bottom = 12
margin_side = 5
box_width = 30  # Etiket genişliği (mm)
box_height = 9  # Etiket yüksekliği (mm)
gap_horizontal = 4  # Yatay karakter sıklığı (mm)
usable_height = 297 - margin_top - margin_bottom
if rows > 1:
    gap_vertical = (usable_height - (rows * box_height)) / (rows - 1)
else:
    gap_vertical = 0

c = canvas.Canvas("etiketler_v3.pdf", pagesize=A4)

for idx, (pin, desc) in enumerate(pin_labels):
    if idx >= 180:  # 175'ten sonraki etiketleri atla
        break
    col = idx % cols
    row = idx // cols
    x = mm(margin_side + col * (box_width + gap_horizontal))
    y = mm(297 - margin_top - (row + 1) * box_height - row * gap_vertical)
    # Etiket grubuna göre arkaplan rengi
    if 'GND' in pin or 'GND' in desc:
        c.setFillColor(colors.Color(0, 0, 0, alpha=0.5))  # Siyah, yarı şeffaf
    elif '5V' in pin or '5V' in desc:
        c.setFillColor(colors.Color(1, 0, 0, alpha=0.5))  # Kırmızı, yarı şeffaf
    elif '3.3V' in pin or '3.3V' in desc:
        c.setFillColor(colors.Color(1, 0.5, 0, alpha=0.5))  # Turuncu, yarı şeffaf
    elif 'SDA' in pin or 'SDA' in desc:  # I2C pinleri
        c.setFillColor(colors.Color(0, 0, 1, alpha=0.5))  # Mavi, yarı şeffaf
    elif 'SCL' in pin or 'SCL' in desc:  # I2C pinleri
        c.setFillColor(colors.Color(0, 0, 1, alpha=0.5))  # Mavi, yarı şeffaf
    elif 'MOSI' in pin or 'MOSI' in desc:  # SPI pinleri
        c.setFillColor(colors.Color(0, 1, 0, alpha=0.5))  # Yeşil, yarı şeffaf
    elif 'MISO' in pin or 'MISO' in desc:  # SPI pinleri
        c.setFillColor(colors.Color(0, 1, 0, alpha=0.5))  # Yeşil, yarı şeffaf
    elif 'SCK' in pin or 'SCK' in desc:  # SPI pinleri
        c.setFillColor(colors.Color(0, 1, 0, alpha=0.5))  # Yeşil, yarı şeffaf
    elif 'SS' in pin or 'SS' in desc:  # SPI pinleri
        c.setFillColor(colors.Color(0, 1, 0, alpha=0.5))  # Yeşil, yarı şeffaf
    else:
        c.setFillColor(colors.Color(1, 1, 1, alpha=0.5))  # Beyaz, yarı şeffaf
    c.setStrokeColor(colors.black)  # Dış çerçeve her zaman siyah
    c.roundRect(x + mm(1), y + mm(1), mm(28), mm(7), mm(2), stroke=1, fill=1)
    # Ortadaki dik çizgi
    if 'GND' in pin or '5V' in pin:
        c.setStrokeColor(colors.white)  # GND ve 5V için beyaz çizgi
    else:
        c.setStrokeColor(colors.black)  # Diğerleri için siyah çizgi
    c.line(x + mm(15), y + mm(1), x + mm(15), y + mm(8))
    # Pin ve açıklama (sola dayalı)
    c.setFont("Helvetica-Bold", 6)
    if 'GND' in pin or '5V' in pin:
        c.setFillColor(colors.white)  # GND ve 5V için beyaz font
    else:
        c.setFillColor(colors.black)  # Diğerleri için siyah font
    # Sol bölüm için metin genişliğini hesapla
    left_text = f"{pin} - {desc}"
    left_text_width = c.stringWidth(left_text, "Helvetica-Bold", 6)
    left_center_x = x + mm(2) + (mm(14) - left_text_width) / 2
    c.drawString(left_center_x, y + mm(box_height/2) - 1, left_text)
    # Açıklama (sağa dayalı)
    # Sağ bölüm için metin genişliğini hesapla
    right_text = f"{pin} - {desc}"
    right_text_width = c.stringWidth(right_text, "Helvetica-Bold", 6)
    right_center_x = x + mm(15) + (mm(14) - right_text_width) / 2
    c.drawString(right_center_x, y + mm(box_height/2) - 1, right_text)

c.save() 