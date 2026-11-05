from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, Color

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'packet/grade5_geography_map_skills_review.pdf'
W,H=A4
c=canvas.Canvas(str(OUT),pagesize=A4)
c.setTitle('Grade 5 Geography Map Skills Review - A4 Print Edition')
c.setAuthor('Codex')
NAVY=HexColor('#17324d');TEAL=HexColor('#087e87');INK=HexColor('#253444')
MUTED=HexColor('#5d7180');LINE=HexColor('#cbd9df');PALE=HexColor('#e8f6f7')
CREAM=HexColor('#fff7e8')

def t(x,y,s,size=10,bold=False,color=INK):
    c.setFillColor(color);c.setFont('Helvetica-Bold' if bold else 'Helvetica',size);c.drawString(x,y,s)
def line(x1,y1,x2,y2):
    c.setStrokeColor(LINE);c.setLineWidth(.8);c.line(x1,y1,x2,y2)
def box(x,y,w,h,fill):
    c.setFillColor(fill);c.roundRect(x,y,w,h,9,fill=1,stroke=0)
def header(sub):
    c.setFillColor(NAVY);c.rect(0,H-70,W,70,fill=1,stroke=0)
    t(40,H-34,'GEOGRAPHY  /  MAP SKILLS',18,True,Color(1,1,1))
    t(41,H-54,sub,10,False,HexColor('#c9e7eb'))
def footer(n):
    line(40,37,W-40,37);t(40,23,'Grade 5 Review Packet  |  A4 print edition',8,False,MUTED)
    c.setFillColor(MUTED);c.setFont('Helvetica',8);c.drawRightString(W-40,23,str(n))
def mc(y,n,q,opts):
    t(43,y,f'{n}. {q}',10,True)
    t(63,y-18,'    '.join(f'{a} {b}' for a,b in opts),9.3)
def short(y,n,q,lines=2):
    t(43,y,f'{n}. {q}',10,True)
    for k in range(lines):line(63,y-19-k*17,W-43,y-19-k*17)

# 1 terms
header('Learn the terms, then read two published maps')
t(40,743,'Name  _____________________________________    Date  __________________',10)
box(40,678,W-80,43,CREAM)
t(56,699,'Your mission',11,True,NAVY)
t(56,684,'Use the maps as evidence for every answer.',9.6)
terms=[
 ('Legend or key','Explains the meaning of symbols and colors.'),
 ('Compass rose','Shows north, south, east, and west.'),
 ('Scale','Shows how map distance relates to real distance.'),
 ('Latitude','East-west lines that measure north or south of the equator.'),
 ('Longitude','North-south lines that measure east or west of the prime meridian.'),
 ('Equator','0° latitude; divides Northern and Southern Hemispheres.'),
 ('Prime meridian','0° longitude; divides Eastern and Western Hemispheres.'),
]
y=643
for name,meaning in terms:
    c.setStrokeColor(LINE);c.setFillColor(Color(1,1,1));c.roundRect(40,y-12,W-80,47,7,fill=1,stroke=1)
    box(48,y-4,137,31,PALE)
    t(58,y+8,name,10,True,TEAL);t(195,y+8,meaning,9.4)
    y-=53
box(40,76,W-80,125,CREAM)
t(56,178,'Remember',11,True,NAVY)
t(56,153,'Latitude lines run across; longitude lines run from pole to pole.',9.8)
t(56,130,'Write coordinates in this order: latitude, then longitude.',9.8,True)
t(56,107,'Use the scale bar for distance estimates on a resized map.',9.8)
footer(1);c.showPage()

# 2 authentic NPS map, scaled for A4
t(57,817,'MAP 1  /  HAMPTON NATIONAL HISTORIC SITE',13,True,NAVY)
c.drawImage(str(ROOT/'assets/hampton_map_crop.png'),57,52,width=481,height=752,mask='auto')
t(57,38,'Official National Park Service classroom map. Use the scale bar for distance.',7.7,False,MUTED)
c.linkURL('https://www.nps.gov/common/uploads/teachers/lessonplans/HAMP%20scavenger.pdf',(57,30,538,47),relative=0)
c.showPage()

