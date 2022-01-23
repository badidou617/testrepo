# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
#from qt_core import *
import pandas as pd 
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from gui.core.json_themes import Themes
import sys
import os
import PySide6.QtCore
from gui.widgets import *

from qt_material import apply_stylesheet
from qt_material import list_themes
import sys
import os
import PySide6.QtCore
from PySide6.QtCore import QThread, Signal
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *
import numpy as np
# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings
import sys
import time
# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////


# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# //////////////////./////////////////////////////////////////////
from gui.uis.windows.main_window import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////


import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import QChart, QChartView, QPieSeries




# IMPORT QT CORE
class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        MainPages.setStyleSheet("QFrame{\n"
                                         
"    border-radius : 15px;\n"
"    \n"
"    \n"
"}\n"


"QGroupBox {\n"
"    spacing: 5px;\n"
"    color : black ;"
"   font-size: 13px;\n"
"}\n"

"QCheckBox {\n"
"    spacing: 5px;\n"
" color : #1c89ff ;"
"}\n"
""
"QCheckBox::indicator {\n"
"    width: 13px;\n"
"   height: 13px;\n"
"}\n"

"\n"
"QLineEdit{\n"
"    background : transparent;\n"
"    border : none;\n"
"    color : black;\n"
"    border-bottom : 1px solid black;\n"
"    font-size: 12px;\n"
"     font-weight: 200;\n"

"}\n"
"QPushButton{\n"
"    position: relative;\n"
"    \n"
"      width: 200;\n"
"     height: 45;\n"
"      border-radius: 18px;\n"
"     background-color: #1c89ff;\n"
"      border: solid 1px transparent;\n"
"     color: #0e0e0e;\n"
"      font-size: 25;\n"
"     font-weight: 400;\n"
"      \n"
"    font-family: \"Montserrat\"\n"
"}\n"
"QPushButton:hover{\n"
"        background-color : #9fd9ec;\n"
"    text-decoration : underline;\n"
"    color:  #0e0e0e;\n"
"    \n"
"    \n"
"}\n"

"\n"

"QToolBox::tab {\n"
"     border: 1px solid #C4C4C3;\n"
"     border-bottom-color: blue ;\n"  
"     border-radius: 10px;\n"
"     background-color: #bdbdbd;\n"


 
"    font: bold 12px;\n"
                     
"}\n"
"QToolBox::tab:selected {\n"
"      font-size: 14px;\n"

"}\n"
    
 "QToolBox::item {\n"
"     background-color: #922626;\n"
"     border-bottom-style: none;\n"

"}\n"
       
"QLabel{\n"
"    color : black;\n"


"}\n"

"QProgressBar {\n"
"    border: 2px solid #2196F3;\n"
"    border-radius: 5px;\n"
"    background-color: #E0E0E0;\n"
"}\n"
    
"QProgressBar::chunk {\n"
"    background-color: #2196F3;\n"
"    width: 10px; \n"
"    margin: 0.5px;\n"
"}\n"


   
" QTableWidget {\n"
"    background-color:rgba(68, 119, 170, 125);\n"
"    border-radius: 10px;\n"
"}\n"



"")
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(QRect(300, 500, 481, 60))
        """
        self.label.setStyleSheet("QLabel{\n"
"    color : black;\n"
"    font-size: 20px;\n"
"}\n")
        """
        self.center_page_layout.addWidget(self.label)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 840, 580))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)
        
       
        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        ############################################
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        """
        self.empty_page_label = QLabel(self.page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        self.empty_page_label.setFont(font)
        self.empty_page_label.setAlignment(Qt.AlignCenter)
        self.page_3_layout.addWidget(self.empty_page_label)
        """
        self.pushButtonImport = QPushButton(self.page_3)
        self.pushButtonImport.setEnabled(True)
        self.pushButtonImport.setGeometry(QRect(500, 108, 120, 41))
        self.pushButtonImport.setCheckable(False)
        self.pushButtonImport.setChecked(False)
        self.pushButtonImport.setObjectName("pushButtonImport")
        
        self.pushButtonImport.setStyleSheet("QPushButton{\n"
"    position: relative;\n"
"    \n"
"      width: 200;\n"
"     height: 45;\n"
"      border-radius: 18px;\n"
"     background-color: #1c89ff;\n"
"      border: solid 1px transparent;\n"
"     color: #0e0e0e;\n"
"      font-size: 25;\n"
"     font-weight: 400;\n"
"      \n"
"    font-family: \"Montserrat\"\n"
"}\n"
"QPushButton:hover{\n"
"        background-color : #9fd9ec;\n"
"    text-decoration : underline;\n"
"    color:  #0e0e0e;\n"
"    \n"
"    \n"
"}\n")
        self.path = QLineEdit(self.page_3)
        self.path.setGeometry(QRect(80, 110, 401, 51))
        self.path.setText("")
        self.path.setStyleSheet("QLineEdit{\n"
"    background : transparent;\n"
"    border : none;\n"
"    color : gray;\n"
"    border-bottom : 1px solid black;\n"
"    font-size: 18px;\n"
"     font-weight: 300;\n"
"}\n")
        self.path.setObjectName("path")
        self.label_data = QLabel(self.page_3)
        self.label_data.setGeometry(QRect(40, 5, 481, 40))
        
        self.label_data.setAlignment(Qt.AlignCenter)
        self.label_data.setObjectName("label_data")
        
        
        self.pages.addWidget(self.page_3)

        #self.pushButtonImport.clicked.connect(self.openfileT)


        self.page_3_layout.addWidget(self.page_3)
        
      ##########################################  

 # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes2 = Themes()
        self.themes2 = themes2.items

        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")

        self.page_4.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_4_layout = QVBoxLayout(self.page_4)
        self.page_4_layout.setObjectName(u"page_4_layout")
        self.page_4_layout.setGeometry(QRect(150, 300, 1000, 400))
        #self.page_4_layout.setSpacing(10)
        #self.page_4_layout.setContentsMargins(10, 10, 10, 10) 
        """
        self.test = QLabel()
        self.test.setGeometry(QRect(200, 70, 400, 40))        
        self.test.setObjectName("test") 
        self.page_4_layout.addWidget(self.test, 0, Qt.AlignHCenter) 
        """

        self.label_Result = QLabel(self.page_4)
        self.label_Result.setGeometry(QRect(300, 30, 400, 40))
        
        
        self.label_Result.setObjectName("trait")
        
        self.label_Re = QLabel(self.page_4)
        self.label_Re.setGeometry(QRect(160, 120, 500, 40))
        
        
        
        self.label_Re.setObjectName("label_Re")
        
        
        self.pushButtonRe = QPushButton(self.page_4)
        self.pushButtonRe.setGeometry(QRect(650, 117, 120, 41))
        self.pushButtonRe.setObjectName("pushButtonRe")
        self.pushButtonRe.clicked.connect(self.train_func)

        self.progressBarRes = QProgressBar(self.page_4)
        self.progressBarRes.setGeometry(QRect(150, 165, 450, 25))
        self.progressBarRes.setProperty("value", 100)
        self.progressBarRes.setObjectName("progressBar")
        
        self.scroll_area = QScrollArea(self.page_4)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setGeometry(QRect(50, 230, 1000, 350))


        self.table_widgetRes = PyTableWidget(
            radius = 8,
            color = self.themes2["app_color"]["text_foreground"],
            selection_color = self.themes2["app_color"]["context_color"],
            bg_color = self.themes2["app_color"]["bg_two"],
            header_horizontal_color = self.themes2["app_color"]["dark_two"],
            header_vertical_color = self.themes2["app_color"]["bg_three"],
            bottom_line_color = self.themes2["app_color"]["bg_three"],
            grid_line_color = self.themes2["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes2["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes2["app_color"]["dark_four"],
            context_color = self.themes2["app_color"]["context_color"]
        )
        
        self.table_widgetRes.setColumnCount(10)
        self.table_widgetRes.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table_widgetRes.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widgetRes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widgetRes.setRowCount(40)
        self.table_widgetRes.setColumnCount(10)

        self.table_widgetRes.setGeometry(QRect(50, 230, 1000, 350))
        #self.table_widgetRes.setMinimumSize(QSize(700,200))
        #self.table_widgetRes.setMaximumSize(QSize(900,400))
        
        #self.page_4_layout.addWidget(self.table_widgetRes) 
        #self.page_4_layout.addWidget(self.table_widgetRes)  

        self.scroll_area.setWidget(self.table_widgetRes)
         
        self.page_4_layout.addWidget(self.page_4) 
        self.pages.addWidget(self.page_4)  
        
 ############################################

# Page STAT
        # ///////////////////////////////////////////////////////////////
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")

        self.page_5.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_5_layout = QVBoxLayout(self.page_5)
        self.page_5_layout.setObjectName(u"page_5_layout")
        #self.page_5_layout.setGeometry(QRect(150, 300, 1000, 400))
        self.series = QPieSeries()

        self.series.append('Jane', 1)
        self.series.append('Joe', 2)
        self.series.append('Andy', 3)
        self.series.append('Barbara', 4)
        self.series.append('Axel', 5)

        self.slice = self.series.slices()[1]
        self.slice.setExploded()
        self.slice.setLabelVisible()
        self.slice.setPen(QPen(Qt.darkGreen, 2))
        self.slice.setBrush(Qt.green)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle('Simple piechart example')
        self.chart.legend().hide()

        self._chart_view = QChartView(self.chart)
      
        self._chart_view.setRenderHint(QPainter.Antialiasing)
        

        self.pages.addWidget(self.page_5) 
    







 #####################################################
  ############################################

# Page Recherche
        # ///////////////////////////////////////////////////////////////
        
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")

        self.page_6.setStyleSheet(u"QFrame {\n"
"	font-size: 12pt;\n"
"}")


        

        """
        self.verticalScrollBar = QScrollBar(self.page_6)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(1000, 0, 16, 800))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        """
        


        """
        self.scroll_area2 = QScrollArea(self.page_6)
        self.scroll_area2.setObjectName(u"scroll_area")
        self.scroll_area2.setStyleSheet(u"background: black;")
        self.scroll_area2.setFrameShape(QFrame.NoFrame)
        self.scroll_area2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area2.setWidgetResizable(True)
        self.scroll_area2.setGeometry(QRect(10, 10, 900, 800))
        """

        self.groupBox = QGroupBox(self.page_6)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(50, 10, 800, 111))
        self.label_DCL = QLabel(self.groupBox)
        self.label_DCL.setObjectName(u"label_DCL")
        self.label_DCL.setGeometry(QRect(90, 30, 91, 20))
        self.label_ANDCL = QLabel(self.groupBox)
        self.label_ANDCL.setObjectName(u"label_ANDCL")
        self.label_ANDCL.setGeometry(QRect(340, 30, 91, 20))
        self.label_CB = QLabel(self.groupBox)
        self.label_CB.setObjectName(u"label_CB")
        self.label_CB.setGeometry(QRect(580, 30, 91, 20))
        self.lineEdit_DCL = QLineEdit(self.groupBox)
        self.lineEdit_DCL.setObjectName(u"lineEdit_DCL")
        self.lineEdit_DCL.setGeometry(QRect(70, 70, 113, 22))
        self.lineEdit_ANDCL = QLineEdit(self.groupBox)
        self.lineEdit_ANDCL.setObjectName(u"lineEdit_ANDCL")
        self.lineEdit_ANDCL.setGeometry(QRect(320, 70, 113, 22))
        self.lineEdit_CB = QLineEdit(self.groupBox)
        self.lineEdit_CB.setObjectName(u"lineEdit_CB")
        self.lineEdit_CB.setGeometry(QRect(560, 70, 113, 22))
        
        self.groupBox_2 = QGroupBox(self.page_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(70, 130, 400, 161))
        self.checkBox_FRS = QCheckBox(self.groupBox_2)
        self.checkBox_FRS.setObjectName(u"checkBox_FRS")
        self.checkBox_FRS.setGeometry(QRect(40, 30, 91, 20))
        self.checkBox_CB = QCheckBox(self.groupBox_2)
        self.checkBox_CB.setObjectName(u"checkBox_CB")
        self.checkBox_CB.setGeometry(QRect(190, 80, 75, 20))
        self.checkBox_CODE_PAYS = QCheckBox(self.groupBox_2)
        self.checkBox_CODE_PAYS.setObjectName(u"checkBox_CODE_PAYS")
        self.checkBox_CODE_PAYS.setGeometry(QRect(190, 30, 300, 20))
        self.checkBox_REG = QCheckBox(self.groupBox_2)
        self.checkBox_REG.setObjectName(u"checkBox_REG")
        self.checkBox_REG.setGeometry(QRect(40, 80, 81, 20))
        self.checkBox_PROV = QCheckBox(self.groupBox_2)
        self.checkBox_PROV.setObjectName(u"checkBox_PROV")
        self.checkBox_PROV.setGeometry(QRect(40, 120, 75, 20))
        self.checkBox_ANDCL = QCheckBox(self.groupBox_2)
        self.checkBox_ANDCL.setObjectName(u"checkBox_ANDCL")
        self.checkBox_ANDCL.setGeometry(QRect(190, 120, 75, 20))
        
        self.groupBox_3 = QGroupBox(self.page_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(490, 130, 400, 161))
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 40, 100, 20))
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 80, 100, 20))
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 120, 100, 20))
        self.lineEdit_4 = QLineEdit(self.groupBox_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(190, 40, 113, 22))
        self.lineEdit_5 = QLineEdit(self.groupBox_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(190, 80, 113, 22))
        self.lineEdit_6 = QLineEdit(self.groupBox_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(190, 120, 113, 22))
        
        self.pushButtonRech = QPushButton(self.page_6)
        self.pushButtonRech.setObjectName(u"pushButton")
        self.pushButtonRech.setGeometry(QRect(230, 302, 370, 31))
        self.pushButtonRech.clicked.connect(self.Recherche)
        self.scroll_area = QScrollArea(self.page_6)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setGeometry(QRect(80, 350, 850, 250))
        
        self.tableWidgetRech = PyTableWidget(
            radius = 8,
            color = self.themes2["app_color"]["text_foreground"],
            selection_color = self.themes2["app_color"]["context_color"],
            bg_color = self.themes2["app_color"]["bg_two"],
            header_horizontal_color = self.themes2["app_color"]["dark_two"],
            header_vertical_color = self.themes2["app_color"]["bg_three"],
            bottom_line_color = self.themes2["app_color"]["bg_three"],
            grid_line_color = self.themes2["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes2["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes2["app_color"]["dark_four"],
            context_color = self.themes2["app_color"]["context_color"]
        )

        self.tableWidgetRech.setObjectName(u"tableWidgetRech")
        self.tableWidgetRech.setRowCount(40)
        self.tableWidgetRech.setColumnCount(35)
        self.tableWidgetRech.setGeometry(QRect(80, 350, 850, 250))
        self.tableWidgetRech.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidgetRech.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidgetRech.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.scroll_area.setWidget(self.tableWidgetRech)
        
        self.pushButtonRech.clicked.connect(self.Recherche)
  
        self.pages.addWidget(self.page_6) 
 #####################################################
        self.main_pages_layout.addWidget(self.pages)
        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u" Controle de la Valeur en douane ", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
        
        #self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
        self.pushButtonImport.setText(QCoreApplication.translate("MainPages", u" Import file", None))
        self.path.setText(QCoreApplication.translate("MainPages", u" Chemin de votre fichier excel ", None))

        self.pushButtonRe.setText(QCoreApplication.translate("MainPages", u" Oui", None))
        self.label_Result.setText(QCoreApplication.translate("MainPages", u" Resultat de la Prediction", None))
        
        
        self.label_Re.setText(QCoreApplication.translate("MainPages", u" Voulez vous voir le resultat de la prediction", None))
        
        #self.test.setText(QCoreApplication.translate("MainPages", u"    TEST   ", None))
    


       #Recherche 
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Informations de la d\u00e9claration ", None))
        self.label_DCL.setText(QCoreApplication.translate("MainWindow", u"Num DCL", None))
        self.label_ANDCL.setText(QCoreApplication.translate("MainWindow", u"Ann\u00e9e DCL ", None))
        self.label_CB.setText(QCoreApplication.translate("MainWindow", u"Code Bureau", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Rechercher par rapport a : ", None))
        self.checkBox_FRS.setText(QCoreApplication.translate("MainWindow", u"NOM_FRS", None))
        self.checkBox_CB.setText(QCoreApplication.translate("MainWindow", u"CB", None))
        self.checkBox_CODE_PAYS.setText(QCoreApplication.translate("MainWindow", u"CODE_PAYS", None))
        self.checkBox_REG.setText(QCoreApplication.translate("MainWindow", u"CODE_REG", None))
        self.checkBox_PROV.setText(QCoreApplication.translate("MainWindow", u"PAYS_PROV", None))
        self.checkBox_ANDCL.setText(QCoreApplication.translate("MainWindow", u"AN_DCL", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Tapper les mots cl\u00e9s de la d\u00e9scription article  :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"1er mot cl\u00e9 ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"2eme mot cl\u00e9 ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"3eme mot cl\u00e9 ", None))
        self.pushButtonRech.setText(QCoreApplication.translate("MainWindow", u"Lancer la Recherche", None))
   
    # retranslateUi


   
   
    def Recherche(self):
     num_dcl = self.lineEdit_DCL.text()
     print(num_dcl)
     an_dcl = self.lineEdit_ANDCL.text()
     print(an_dcl)
     cb = self.lineEdit_CB.text()  
     print(cb) 
     df = pd.read_excel(r'C:\Users\Administrateur\Downloads\LOG_FINAL.xlsx')
     df.columns =['CB', 'AN_DECL','NUM_DECL', 'CODE_REG','CODE_FISCA','DD','TO','NOM_FRS','PAYS_FRS','ADR_FRS','PAY_PROV','LC_PTFN','NUM_ART','NUM_STAT','CODE_PAYS','DES_ART','PU','QTE_FACT','QTE_COMPL','POIDS','MACHINE','MOULE','INJECT','PLASTIQUE','CAOU','SOUFLAGE','EXTRUD','SOUS-VIDE-THERM','PRESS','MELANG-MALAX','DECOUP-REFONDRE','PU_LC']
     dfT = pd.read_excel(r'C:\Users\Administrateur\Downloads\LOG_FINAL_TEST.xlsx')
     dfT.columns =['CB', 'AN_DECL','NUM_DECL', 'CODE_REG','CODE_FISCA','DD','TO','NOM_FRS','PAYS_FRS','ADR_FRS','PAY_PROV','LC_PTFN','NUM_ART','NUM_STAT','CODE_PAYS','DES_ART','PU','QTE_FACT','QTE_COMPL','POIDS','MACHINE','MOULE','INJECT','PLASTIQUE','CAOU','SOUFLAGE','EXTRUD','SOUS-VIDE-THERM','PRESS','MELANG-MALAX','DECOUP-REFONDRE','PU_LC']
     
     self.tableWidgetRech.setHorizontalHeaderLabels(dfT.columns) 
     dfSimilaire = pd.DataFrame()
       
     for i, row in dfT.iterrows():
          if str(row['NUM_DECL']) == str(num_dcl):
            
              if str(row['AN_DECL']) == str(an_dcl):
            #row_number = self.tableWidgetres.rowCount()
                dfSimilaire = dfSimilaire.append(row)
     print(dfSimilaire)
     count = 0
     dfSimilaire[['PU_LC']]= np.exp(dfSimilaire[['PU_LC']])
     dfSimilaire['PU_LC'] = dfSimilaire['PU_LC'].apply(np.int64)
     dfSimilaire[['POIDS']]= np.exp(dfSimilaire[['POIDS']])
     df[['PU_LC']]= np.exp(df[['PU_LC']])
     df[['POIDS']]= np.exp(df[['POIDS']])
     nom_frs = ''
     code_reg=''
     pay_prov=''   
     code_pays=''

     if  self.checkBox_FRS.isChecked()  : 
               nom_frs = dfSimilaire['NOM_FRS']
               print(nom_frs)
     if  self.checkBox_REG.isChecked()  : 
               code_reg = dfSimilaire['CODE_REG']
               print(code_reg)
     if  self.checkBox_CODE_PAYS.isChecked()  : 
               code_pays = dfSimilaire['CODE_PAYS']
               print(code_pays)
     if  self.checkBox_PROV.isChecked()  : 
               pay_prov = dfSimilaire['PAY_PROV']
               print(pay_prov)
     
     for i2, roow in dfSimilaire.iterrows():
         print("enter here")
         for i3 , roww in df.iterrows():
           print("enter here 2")  
           print(str(roww["NUM_STAT"]))
           print(" AND ")
           print(str(roow["NUM_STAT"]))
           if( roww["NUM_STAT"] == roow["NUM_STAT"])  :
            print(" FOUND NUM stat correct") 
            if self.checkBox_FRS.isChecked() and self.checkBox_PROV.isChecked()  :
                   
             if ( roww['NOM_FRS'] == roow['NOM_FRS']) and (roww['PAY_PROV'] == roow['PAY_PROV']) :
                     
              for indx , vall in enumerate(roww):
                #print("second") 
                self.tableWidgetRech.setItem(count, indx, QTableWidgetItem(str(vall)))
                print(" J'AI saisie ")
              #ind = 0
              count = count + 1  
            if self.checkBox_REG.isChecked()   :  
             if ( roww['CODE_REG'] == roow['CODE_REG']) :
              print("enfin l9it whda")       
              for indx , vall in enumerate(roww):
                #print("second") 
                self.tableWidgetRech.setItem(count, indx, QTableWidgetItem(str(vall)))
                print(" J'AI saisie ")
              #ind = 0
              count = count + 1 
              self.tableWidgetRech.setColumnWidth(indx,600)     


              """
            if self.checkBox_REG.isChecked()  :
             if ( roww['CODE_REG'] == roow['CODE_REG'])  :
              for indx , vall in enumerate(roww):
                #print("second") 
                self.tableWidgetres.setItem(count, indx, QTableWidgetItem(str(vall)))
              #ind = 0
              count = count + 1    
              """




 

         
    def train_func(self):
     
        
        
     #if(self.path!=""):
        #file = QFileDialog.getOpenFileName()
        #self.path.setText(file[0])
        #df = pd.read_excel(self.path.text())
        df=pd.read_excel(r'C:\Users\Administrateur\Downloads\LOG_FINAL.xlsx')
        df.columns =['CB', 'AN_DECL','NUM_DECL', 'CODE_REG','CODE_FISCA','DD','TO','NOM_FRS','PAYS_FRS','ADR_FRS','PAY_PROV','LC_PTFN','NUM_ART','NUM_STAT','CODE_PAYS','DES_ART','PU','QTE_FACT','QTE_COMPL','POIDS','MACHINE','MOULE','INJECT','PLASTIQUE','CAOU','SOUFLAGE','EXTRUD','SOUS-VIDE-THERM','PRESS','MELANG-MALAX','DECOUP-REFONDRE','PU_LC']
        #df[['PU_LC']]= np.log(df[['PU_LC']])
        #data[['POIDS']]= np.log(data[['POIDS']])
        df = df.sample(frac=1).reset_index(drop=True)
        df = df.sample(frac=1).reset_index(drop=True)
        x =df[['CB', 'AN_DECL', 'CODE_REG','TO','PAYS_FRS','PAY_PROV','NUM_STAT','CODE_PAYS','POIDS','MACHINE','MOULE','INJECT','PLASTIQUE','CAOU','SOUFLAGE','EXTRUD','SOUS-VIDE-THERM','PRESS','MELANG-MALAX','DECOUP-REFONDRE']]
        #x = data[[ 'PAYS_FRS','PAY_PROV','POIDS_NET','NUM_STAT','CODE_PAYS','ACCESSOIRES','AIR','ALIMENT','AUTOCLAVE','AUTOMATIQUE','BATTERIE','BETAIL','BOUTEILLE','CAOUCHOUC','CHALEUR','CHALUMEAU','CHARIOT','CHAUSSURES','COMPRESSEUR','COUPEUR','DECAPEUR','EAU','ECHANGEUR','ECHAPPEMNT','ELECTRIQUE','EPANDAGE/PAVAGE/PROFILAGE','ETIQUETEUSE','EXTRUDEUSE','GAZ','GENERATEUR','HACHOIR','HUILE','INJECTION','KIT','LABORATOIRE','LIGNE','MACHINE','MAIN','MEDICAL','MELANGEUR','MOULER','PARTIE','PLASTIQUE','PRESSE','PRODUCTION','REFROIDISSEUR','SOUDEUR','SOUFFLAGE','SOUS VIDE','STERILISATEUR','THERMOFORMEUSE', 'TORCHE','TRONCONNER','VIANDE']]
        y = df['PU_LC']

        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)
        #print(y_test)
        
        gbr = GradientBoostingRegressor()
        gbr.fit(x_train, y_train) 
        clf = GradientBoostingRegressor(loss='quantile', alpha=0.40)
        clf.fit(x_train, y_train)

        
        dfT = pd.read_excel(r'C:\Users\Administrateur\Downloads\LOG_FINAL_TEST.xlsx')
        dfT.columns =['CB', 'AN_DECL','NUM_DECL', 'CODE_REG','CODE_FISCA','DD','TO','NOM_FRS','PAYS_FRS','ADR_FRS','PAY_PROV','LC_PTFN','NUM_ART','NUM_STAT','CODE_PAYS','DES_ART','PU','QTE_FACT','QTE_COMPL','POIDS','MACHINE','MOULE','INJECT','PLASTIQUE','CAOU','SOUFLAGE','EXTRUD','SOUS-VIDE-THERM','PRESS','MELANG-MALAX','DECOUP-REFONDRE','PU_LC']
        
        x_pred = dfT[['CB', 'AN_DECL', 'CODE_REG','TO','PAYS_FRS','PAY_PROV','NUM_STAT','CODE_PAYS','POIDS','MACHINE','MOULE','INJECT','PLASTIQUE','CAOU','SOUFLAGE','EXTRUD','SOUS-VIDE-THERM','PRESS','MELANG-MALAX','DECOUP-REFONDRE']]
        #x = data[[ 'PAYS_FRS','PAY_PROV','POIDS_NET','NUM_STAT','CODE_PAYS','ACCESSOIRES','AIR','ALIMENT','AUTOCLAVE','AUTOMATIQUE','BATTERIE','BETAIL','BOUTEILLE','CAOUCHOUC','CHALEUR','CHALUMEAU','CHARIOT','CHAUSSURES','COMPRESSEUR','COUPEUR','DECAPEUR','EAU','ECHANGEUR','ECHAPPEMNT','ELECTRIQUE','EPANDAGE/PAVAGE/PROFILAGE','ETIQUETEUSE','EXTRUDEUSE','GAZ','GENERATEUR','HACHOIR','HUILE','INJECTION','KIT','LABORATOIRE','LIGNE','MACHINE','MAIN','MEDICAL','MELANGEUR','MOULER','PARTIE','PLASTIQUE','PRESSE','PRODUCTION','REFROIDISSEUR','SOUDEUR','SOUFFLAGE','SOUS VIDE','STERILISATEUR','THERMOFORMEUSE', 'TORCHE','TRONCONNER','VIANDE']]
        y_pred = dfT['PU_LC']
        gbr_pred = gbr.predict(x_pred) 
        print(gbr_pred)
        clf_pred = clf.predict(x_pred)

        dtFinal = pd.DataFrame(dfT[['CB','AN_DECL','NUM_DECL','CODE_REG','NUM_STAT','NOM_FRS']])
        dtFinal[' Valeur déclaré '] = np.exp(y_pred)
        dtFinal[' Valeur déclaré '] = dtFinal[' Valeur déclaré '].apply(np.int64)
        dtFinal[' Valeur minimale prédite ']  = np.exp(clf_pred)
        dtFinal[' Valeur minimale prédite '] = dtFinal[' Valeur minimale prédite '].apply(np.int64)
        dtFinal[' Valeur maximale prédite '] = np.exp(gbr_pred)
        dtFinal[' Valeur maximale prédite '] = dtFinal[' Valeur maximale prédite '].apply(np.int64)
        dtFinal[' Différence maximale '] = dtFinal[' Valeur déclaré '] - dtFinal[' Valeur maximale prédite ']
        dtFinal[' Différence maximale '] = dtFinal[' Différence maximale '].apply(np.int64)
        #dtFinal['Risque'] = str
        
        """"
        self.model2 = QStandardItemModel()
        self.model2.setHorizontalHeaderLabels(dtFinal.columns)
        self.model2.setRowCount(dtFinal.shape[0])
        self.tableView.setModel(self.model2)
        """
        self.table_widgetRes.setHorizontalHeaderLabels(dtFinal.columns) 
        for row in dtFinal.iterrows():
          #L = []
          values = row[1]
          print(values)
          #print(values)
          for col_indx, value in enumerate(values):
            tableItemS = QTableWidgetItem(str(value))
            self.table_widgetRes.setItem(row[0],col_indx,tableItemS)
          self.table_widgetRes.setColumnWidth(col_indx,600)

        
      
        