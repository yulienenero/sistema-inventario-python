# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nievesRjsMwc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(964, 593)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"*{border: none;\n"
"background-color: transparent;\n"
"}\n"
"#centralWingets{\n"
"background-color: #040f13;\n"
"}\n"
"#side_menu{\n"
"background-color: #071e26;\n"
"\n"
"}\n"
"QPushButton{\n"
"padding:2px;\n"
"background-color: #040f13;\n"
"\n"
"}\n"
"#main_body{\n"
"background-color: #071e26;\n"
";\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background-color: rgb(193, 250, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        self.pushButton.setStyleSheet(u"image: url(:/prefijoNuevo/imagenes/11011666.png);")

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.pushButton_9 = QPushButton(self.frame_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 0, 71, 41))
        self.pushButton_9.setStyleSheet(u"image: url(:/prefijoNuevo/imagenes/Imagen1.png);")
        self.usuario_l = QLabel(self.frame_6)
        self.usuario_l.setObjectName(u"usuario_l")
        self.usuario_l.setGeometry(QRect(100, 10, 91, 21))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.usuario_l.setFont(font)
        self.fecha_l = QLabel(self.frame_6)
        self.fecha_l.setObjectName(u"fecha_l")
        self.fecha_l.setGeometry(QRect(720, 10, 151, 31))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.fecha_l.setFont(font1)
        self.prueba = QLabel(self.frame_6)
        self.prueba.setObjectName(u"prueba")
        self.prueba.setGeometry(QRect(580, 20, 0, 16))
        self.prueba.setMaximumSize(QSize(0, 16777215))
        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(610, 10, 75, 24))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(165, 222, 183);")

        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"background-color: rgb(208, 236, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(0, 16777215))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(251, 142, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(202, 202, 255);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(150, 0))
        self.frame_7.setMaximumSize(QSize(150, 16777215))
        self.frame_7.setStyleSheet(u"QPushButton{\n"
"padding: 5px 10px;\n"
"border: none;\n"
"border-radius: 10px;\n"
"background-color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_3 = QPushButton(self.frame_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        self.pushButton_3.setStyleSheet(u"image: url(:/prefijoNuevo/imagenes/descarga (1).png);\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 40))
        self.pushButton_4.setStyleSheet(u"image: url(:/menu/imagenes/images.png);\n"
"image: url(:/prefijoNuevo/imagenes/images.png);")
        self.pushButton_4.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 40))
        self.pushButton_5.setStyleSheet(u"image: url(:/menu/imagenes/gratis-png-caja-registradora-iconos-iconos-dinero-punto-de-venta-pago-caja-registradora.png);\n"
"image: url(:/prefijoNuevo/imagenes/gratis-png-caja-registradora-iconos-iconos-dinero-punto-de-venta-pago-caja-registradora.png);")

        self.verticalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_2.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_10 = QPushButton(self.frame_12)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"image:url(:/menu/imagenes/png-transparent-logo-house-home-building-computer-icons-house-angle-building-text.png);\n"
"image: url(:/prefijoNuevo/imagenes/png-transparent-logo-house-home-building-computer-icons-house-angle-building-text.png);\n"
"border-radius:15px;\n"
"")

        self.verticalLayout_6.addWidget(self.pushButton_10, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.frame_12, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 244, 235);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_13 = QFrame(self.page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"QpushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_20 = QFrame(self.frame_13)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(229, 197, 255);\n"
"    border-radius: 20px;\n"
"\n"
"}\n"
"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.bt_chica = QPushButton(self.frame_20)
        self.bt_chica.setObjectName(u"bt_chica")
        self.bt_chica.setMinimumSize(QSize(40, 160))
        self.bt_chica.setStyleSheet(u"image: url(:/prefijoNuevo/imagenes/1.png);")

        self.horizontalLayout_9.addWidget(self.bt_chica)

        self.bt_media = QPushButton(self.frame_20)
        self.bt_media.setObjectName(u"bt_media")
        self.bt_media.setMinimumSize(QSize(40, 140))
        self.bt_media.setStyleSheet(u"image: url(:/prefijoNuevo/imagenes/2.png);")

        self.horizontalLayout_9.addWidget(self.bt_media)

        self.bt_grande = QPushButton(self.frame_20)
        self.bt_grande.setObjectName(u"bt_grande")
        self.bt_grande.setMinimumSize(QSize(40, 140))
        self.bt_grande.setStyleSheet(u"image: url(:/prefijoNuevo/imagenes/3.png);")

        self.horizontalLayout_9.addWidget(self.bt_grande)

        self.bt_mediol = QPushButton(self.frame_20)
        self.bt_mediol.setObjectName(u"bt_mediol")
        self.bt_mediol.setMinimumSize(QSize(40, 140))
        self.bt_mediol.setStyleSheet(u"image: url(:/prefijoNuevo/imagenes/4.png);")

        self.horizontalLayout_9.addWidget(self.bt_mediol)

        self.bt_cono = QPushButton(self.frame_20)
        self.bt_cono.setObjectName(u"bt_cono")
        self.bt_cono.setMinimumSize(QSize(40, 120))
        self.bt_cono.setStyleSheet(u"image: url(:/prefijoNuevo/imagenes/descarga (2).jpg);")

        self.horizontalLayout_9.addWidget(self.bt_cono)


        self.verticalLayout_10.addWidget(self.frame_20)


        self.verticalLayout_7.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_14)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(229, 197, 255);\n"
