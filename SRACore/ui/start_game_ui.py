# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_game.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_StartGameWidget(object):
    def setupUi(self, StartGameWidget):
        if not StartGameWidget.objectName():
            StartGameWidget.setObjectName(u"StartGameWidget")
        StartGameWidget.resize(426, 545)
        font = QFont()
        font.setPointSize(13)
        StartGameWidget.setFont(font)
        self.gridLayout_2 = QGridLayout(StartGameWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.frame_1 = QFrame(StartGameWidget)
        self.frame_1.setObjectName(u"frame_1")
        self.frame_1.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.2);")
        self.frame_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_1)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border:none")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label)


        self.gridLayout_2.addWidget(self.frame_1, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(StartGameWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"/* \u7ea4\u7ec6\u73b0\u4ee3\u98ce\u683c\u6eda\u52a8\u6761 */\n"
"QScrollArea {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollArea > QWidget {\n"
"    background-color: #f8f9fa; /* \u5185\u5bb9\u533a\u57df\u80cc\u666f\u8272 */\n"
"}\n"
"\n"
"/* \u6eda\u52a8\u6761\u6574\u4f53\uff08\u66f4\u7ec6\uff09 */\n"
"QScrollBar:vertical {\n"
"    width: 8px; /* \u5782\u76f4\u6eda\u52a8\u6761\u5bbd\u5ea6 */\n"
"    background: transparent; /* \u80cc\u666f\u900f\u660e */\n"
"    margin: 0;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    height: 8px; /* \u6c34\u5e73\u6eda\u52a8\u6761\u9ad8\u5ea6 */\n"
"    background: transparent;\n"
"    margin: 0;\n"
"}\n"
"\n"
"/* \u6ed1\u5757\uff08\u66f4\u7cbe\u81f4\uff09 */\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background: rgba(150, 150, 150, 0.4); /* \u534a\u900f\u660e\u7070\u8272 */\n"
"    border-radius: 4px; /* \u7a0d\u5c0f\u7684\u5706\u89d2 */\n"
"    min-width: 8px; /* \u6700\u5c0f\u5bbd\u5ea6\uff08\u9632\u6b62\u8fc7\u7ec6"
                        "\uff09 */\n"
"    min-height: 8px; /* \u6700\u5c0f\u9ad8\u5ea6\uff08\u9632\u6b62\u8fc7\u7ec6\uff09 */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover, \n"
"QScrollBar::handle:horizontal:hover {\n"
"    background: rgba(120, 120, 120, 0.6); /* \u60ac\u505c\u65f6\u66f4\u6df1 */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed, \n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background: rgba(100, 100, 100, 0.8); /* \u70b9\u51fb\u65f6\u66f4\u6df1 */\n"
"}\n"
"\n"
"/* \u9690\u85cf\u6eda\u52a8\u6761\u6309\u94ae\u548c\u89d2\u843d\u533a\u57df */\n"
"QScrollBar::add-line, QScrollBar::sub-line,\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: none;\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 400, 441))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame2_1 = QFrame(self.scrollAreaWidgetContents)
        self.frame2_1.setObjectName(u"frame2_1")
        self.frame2_1.setStyleSheet(u"border: 1.4px solid gray;  font-size: 16px;\n"
"border-radius: 8px;")
        self.frame2_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame2_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame2_1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label2_1 = QLabel(self.frame2_1)
        self.label2_1.setObjectName(u"label2_1")
        self.label2_1.setStyleSheet(u"border:none")

        self.horizontalLayout_4.addWidget(self.label2_1)

        self.channel_comboBox = QComboBox(self.frame2_1)
        self.channel_comboBox.addItem("")
        self.channel_comboBox.addItem("")
        self.channel_comboBox.setObjectName(u"channel_comboBox")
        self.channel_comboBox.setMinimumSize(QSize(0, 0))
        self.channel_comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    padding: 12px 16px;\n"
"    background-color: #ffffff;\n"
"    color: #333333;\n"
"    font-size: 14px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"    border:none;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(\"resources/ui/down-arrow.png\");\n"
"}\n"
"\n"
"/* \u60ac\u505c\u6548\u679c */\n"
"QComboBox:hover {\n"
"    border-color: #bdbdbd;\n"
"    background-color: #f8f9fa;\n"
"}\n"
" \n"
"/* \u6309\u4e0b\u72b6\u6001 */\n"
"QComboBox:pressed {\n"
"    background-color: #eeeeee;\n"
"    border-color: #adadad;\n"
"}\n"
" \n"
"/* \u4e0b\u62c9\u5217\u8868\u6837\u5f0f */\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 8px;\n"
"    background-color: #ffffff;\n"
"    selection-background-color: #f5f9ff;\n"
"    selection-color: #1976d2;\n"
"    padding: 8px 0;\n"
"    margin-top: 8px;\n"
"    ou"
                        "tline: 0;\n"
"    box-shadow: 0 4px 12px rgba(0,0,0,0.1);\n"
"}\n"
" \n"
"/* \u5217\u8868\u9879\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item {\n"
"    padding: 10px 16px;\n"
"    min-height: 20px;\n"
"    border: none;\n"
"}\n"
" \n"
"/* \u5217\u8868\u9879\u60ac\u505c\u6548\u679c */\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    background-color: #f0f7ff;\n"
"    color: #1976d2;\n"
"}\n"
" \n"
"/* \u9009\u4e2d\u9879\u6837\u5f0f */\n"
"QComboBox QAbstractItemView::item:selected {\n"
"    background-color: #e3f2fd;\n"
"    color: #1976d2;\n"
"    font-weight: 500;\n"
"}\n"
" \n"
"/* \u7981\u7528\u72b6\u6001 */\n"
"QComboBox:disabled {\n"
"    background-color: #f5f5f5;\n"
"    color: #9e9e9e;\n"
"    border-color: #e0e0e0;\n"
"}\n"
" \n"
"/* \u7bad\u5934\u60ac\u505c\u6548\u679c */\n"
"QComboBox::drop-down:hover {\n"
"    background-color: #f5f5f5;\n"
"    border-radius: 4px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.channel_comboBox)


        self.verticalLayout_3.addWidget(self.frame2_1)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border: 1.4px solid gray;\n"
"border-radius:  8px")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.use_launcher_checkbox = QCheckBox(self.frame_3)
        self.use_launcher_checkbox.setObjectName(u"use_launcher_checkbox")
        self.use_launcher_checkbox.setEnabled(False)
        self.use_launcher_checkbox.setMinimumSize(QSize(0, 30))
        self.use_launcher_checkbox.setFont(font)
        self.use_launcher_checkbox.setAutoFillBackground(False)
        self.use_launcher_checkbox.setStyleSheet(u"border: none;")
        self.use_launcher_checkbox.setCheckable(True)
        self.use_launcher_checkbox.setChecked(False)

        self.horizontalLayout_5.addWidget(self.use_launcher_checkbox)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame2_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame2_2.setObjectName(u"frame2_2")
        self.frame2_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 8px")
        self.frame2_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame2_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame2_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.path_label = QLabel(self.frame2_2)
        self.path_label.setObjectName(u"path_label")
        self.path_label.setStyleSheet(u"border:none;")

        self.horizontalLayout_2.addWidget(self.path_label)

        self.path_lineEdit = QLineEdit(self.frame2_2)
        self.path_lineEdit.setObjectName(u"path_lineEdit")
        self.path_lineEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.path_lineEdit)

        self.file_pushButton = QPushButton(self.frame2_2)
        self.file_pushButton.setObjectName(u"file_pushButton")
        self.file_pushButton.setMinimumSize(QSize(0, 30))
        self.file_pushButton.setStyleSheet(u"  QPushButton:hover {ackground-color: #f0f0f0;border-color: #ccc;}")

        self.horizontalLayout_2.addWidget(self.file_pushButton)


        self.verticalLayout_3.addWidget(self.frame2_2)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame2_3 = QFrame(self.frame_2)
        self.frame2_3.setObjectName(u"frame2_3")
        self.frame2_3.setStyleSheet(u"\n"
"border: 1.4px solid black;  font-size: 16px;")
        self.frame2_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame2_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame2_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.auto_login_checkBox = QCheckBox(self.frame2_3)
        self.auto_login_checkBox.setObjectName(u"auto_login_checkBox")
        self.auto_login_checkBox.setStyleSheet(u"QCheckBox{border: none;}\n"
"                                                    QCheckBox:hover {\n"
"                                                    background-color: #f0f0f0;\n"
"                                                    }\n"
"\n"
"                                                    /* \u52fe\u9009\u6846\u60ac\u505c\u65f6\u8fb9\u6846\u53d8\u8272 */\n"
"                                                    QCheckBox::indicator:hover {\n"
"                                                    border-color: #666;\n"
"                                                    }")

        self.gridLayout_3.addWidget(self.auto_login_checkBox, 0, 1, 1, 1)

        self.horizontalSpacer2_3 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer2_3, 0, 2, 1, 1)

        self.password_toggle_button = QPushButton(self.frame2_3)
        self.password_toggle_button.setObjectName(u"password_toggle_button")
        self.password_toggle_button.setMinimumSize(QSize(100, 30))
        self.password_toggle_button.setStyleSheet(u"  QPushButton:hover {ackground-color: #f0f0f0;border-color: #ccc;}")

        self.gridLayout_3.addWidget(self.password_toggle_button, 0, 3, 1, 1)

        self.label_2 = QLabel(self.frame2_3)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        self.label_2.setFont(font1)
        self.label_2.setWordWrap(True)

        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 3)

        self.always_logout_checkBox = QCheckBox(self.frame2_3)
        self.always_logout_checkBox.setObjectName(u"always_logout_checkBox")
        self.always_logout_checkBox.setStyleSheet(u"QCheckBox{border: none;}\n"
"                                                    QCheckBox:hover {\n"
"                                                    background-color: #f0f0f0;\n"
"                                                    }\n"
"\n"
"                                                    /* \u52fe\u9009\u6846\u60ac\u505c\u65f6\u8fb9\u6846\u53d8\u8272 */\n"
"                                                    QCheckBox::indicator:hover {\n"
"                                                    border-color: #666;\n"
"                                                    }")

        self.gridLayout_3.addWidget(self.always_logout_checkBox, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame2_3)

        self.frame2_4 = QFrame(self.frame_2)
        self.frame2_4.setObjectName(u"frame2_4")
        self.frame2_4.setStyleSheet(u"\n"
"border: 1.4px solid black;  font-size: 16px;")
        self.frame2_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame2_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame2_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label2_4_11 = QLabel(self.frame2_4)
        self.label2_4_11.setObjectName(u"label2_4_11")
        self.label2_4_11.setStyleSheet(u"border:none")

        self.gridLayout.addWidget(self.label2_4_11, 0, 0, 1, 1)

        self.password_lineEdit = QLineEdit(self.frame2_4)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setMinimumSize(QSize(0, 30))
        self.password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.password_lineEdit, 1, 1, 1, 1)

        self.label2_4_21 = QLabel(self.frame2_4)
        self.label2_4_21.setObjectName(u"label2_4_21")
        self.label2_4_21.setStyleSheet(u"border:none")

        self.gridLayout.addWidget(self.label2_4_21, 1, 0, 1, 1)

        self.account_lineEdit = QLineEdit(self.frame2_4)
        self.account_lineEdit.setObjectName(u"account_lineEdit")
        self.account_lineEdit.setMinimumSize(QSize(0, 30))

        self.gridLayout.addWidget(self.account_lineEdit, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame2_4)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.retranslateUi(StartGameWidget)

        QMetaObject.connectSlotsByName(StartGameWidget)
    # setupUi

    def retranslateUi(self, StartGameWidget):
        StartGameWidget.setWindowTitle(QCoreApplication.translate("StartGameWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("StartGameWidget", u"\u542f\u52a8\u6e38\u620f", None))
        self.label2_1.setText(QCoreApplication.translate("StartGameWidget", u"\u6e20\u9053: ", None))
        self.channel_comboBox.setItemText(0, QCoreApplication.translate("StartGameWidget", u"\u5b98\u670d", None))
        self.channel_comboBox.setItemText(1, QCoreApplication.translate("StartGameWidget", u"bilibili", None))

#if QT_CONFIG(tooltip)
        self.use_launcher_checkbox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.use_launcher_checkbox.setText(QCoreApplication.translate("StartGameWidget", u"\u4f7f\u7528\u542f\u52a8\u5668", None))
        self.path_label.setText(QCoreApplication.translate("StartGameWidget", u"\u6e38\u620f\u8def\u5f84\uff1a", None))
        self.file_pushButton.setText(QCoreApplication.translate("StartGameWidget", u"\u6d4f\u89c8", None))
        self.auto_login_checkBox.setText(QCoreApplication.translate("StartGameWidget", u"\u81ea\u52a8\u767b\u5f55", None))
        self.password_toggle_button.setText(QCoreApplication.translate("StartGameWidget", u"\u663e\u793a\u5bc6\u7801", None))
        self.label_2.setText(QCoreApplication.translate("StartGameWidget", u"\u52fe\u9009\u81ea\u52a8\u767b\u5f55\u8868\u660e\u60a8\u5df2\u9605\u8bfb\u5e76\u540c\u610f\u300a\u7528\u6237\u534f\u8bae\u300b\u548c\u300a\u9690\u79c1\u653f\u7b56\u300b", None))
#if QT_CONFIG(whatsthis)
        self.always_logout_checkBox.setWhatsThis(QCoreApplication.translate("StartGameWidget", u"\u5982\u679c\u542f\u7528\uff0c\u767b\u5f55\u65f6\u4f1a\u767b\u51fa\u5df2\u7ecf\u767b\u5f55\u7684\u8d26\u53f7\u91cd\u65b0\u767b\u5f55\n"
"                                                                ", None))
#endif // QT_CONFIG(whatsthis)
        self.always_logout_checkBox.setText(QCoreApplication.translate("StartGameWidget", u"\u603b\u662f\u91cd\u65b0\u767b\u5f55", None))
        self.label2_4_11.setText(QCoreApplication.translate("StartGameWidget", u"\u8d26\u53f7\uff1a", None))
        self.label2_4_21.setText(QCoreApplication.translate("StartGameWidget", u"\u5bc6\u7801\uff1a", None))
    # retranslateUi

