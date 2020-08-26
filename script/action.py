from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QLabel
from qgis.PyQt.QtGui import QImage, QPixmap
from qgis.utils import iface
import sqlite3

UNIQUE_FIELD = "unique_field_name"
BLOB_FIELD = "picture_field_name"
FIELD_VALUE = '[%unique_field_name%]'

vl = iface.activeLayer()
pr = vl.dataProvider()
db = pr.dataSourceUri().split(' ')[0].replace('dbname=','').replace("'","")
conn = sqlite3.connect(db)
sql = "SELECT {0} FROM {1} WHERE {2}={3}".format(BLOB_FIELD, vl.name(), 
                                                 UNIQUE_FIELD, FIELD_VALUE)
c = conn.cursor()
c.execute(sql)
rows = c.fetchone()
c.close()
conn.close()

qimg = QImage.fromData(rows[0])
pixmap = QPixmap.fromImage(qimg)

label = QLabel()
h = label.height()
w = label.width()
label.setPixmap(pixmap.scaled(w,h,Qt.KeepAspectRatio))
label.show()