"    border-radius: 20px;\n"
"\n"
"}\n"
"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.bt_fresa = QPushButton(self.frame_21)
        self.bt_fresa.setObjectName(u"bt_fresa")
        self.bt_fresa.setMinimumSize(QSize(40, 110))
        self.bt_fresa.setStyleSheet(u"\n"
"image: url(:/prefijoNuevo/imagenes/Imagen4.png);")

        self.horizontalLayout_10.addWidget(self.bt_fresa)

        self.bt_chocolate = QPushButton(self.frame_21)
        self.bt_chocolate.setObjectName(u"bt_chocolate")
        self.bt_chocolate.setMinimumSize(QSize(40, 110))
        self.bt_chocolate.setStyleSheet(u"image: url(:/prefijoNuevo/imagenes/Imagen5.png);")

        self.horizontalLayout_10.addWidget(self.bt_chocolate)

        self.bt_cafe = QPushButton(self.frame_21)
        self.bt_cafe.setObjectName(u"bt_cafe")
        self.bt_cafe.setMinimumSize(QSize(0, 110))
        self.bt_cafe.setStyleSheet(u"image: url(:/prefijoNuevo/imagenes/Imagen6.png);")

        self.horizontalLayout_10.addWidget(self.bt_cafe)

        self.bt_pstache = QPushButton(self.frame_21)
        self.bt_pstache.setObjectName(u"bt_pstache")
        self.bt_pstache.setMinimumSize(QSize(0, 110))
        self.bt_pstache.setStyleSheet(u"image: url(:/prefijoNuevo/imagenes/Imagen3.png);")

        self.horizontalLayout_10.addWidget(self.bt_pstache)

        self.bt_franbuesa = QPushButton(self.frame_21)
        self.bt_franbuesa.setObjectName(u"bt_franbuesa")
        self.bt_franbuesa.setMinimumSize(QSize(0, 110))
        self.bt_franbuesa.setStyleSheet(u"image: url(:/prefijoNuevo/imagenes/Imagen7.png);")

        self.horizontalLayout_10.addWidget(self.bt_franbuesa)


        self.horizontalLayout_11.addWidget(self.frame_21)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"padding: 5px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_18)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_16)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_19 = QFrame(self.frame_16)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_19)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget = QWidget(self.frame_19)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_9.addWidget(self.widget)


        self.verticalLayout_8.addWidget(self.frame_19)


        self.horizontalLayout_8.addWidget(self.frame_16)

        self.label_9 = QLabel(self.frame_18)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_9.setFont(font2)
        self.label_9.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.l_sabores = QLabel(self.frame_18)
        self.l_sabores.setObjectName(u"l_sabores")

        self.horizontalLayout_8.addWidget(self.l_sabores)

        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_10)

        self.l_tamayo = QLabel(self.frame_18)
        self.l_tamayo.setObjectName(u"l_tamayo")

        self.horizontalLayout_8.addWidget(self.l_tamayo)

        self.label_2 = QLabel(self.frame_18)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        self.label_2.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.comboBox_3 = QComboBox(self.frame_18)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_8.addWidget(self.comboBox_3)

        self.frame_17 = QFrame(self.frame_18)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy3)
        self.frame_17.setMinimumSize(QSize(0, 100))
        self.frame_17.setMaximumSize(QSize(16777215, 100))
        self.frame_17.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 243, 243);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton{\n"
"border-radius: 15px;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bt_Cancel = QPushButton(self.frame_17)
        self.bt_Cancel.setObjectName(u"bt_Cancel")
        self.bt_Cancel.setMinimumSize(QSize(50, 50))
        self.bt_Cancel.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius:20px;")

        self.horizontalLayout_6.addWidget(self.bt_Cancel)

        self.bt_AN = QPushButton(self.frame_17)
        self.bt_AN.setObjectName(u"bt_AN")
        self.bt_AN.setMaximumSize(QSize(16777215, 50))
        self.bt_AN.setStyleSheet(u"background-color: rgb(0, 170, 127);")

        self.horizontalLayout_6.addWidget(self.bt_AN)


        self.horizontalLayout_8.addWidget(self.frame_17)


        self.horizontalLayout_7.addWidget(self.frame_18)


        self.verticalLayout_7.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_11 = QVBoxLayout(self.page_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_22 = QFrame(self.page_3)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_22)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 6, -1, -1)
        self.frame_26 = QFrame(self.frame_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lineEdit_4 = QLineEdit(self.frame_27)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(167, 171, 162);")

        self.horizontalLayout_15.addWidget(self.lineEdit_4)

        self.l_np = QLabel(self.frame_27)
        self.l_np.setObjectName(u"l_np")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.l_np.setFont(font4)

        self.horizontalLayout_15.addWidget(self.l_np)

        self.lineEdit = QLineEdit(self.frame_27)
        self.lineEdit.setObjectName(u"lineEdit")
        font5 = QFont()
        font5.setPointSize(10)
        self.lineEdit.setFont(font5)

        self.horizontalLayout_15.addWidget(self.lineEdit)


        self.horizontalLayout_14.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.l_pp = QLabel(self.frame_28)
        self.l_pp.setObjectName(u"l_pp")
        self.l_pp.setFont(font4)

        self.horizontalLayout_16.addWidget(self.l_pp)

        self.lineEdit_2 = QLineEdit(self.frame_28)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font5)

        self.horizontalLayout_16.addWidget(self.lineEdit_2)

        self.l_Descripcion = QLabel(self.frame_28)
        self.l_Descripcion.setObjectName(u"l_Descripcion")
        self.l_Descripcion.setFont(font4)

        self.horizontalLayout_16.addWidget(self.l_Descripcion)

        self.lineEdit_3 = QLineEdit(self.frame_28)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font5)

        self.horizontalLayout_16.addWidget(self.lineEdit_3)

        self.comboBox_2 = QComboBox(self.frame_28)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_16.addWidget(self.comboBox_2)


        self.horizontalLayout_14.addWidget(self.frame_28)

        self.frame_28.raise_()
        self.frame_27.raise_()

        self.verticalLayout_12.addWidget(self.frame_26, 0, Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.frame_22, 0, Qt.AlignTop)

        self.frame_23 = QFrame(self.page_3)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_23)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tabla_productos = QTableWidget(self.frame_23)
        if (self.tabla_productos.columnCount() < 7):
            self.tabla_productos.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_productos.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_productos.setObjectName(u"tabla_productos")

        self.verticalLayout_15.addWidget(self.tabla_productos)


        self.verticalLayout_11.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.page_3)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"	background-color: rgb(233, 207, 255);\n"
