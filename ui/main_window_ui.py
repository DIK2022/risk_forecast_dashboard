# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QStatusBar,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_programm = QAction(MainWindow)
        self.action_programm.setObjectName(u"action_programm")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabData = QWidget()
        self.tabData.setObjectName(u"tabData")
        self.verticalLayout_2 = QVBoxLayout(self.tabData)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.data_view = QTableView(self.tabData)
        self.data_view.setObjectName(u"data_view")

        self.verticalLayout_2.addWidget(self.data_view)

        self.btn_load = QPushButton(self.tabData)
        self.btn_load.setObjectName(u"btn_load")

        self.verticalLayout_2.addWidget(self.btn_load)

        self.tabWidget.addTab(self.tabData, "")
        self.tabGraphic = QWidget()
        self.tabGraphic.setObjectName(u"tabGraphic")
        self.horizontalLayout = QHBoxLayout(self.tabGraphic)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graph_container = QWidget(self.tabGraphic)
        self.graph_container.setObjectName(u"graph_container")

        self.horizontalLayout.addWidget(self.graph_container)

        self.tabWidget.addTab(self.tabGraphic, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.combo_method = QComboBox(self.tab)
        self.combo_method.addItem("")
        self.combo_method.addItem("")
        self.combo_method.setObjectName(u"combo_method")

        self.verticalLayout_3.addWidget(self.combo_method)

        self.spin_horizon = QSpinBox(self.tab)
        self.spin_horizon.setObjectName(u"spin_horizon")

        self.verticalLayout_3.addWidget(self.spin_horizon)

        self.slider_alpha = QSlider(self.tab)
        self.slider_alpha.setObjectName(u"slider_alpha")
        self.slider_alpha.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_3.addWidget(self.slider_alpha)

        self.spin_window = QSpinBox(self.tab)
        self.spin_window.setObjectName(u"spin_window")

        self.verticalLayout_3.addWidget(self.spin_window)

        self.btn_calc = QPushButton(self.tab)
        self.btn_calc.setObjectName(u"btn_calc")

        self.verticalLayout_3.addWidget(self.btn_calc)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_exit)
        self.menu_2.addAction(self.action_programm)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.action_programm.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.btn_load.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c CSV", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabData), QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGraphic), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a", None))
        self.combo_method.setItemText(0, QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0435 \u0441\u0433\u043b\u0430\u0436\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.combo_method.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041b\u0438\u043d\u0435\u0439\u043d\u0430\u044f \u0440\u0435\u0433\u0440\u0435\u0441\u0441\u0438\u044f", None))

        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"3D", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u043e\u0449\u044c", None))
    # retranslateUi

