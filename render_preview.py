import os, subprocess, pypdf

work_dir = r'f:\SLIIT Y3 , S1\IE3142 - DevOps Security [2026JUL]\IE3142---DevOps-Security-'
os.chdir(work_dir)

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
html_file = os.path.abspath('IE3142_Reference_Sheet_V1_Source.html')
pdf_file = os.path.abspath('IE3142_Reference_Sheet_V1.pdf')

# 1. Compile PDF
cmd = [chrome_path, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf_file}', html_file]
res = subprocess.run(cmd, capture_output=True, text=True)
print('PDF Render exit code:', res.returncode)

# 2. Check PDF page count and sizes
reader = pypdf.PdfReader(pdf_file)
print('PDF Page count:', len(reader.pages))
for i, page in enumerate(reader.pages):
    print(f'Page {i+1} MediaBox: {page.mediabox}')

# 3. Create individual page HTML files for screenshot rendering
with open('IE3142_Reference_Sheet_V1_Source.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Separate Page 1 and Page 2
pages = html.split('<div class="page">')
head = pages[0]
p1_body = pages[1].split('</div>\n\n<!-- =====')[0]
p2_body = pages[2].split('</body>')[0]

p1_html = head + '<div class="page" style="height:287mm;">' + p1_body + '</div></body></html>'
p2_html = head + '<div class="page" style="height:287mm;">' + p2_body + '</body></html>'

with open('p1_temp.html', 'w', encoding='utf-8') as f:
    f.write(p1_html)
with open('p2_temp.html', 'w', encoding='utf-8') as f:
    f.write(p2_html)

# Screenshot Page 1 and Page 2 at 1240 x 1754 (A4 ratio)
p1_img = os.path.abspath('IE3142_Reference_Sheet_V1_Page_1.png')
p2_img = os.path.abspath('IE3142_Reference_Sheet_V1_Page_2.png')

cmd1 = [chrome_path, '--headless=new', '--disable-gpu', '--window-size=1240,1754', f'--screenshot={p1_img}', os.path.abspath('p1_temp.html')]
cmd2 = [chrome_path, '--headless=new', '--disable-gpu', '--window-size=1240,1754', f'--screenshot={p2_img}', os.path.abspath('p2_temp.html')]

subprocess.run(cmd1, capture_output=True)
subprocess.run(cmd2, capture_output=True)

if os.path.exists('p1_temp.html'): os.remove('p1_temp.html')
if os.path.exists('p2_temp.html'): os.remove('p2_temp.html')

print('P1 image exists:', os.path.exists('IE3142_Reference_Sheet_V1_Page_1.png'), 'size:', os.path.getsize('IE3142_Reference_Sheet_V1_Page_1.png'))
print('P2 image exists:', os.path.exists('IE3142_Reference_Sheet_V1_Page_2.png'), 'size:', os.path.getsize('IE3142_Reference_Sheet_V1_Page_2.png'))