"}\n"
"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.bt_eliminar = QPushButton(self.frame_25)
        self.bt_eliminar.setObjectName(u"bt_eliminar")
        self.bt_eliminar.setMinimumSize(QSize(150, 30))
        self.bt_eliminar.setStyleSheet(u"background-color: rgb(196, 195, 193);\n"
"")

        self.horizontalLayout_13.addWidget(self.bt_eliminar)

        self.bt_agregar = QPushButton(self.frame_25)
        self.bt_agregar.setObjectName(u"bt_agregar")
        self.bt_agregar.setMinimumSize(QSize(150, 30))
        self.bt_agregar.setStyleSheet(u"background-color: rgb(243, 242, 239);")

        self.horizontalLayout_13.addWidget(self.bt_agregar)


        self.horizontalLayout_12.addWidget(self.frame_25, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_24)

        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_13 = QVBoxLayout(self.page_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_29 = QFrame(self.page_2)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_29)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_15 = QLabel(self.frame_29)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout_14.addWidget(self.label_15)

        self.label = QLabel(self.frame_29)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 29))

        self.verticalLayout_14.addWidget(self.label)

        self.label_7 = QLabel(self.frame_29)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 0))

        self.verticalLayout_14.addWidget(self.label_7)

        self.tabla_venta = QTableWidget(self.frame_29)
        if (self.tabla_venta.columnCount() < 6):
            self.tabla_venta.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_venta.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        self.tabla_venta.setObjectName(u"tabla_venta")

        self.verticalLayout_14.addWidget(self.tabla_venta)


        self.verticalLayout_13.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.page_2)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: rgb(177, 177, 179);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"	background-color: rgb(233, 207, 255);\n"
