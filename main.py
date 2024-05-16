# -*- coding: utf-8 -*-
from weasyprint import HTML

html_content = """

"""

# HTML을 PDF로 변환
HTML(string=html_content).write_pdf("output.pdf")
