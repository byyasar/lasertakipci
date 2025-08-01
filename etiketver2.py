from fpdf.fpdf import FPDF
import math



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
   ("CE", "CE"),
   ("1", "1"), ("1", "1"), ("1", "1"), ("1", "1"), ("1", "1"), ("1", "1"),
]

class PDF(FPDF):
    def rounded_rect(self, x, y, w, h, r, style=''):
        '''Draw a rounded rectangle'''
        k = self.k
        hp = self.h
        if style=='F':
            op='f'
        elif style=='FD' or style=='DF':
            op='B'
        else:
            op='S'
        # Scale by k for page units
        myArc = 4/3 * (math.sqrt(2) - 1)
        self._out('%.2F %.2F m' % ((x+r)*k,(hp-y)*k))
        xc = x+w-r
        yc = y+r
        self._out('%.2F %.2F l' % (xc*k,(hp-y)*k))
        self.curve(xc+r*myArc, y, xc+r, y+r*myArc, xc+r, y+r)
        xc = x+w-r
        yc = y+h-r
        self._out('%.2F %.2F l' % ((x+w)*k,(hp-yc)*k))
        self.curve(xc+r, yc+r*myArc, xc+r*myArc, yc+r, xc, yc+r)
        xc = x+r
        yc = y+h-r
        self._out('%.2F %.2F l' % (xc*k,(hp-(y+h))*k))
        self.curve(xc-r*myArc, yc+r, xc-r, yc+r*myArc, xc-r, yc)
        xc = x+r
        yc = y+r
        self._out('%.2F %.2F l' % (x*k,(hp-yc)*k))
        self.curve(xc-r, yc-r*myArc, xc-r*myArc, yc-r, xc, yc-r)
        self._out(op)

    def curve(self, x1, y1, x2, y2, x3, y3):
        '''Draw a Bezier curve'''
        k = self.k
        hp = self.h
        self._out('%.2F %.2F %.2F %.2F %.2F %.2F c' %
            (x1*k, (hp-y1)*k,
             x2*k, (hp-y2)*k,
             x3*k, (hp-y3)*k))

# PDF oluştur
pdf = PDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

# Font ekle
pdf.add_font("RobotoMono", style="B", fname="Roboto-Regular.ttf", uni=True)
pdf.set_font("RobotoMono", style="B", size=6)

# Yerleşim ayarları
cols = 6  # Yatay sayı
rows = 30  # Dikey sayı
margin_top = 15  # Üst kenar boşluğu (mm)
margin_side = 5  # Yan kenar boşluğu (mm)
margin_bottom = 13.5  # Alt kenar boşluğu (mm)
box_width = 30  # Etiket genişliği (mm)
box_height = 9  # Etiket yüksekliği (mm)
gap_horizontal = 4  # Yatay karakter sıklığı (mm)
gap_vertical = 0  # Dikey karakter sıklığı (mm)

# Kullanılabilir yükseklik hesaplama
usable_height = 297 - margin_top - margin_bottom  # A4 yüksekliği - üst ve alt boşluklar
# Dikey boşluk hesaplama
total_vertical_gap = usable_height - (rows * box_height)  # Toplam dikey boşluk
gap_vertical = total_vertical_gap / (rows - 1)  # Etiketler arası dikey boşluk

# Radius değeri (köşe yuvarlaklığı)
radius = 2

# Hücreleri çiz
for idx, (pin, desc) in enumerate(pin_labels):
    # Her sayfada rows * cols kadar etiket olacak (30 * 6 = 180)
    if idx > 0 and idx % (rows * cols) == 0:
        pdf.add_page()
    
    # Sayfa içindeki pozisyonu hesapla
    idx_in_page = idx % (rows * cols)
    col = idx_in_page % cols
    row = idx_in_page // cols
    
    x = margin_side + col * (box_width + gap_horizontal)
    y = margin_top + row * (box_height + gap_vertical)

    # Etiket çerçevesi (8mm yükseklik)
    inner_margin = 0.5  # İç kenar boşluğu (mm)
    pdf.rounded_rect(x + inner_margin, y + inner_margin, box_width - (2 * inner_margin), 8, radius, style='D')

    # Sıra numarasını yazdır
    pdf.set_text_color(0, 0, 0)  # Siyah yazı
    pdf.set_xy(x + 1, y + 3)  # y+3 ile dikeyde ortalama
    pdf.cell(box_width - 2, 3, str(idx + 1), align='C')  # Sıra numarasını ortala

    # Ortadan dikey çizgi
    pdf.set_draw_color(0, 0, 0)  # Siyah çizgi
    pdf.line(x + box_width / 2, y + inner_margin, x + box_width / 2, y + inner_margin + 8)

# PDF dosyayı kaydet
pdf.output("arduino_mega_etiketleri_radiuslu3.pdf")