"}\n"
"")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.borrar_ultimo = QFrame(self.frame_30)
        self.borrar_ultimo.setObjectName(u"borrar_ultimo")
        self.borrar_ultimo.setFrameShape(QFrame.StyledPanel)
        self.borrar_ultimo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.borrar_ultimo)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.borrar_todo = QPushButton(self.borrar_ultimo)
        self.borrar_todo.setObjectName(u"borrar_todo")
        self.borrar_todo.setMaximumSize(QSize(16777215, 90))
        self.borrar_todo.setFont(font2)

        self.horizontalLayout_19.addWidget(self.borrar_todo)

        self.borrar_ultimo_2 = QPushButton(self.borrar_ultimo)
        self.borrar_ultimo_2.setObjectName(u"borrar_ultimo_2")
        self.borrar_ultimo_2.setMaximumSize(QSize(16777215, 70))
        self.borrar_ultimo_2.setFont(font2)

        self.horizontalLayout_19.addWidget(self.borrar_ultimo_2)


        self.horizontalLayout_18.addWidget(self.borrar_ultimo)


        self.verticalLayout_13.addWidget(self.frame_30)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_8)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMinimumSize(QSize(180, 0))
        self.frame_4.setMaximumSize(QSize(180, 16777215))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color: rgb(229, 225, 255);\n"
"border-radius: 10px\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame{\n"
"border-radius: 25px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 10, 81, 21))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 100, 61, 16))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 290, 91, 41))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 200, 151, 41))
        self.label_6.setFont(font4)
        self.comboBox = QComboBox(self.frame_11)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 130, 131, 21))
        self.lorencio = QLabel(self.frame_11)
        self.lorencio.setObjectName(u"lorencio")
        self.lorencio.setGeometry(QRect(40, 340, 49, 16))
        self.cantidad_l = QLabel(self.frame_11)
        self.cantidad_l.setObjectName(u"cantidad_l")
        self.cantidad_l.setGeometry(QRect(40, 260, 49, 16))
        self.codigoV = QLineEdit(self.frame_11)
        self.codigoV.setObjectName(u"codigoV")
        self.codigoV.setGeometry(QRect(0, 60, 113, 21))
        self.label_8 = QLabel(self.frame_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 40, 49, 16))

        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy3.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy3)
        self.frame_10.setMinimumSize(QSize(0, 100))
        self.frame_10.setMaximumSize(QSize(16777215, 100))
        self.frame_10.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 243, 243);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton{\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius: 15px;\n"
"	background-color: rgb(255, 56, 21);\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cancelar_compra = QPushButton(self.frame_10)
        self.cancelar_compra.setObjectName(u"cancelar_compra")
        self.cancelar_compra.setMaximumSize(QSize(16777215, 50))
        self.cancelar_compra.setFont(font1)

        self.horizontalLayout_4.addWidget(self.cancelar_compra)

        self.Pagar = QPushButton(self.frame_10)
        self.Pagar.setObjectName(u"Pagar")
        self.Pagar.setMaximumSize(QSize(16777215, 50))
        self.Pagar.setFont(font1)

        self.horizontalLayout_4.addWidget(self.Pagar)


        self.verticalLayout_5.addWidget(self.frame_10)


        self.verticalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.pushButton_9.setText("")
        self.usuario_l.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.fecha_l.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.prueba.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"nueva  venta", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_10.setText("")
        self.bt_chica.setText("")
        self.bt_media.setText("")
        self.bt_grande.setText("")
        self.bt_mediol.setText("")
        self.bt_cono.setText(QCoreApplication.translate("MainWindow", u"Cono", None))
        self.bt_fresa.setText("")
        self.bt_chocolate.setText("")
        self.bt_cafe.setText("")
        self.bt_pstache.setText("")
        self.bt_franbuesa.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Sabores: ", None))
        self.l_sabores.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None))
        self.l_tamayo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_3.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.bt_Cancel.setText(QCoreApplication.translate("MainWindow", u"Otra", None))
        self.bt_AN.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.l_np.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.l_pp.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.l_Descripcion.setText(QCoreApplication.translate("MainWindow", u"precio", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        ___qtablewidgetitem = self.tabla_productos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tabla_productos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem2 = self.tabla_productos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem3 = self.tabla_productos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        ___qtablewidgetitem4 = self.tabla_productos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem5 = self.tabla_productos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem6 = self.tabla_productos.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None));
        self.bt_eliminar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.bt_agregar.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Lista de productos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtablewidgetitem7 = self.tabla_venta.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem8 = self.tabla_venta.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem9 = self.tabla_venta.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem10 = self.tabla_venta.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        ___qtablewidgetitem11 = self.tabla_venta.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem12 = self.tabla_venta.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        self.borrar_todo.setText(QCoreApplication.translate("MainWindow", u"borrar todo", None))
        self.borrar_ultimo_2.setText(QCoreApplication.translate("MainWindow", u"borrar Seleccionado", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Cuenta", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"precio total:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"cantidad de productos:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Julian", None))

        self.lorencio.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.cantidad_l.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.codigoV.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"folio", None))
        self.cancelar_compra.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.Pagar.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
    # retranslateUi