# 3 park questions
header('Questions  /  Hampton National Historic Site')
t(40,745,'Use the published park map on page 2.',10)
mc(710,1,'What does the boxed P symbol mean?', [('A.','Parking'),('B.','Picnic area'),('C.','Path')])
mc(665,2,'Which direction is the Farm House from the Mansion?', [('A.','Southwest'),('B.','Northeast'),('C.','West')])
mc(620,3,'Which place is south of the Mansion?', [('A.','Gardens'),('B.','Farm House'),('C.','Stables')])
mc(575,4,'What road passes between the Farm House and Mansion?', [('A.','Park Road'),('B.','Hampton Lane'),('C.','Garden Lane')])
mc(530,5,'What unit is used in the map scale?', [('A.','Miles'),('B.','Kilometers'),('C.','Feet')])
mc(485,6,'Which direction is at the top of the compass rose?', [('A.','North'),('B.','East'),('C.','South')])
short(430,7,'Name two visitor services shown in the legend.',2)
short(354,8,'Name two labeled places north of Hampton Lane.',2)
t(43,278,'9. Estimate the straight-line distance from the Visitor Center to the Mansion.',10,True)
t(62,260,'Use the scale bar. About how many feet is it?',10,True)
line(63,238,W-43,238);line(63,221,W-43,221)
short(176,10,'Why might the walking distance be longer than your estimate?',2)
footer(3);c.showPage()

# 4 authentic NOAA graphic
header('Map 2  /  Latitude and longitude on Earth')
t(40,742,'The lines and Earth image below come from a NOAA learning map.',10)
c.drawImage(str(ROOT/'assets/noaa_latlong.jpg'),37,166,width=520,height=520,mask='auto')
box(40,89,W-80,55,PALE)
t(55,121,'Read the labels on the globe.',10.5,True,NAVY)
t(55,101,'White lines: equator and prime meridian. Blue lines: other degrees.',9.5)
t(40,66,'Source: NOAA Science On a Sphere, Latitude Longitude Layers.',8.2,False,MUTED)
c.linkURL('https://sos.noaa.gov/catalog/datasets/latitude-longitude-layers/',(40,55,530,77),relative=0)
footer(4);c.showPage()

# 5 world questions
header('Questions  /  NOAA latitude-longitude map')
t(40,745,'Use the published NOAA map on page 4.',10)
mc(710,11,'Which line is 0° latitude?', [('A.','Equator'),('B.','Prime meridian'),('C.','30°W')])
mc(665,12,'Which line is 0° longitude?', [('A.','30°S'),('B.','Equator'),('C.','Prime meridian')])
mc(620,13,'Which label is west of the prime meridian?', [('A.','30°E'),('B.','30°W'),('C.','30°N')])
mc(575,14,'Which line is south of the equator?', [('A.','30°S'),('B.','30°N'),('C.','0°')])
mc(530,15,'Where do 0° latitude and 0° longitude meet?', [('A.','In Africa'),('B.','In the Atlantic Ocean'),('C.','In Europe')])
mc(485,16,'Which line runs from north to south?', [('A.','Equator'),('B.','Prime meridian'),('C.','30°S')])
short(430,17,'Why is Africa in both Northern and Southern Hemispheres?',2)
short(352,18,'What are the coordinates where 30°E meets the equator?',2)
short(274,19,'Name the hemispheres at 30°S, 30°W.',2)
short(196,20,'Explain how latitude differs from longitude.',3)
footer(5);c.showPage()

# 6 answer key
header('Teacher answer key')
t(40,742,'Accept similar wording and reasonable distance estimates.',10)
t(40,711,'Hampton National Historic Site',12.5,True,NAVY)
answers1=[
 '1. A. Parking.', '2. B. Northeast.', '3. A. Gardens.', '4. B. Hampton Lane.',
 '5. C. Feet.', '6. A. North.',
 '7. Any two: restrooms, parking, picnic tables, accessible entrance.',
 '8. Farm House and slave quarters.',
 '9. About 700-800 feet, using roughly three 250-foot scale bars.',
 '10. The walking paths curve rather than following a straight line.'
]
y=685
for a in answers1:t(50,y,a,9.5);y-=27
t(40,390,'NOAA latitude-longitude map',12.5,True,NAVY)
answers2=[
 '11. A. Equator.', '12. C. Prime meridian.', '13. B. 30°W.',
 '14. A. 30°S.', '15. B. In the Atlantic Ocean.',
 '16. B. Prime meridian.', '17. The equator crosses Africa.',
 '18. 0° latitude, 30°E longitude.',
 '19. Southern and Western Hemispheres.',
 '20. Latitude measures north or south; longitude measures east or west.'
]
y=363
for a in answers2:t(50,y,a,9.5);y-=27
footer(6);c.showPage()
c.save()
print(OUT,OUT.stat().st_size)

