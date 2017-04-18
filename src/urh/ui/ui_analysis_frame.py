# -*- coding: utf-8 -*-

#
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FAnalysis(object):
    def setupUi(self, FAnalysis):
        FAnalysis.setObjectName("FAnalysis")
        FAnalysis.resize(1098, 839)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FAnalysis.sizePolicy().hasHeightForWidth())
        FAnalysis.setSizePolicy(sizePolicy)
        FAnalysis.setFocusPolicy(QtCore.Qt.ClickFocus)
        FAnalysis.setAcceptDrops(True)
        FAnalysis.setFrameShape(QtWidgets.QFrame.StyledPanel)
        FAnalysis.setFrameShadow(QtWidgets.QFrame.Raised)
        FAnalysis.setLineWidth(1)
        FAnalysis.setMidLineWidth(0)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FAnalysis)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(FAnalysis)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1080, 821))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter = QtWidgets.QSplitter(self.scrollAreaWidgetContents)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.frame_2 = QtWidgets.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_2 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName("splitter_2")
        self.frame_4 = QtWidgets.QFrame(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_4)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.treeViewProtocols = ProtocolTreeView(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeViewProtocols.sizePolicy().hasHeightForWidth())
        self.treeViewProtocols.setSizePolicy(sizePolicy)
        self.treeViewProtocols.setAcceptDrops(True)
        self.treeViewProtocols.setDragEnabled(True)
        self.treeViewProtocols.setDragDropOverwriteMode(False)
        self.treeViewProtocols.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.treeViewProtocols.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.treeViewProtocols.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.treeViewProtocols.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.treeViewProtocols.setAnimated(True)
        self.treeViewProtocols.setObjectName("treeViewProtocols")
        self.treeViewProtocols.header().setVisible(False)
        self.verticalLayout_10.addWidget(self.treeViewProtocols)
        self.btnSaveProto = QtWidgets.QToolButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaveProto.sizePolicy().hasHeightForWidth())
        self.btnSaveProto.setSizePolicy(sizePolicy)
        self.btnSaveProto.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnSaveProto.setBaseSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon.fromTheme("document-save")
        self.btnSaveProto.setIcon(icon)
        self.btnSaveProto.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnSaveProto.setObjectName("btnSaveProto")
        self.verticalLayout_10.addWidget(self.btnSaveProto)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.listViewParticipants = QtWidgets.QListView(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewParticipants.sizePolicy().hasHeightForWidth())
        self.listViewParticipants.setSizePolicy(sizePolicy)
        self.listViewParticipants.setObjectName("listViewParticipants")
        self.verticalLayout_11.addWidget(self.listViewParticipants)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.cbProtoView = QtWidgets.QComboBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbProtoView.sizePolicy().hasHeightForWidth())
        self.cbProtoView.setSizePolicy(sizePolicy)
        self.cbProtoView.setObjectName("cbProtoView")
        self.cbProtoView.addItem("")
        self.cbProtoView.addItem("")
        self.cbProtoView.addItem("")
        self.verticalLayout.addWidget(self.cbProtoView)
        self.cbDecoding = QtWidgets.QComboBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDecoding.sizePolicy().hasHeightForWidth())
        self.cbDecoding.setSizePolicy(sizePolicy)
        self.cbDecoding.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cbDecoding.setObjectName("cbDecoding")
        self.cbDecoding.addItem("")
        self.cbDecoding.addItem("")
        self.cbDecoding.addItem("")
        self.cbDecoding.addItem("")
        self.cbDecoding.addItem("")
        self.verticalLayout.addWidget(self.cbDecoding)
        self.lEncodingErrors = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lEncodingErrors.sizePolicy().hasHeightForWidth())
        self.lEncodingErrors.setSizePolicy(sizePolicy)
        self.lEncodingErrors.setObjectName("lEncodingErrors")
        self.verticalLayout.addWidget(self.lEncodingErrors)
        self.lDecodingErrorsValue = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lDecodingErrorsValue.sizePolicy().hasHeightForWidth())
        self.lDecodingErrorsValue.setSizePolicy(sizePolicy)
        self.lDecodingErrorsValue.setObjectName("lDecodingErrorsValue")
        self.verticalLayout.addWidget(self.lDecodingErrorsValue)
        self.cbShowDiffs = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbShowDiffs.sizePolicy().hasHeightForWidth())
        self.cbShowDiffs.setSizePolicy(sizePolicy)
        self.cbShowDiffs.setObjectName("cbShowDiffs")
        self.verticalLayout.addWidget(self.cbShowDiffs)
        self.chkBoxShowOnlyDiffs = QtWidgets.QCheckBox(self.frame_4)
        self.chkBoxShowOnlyDiffs.setObjectName("chkBoxShowOnlyDiffs")
        self.verticalLayout.addWidget(self.chkBoxShowOnlyDiffs)
        self.chkBoxOnlyShowLabelsInProtocol = QtWidgets.QCheckBox(self.frame_4)
        self.chkBoxOnlyShowLabelsInProtocol.setObjectName("chkBoxOnlyShowLabelsInProtocol")
        self.verticalLayout.addWidget(self.chkBoxOnlyShowLabelsInProtocol)
        self.btnAnalyze = QtWidgets.QToolButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAnalyze.sizePolicy().hasHeightForWidth())
        self.btnAnalyze.setSizePolicy(sizePolicy)
        self.btnAnalyze.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.btnAnalyze.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btnAnalyze.setObjectName("btnAnalyze")
        self.verticalLayout.addWidget(self.btnAnalyze)
        self.stackedWidgetLogicAnalysis = QtWidgets.QStackedWidget(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidgetLogicAnalysis.sizePolicy().hasHeightForWidth())
        self.stackedWidgetLogicAnalysis.setSizePolicy(sizePolicy)
        self.stackedWidgetLogicAnalysis.setObjectName("stackedWidgetLogicAnalysis")
        self.pageButtonAnalyzer = QtWidgets.QWidget()
        self.pageButtonAnalyzer.setObjectName("pageButtonAnalyzer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pageButtonAnalyzer)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidgetLogicAnalysis.addWidget(self.pageButtonAnalyzer)
        self.pageProgressBar = QtWidgets.QWidget()
        self.pageProgressBar.setObjectName("pageProgressBar")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pageProgressBar)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.progressBarLogicAnalyzer = QtWidgets.QProgressBar(self.pageProgressBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBarLogicAnalyzer.sizePolicy().hasHeightForWidth())
        self.progressBarLogicAnalyzer.setSizePolicy(sizePolicy)
        self.progressBarLogicAnalyzer.setProperty("value", 24)
        self.progressBarLogicAnalyzer.setObjectName("progressBarLogicAnalyzer")
        self.verticalLayout_6.addWidget(self.progressBarLogicAnalyzer)
        self.stackedWidgetLogicAnalysis.addWidget(self.pageProgressBar)
        self.verticalLayout.addWidget(self.stackedWidgetLogicAnalysis)
        self.frame_3 = QtWidgets.QFrame(self.splitter_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEditSearch = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSearch.sizePolicy().hasHeightForWidth())
        self.lineEditSearch.setSizePolicy(sizePolicy)
        self.lineEditSearch.setAcceptDrops(False)
        self.lineEditSearch.setClearButtonEnabled(True)
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.gridLayout_2.addWidget(self.lineEditSearch, 0, 0, 1, 1)
        self.btnSearchSelectFilter = QtWidgets.QToolButton(self.frame_3)
        self.btnSearchSelectFilter.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.btnSearchSelectFilter.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.btnSearchSelectFilter.setObjectName("btnSearchSelectFilter")
        self.gridLayout_2.addWidget(self.btnSearchSelectFilter, 0, 1, 1, 1)
        self.lFilterShown = QtWidgets.QLabel(self.frame_3)
        self.lFilterShown.setObjectName("lFilterShown")
        self.gridLayout_2.addWidget(self.lFilterShown, 0, 2, 1, 1)
        self.btnPrevSearch = QtWidgets.QToolButton(self.frame_3)
        self.btnPrevSearch.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPrevSearch.sizePolicy().hasHeightForWidth())
        self.btnPrevSearch.setSizePolicy(sizePolicy)
        self.btnPrevSearch.setMaximumSize(QtCore.QSize(20, 16777215))
        icon = QtGui.QIcon.fromTheme("go-previous")
        self.btnPrevSearch.setIcon(icon)
        self.btnPrevSearch.setObjectName("btnPrevSearch")
        self.gridLayout_2.addWidget(self.btnPrevSearch, 0, 3, 1, 1)
        self.lSearchCurrent = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSearchCurrent.sizePolicy().hasHeightForWidth())
        self.lSearchCurrent.setSizePolicy(sizePolicy)
        self.lSearchCurrent.setStyleSheet("QLabel\n"
"{\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.lSearchCurrent.setObjectName("lSearchCurrent")
        self.gridLayout_2.addWidget(self.lSearchCurrent, 0, 4, 1, 1)
        self.lSlash = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSlash.sizePolicy().hasHeightForWidth())
        self.lSlash.setSizePolicy(sizePolicy)
        self.lSlash.setAlignment(QtCore.Qt.AlignCenter)
        self.lSlash.setObjectName("lSlash")
        self.gridLayout_2.addWidget(self.lSlash, 0, 5, 1, 1)
        self.lSearchTotal = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSearchTotal.sizePolicy().hasHeightForWidth())
        self.lSearchTotal.setSizePolicy(sizePolicy)
        self.lSearchTotal.setStyleSheet("QLabel\n"
"{\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.lSearchTotal.setObjectName("lSearchTotal")
        self.gridLayout_2.addWidget(self.lSearchTotal, 0, 6, 1, 1)
        self.btnNextSearch = QtWidgets.QToolButton(self.frame_3)
        self.btnNextSearch.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNextSearch.sizePolicy().hasHeightForWidth())
        self.btnNextSearch.setSizePolicy(sizePolicy)
        self.btnNextSearch.setMaximumSize(QtCore.QSize(20, 16777215))
        icon = QtGui.QIcon.fromTheme("go-next")
        self.btnNextSearch.setIcon(icon)
        self.btnNextSearch.setObjectName("btnNextSearch")
        self.gridLayout_2.addWidget(self.btnNextSearch, 0, 7, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 8, 1, 1)
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 9, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 10, 1, 1)
        self.lblRSSI = QtWidgets.QLabel(self.frame_3)
        self.lblRSSI.setObjectName("lblRSSI")
        self.gridLayout_2.addWidget(self.lblRSSI, 0, 11, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 0, 12, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 13, 1, 1)
        self.lTime = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lTime.sizePolicy().hasHeightForWidth())
        self.lTime.setSizePolicy(sizePolicy)
        self.lTime.setTextFormat(QtCore.Qt.PlainText)
        self.lTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lTime.setObjectName("lTime")
        self.gridLayout_2.addWidget(self.lTime, 0, 14, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.tblViewProtocol = ProtocolTableView(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblViewProtocol.sizePolicy().hasHeightForWidth())
        self.tblViewProtocol.setSizePolicy(sizePolicy)
        self.tblViewProtocol.setAcceptDrops(True)
        self.tblViewProtocol.setAutoFillBackground(True)
        self.tblViewProtocol.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tblViewProtocol.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tblViewProtocol.setLineWidth(1)
        self.tblViewProtocol.setAutoScroll(True)
        self.tblViewProtocol.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.tblViewProtocol.setAlternatingRowColors(True)
        self.tblViewProtocol.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tblViewProtocol.setTextElideMode(QtCore.Qt.ElideNone)
        self.tblViewProtocol.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tblViewProtocol.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tblViewProtocol.setShowGrid(False)
        self.tblViewProtocol.setGridStyle(QtCore.Qt.NoPen)
        self.tblViewProtocol.setSortingEnabled(False)
        self.tblViewProtocol.setWordWrap(False)
        self.tblViewProtocol.setCornerButtonEnabled(False)
        self.tblViewProtocol.setObjectName("tblViewProtocol")
        self.tblViewProtocol.horizontalHeader().setDefaultSectionSize(40)
        self.verticalLayout_3.addWidget(self.tblViewProtocol)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lBits = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lBits.sizePolicy().hasHeightForWidth())
        self.lBits.setSizePolicy(sizePolicy)
        self.lBits.setMaximumSize(QtCore.QSize(16777215, 15))
        self.lBits.setObjectName("lBits")
        self.horizontalLayout_3.addWidget(self.lBits)
        self.lBitsSelection = QtWidgets.QLineEdit(self.frame_3)
        self.lBitsSelection.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lBitsSelection.setAcceptDrops(False)
        self.lBitsSelection.setReadOnly(True)
        self.lBitsSelection.setObjectName("lBitsSelection")
        self.horizontalLayout_3.addWidget(self.lBitsSelection)
        self.lHex = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lHex.sizePolicy().hasHeightForWidth())
        self.lHex.setSizePolicy(sizePolicy)
        self.lHex.setMaximumSize(QtCore.QSize(16777215, 15))
        self.lHex.setObjectName("lHex")
        self.horizontalLayout_3.addWidget(self.lHex)
        self.lHexSelection = QtWidgets.QLineEdit(self.frame_3)
        self.lHexSelection.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lHexSelection.setAcceptDrops(False)
        self.lHexSelection.setReadOnly(True)
        self.lHexSelection.setObjectName("lHexSelection")
        self.horizontalLayout_3.addWidget(self.lHexSelection)
        self.lDecimal = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lDecimal.sizePolicy().hasHeightForWidth())
        self.lDecimal.setSizePolicy(sizePolicy)
        self.lDecimal.setMaximumSize(QtCore.QSize(16777215, 15))
        self.lDecimal.setObjectName("lDecimal")
        self.horizontalLayout_3.addWidget(self.lDecimal)
        self.lDecimalSelection = QtWidgets.QLineEdit(self.frame_3)
        self.lDecimalSelection.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lDecimalSelection.setAcceptDrops(False)
        self.lDecimalSelection.setReadOnly(True)
        self.lDecimalSelection.setObjectName("lDecimalSelection")
        self.horizontalLayout_3.addWidget(self.lDecimalSelection)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lNumSelectedColumns = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lNumSelectedColumns.sizePolicy().hasHeightForWidth())
        self.lNumSelectedColumns.setSizePolicy(sizePolicy)
        self.lNumSelectedColumns.setObjectName("lNumSelectedColumns")
        self.horizontalLayout_3.addWidget(self.lNumSelectedColumns)
        self.lColumnsSelectedText = QtWidgets.QLabel(self.frame_3)
        self.lColumnsSelectedText.setObjectName("lColumnsSelectedText")
        self.horizontalLayout_3.addWidget(self.lColumnsSelectedText)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.lblLabelValues = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLabelValues.sizePolicy().hasHeightForWidth())
        self.lblLabelValues.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblLabelValues.setFont(font)
        self.lblLabelValues.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLabelValues.setObjectName("lblLabelValues")
        self.gridLayout.addWidget(self.lblLabelValues, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbMessagetypes = QtWidgets.QComboBox(self.frame)
        self.cbMessagetypes.setEditable(True)
        self.cbMessagetypes.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.cbMessagetypes.setObjectName("cbMessagetypes")
        self.horizontalLayout.addWidget(self.cbMessagetypes)
        self.btnMessagetypeSettings = QtWidgets.QToolButton(self.frame)
        icon = QtGui.QIcon.fromTheme("preferences-other")
        self.btnMessagetypeSettings.setIcon(icon)
        self.btnMessagetypeSettings.setObjectName("btnMessagetypeSettings")
        self.horizontalLayout.addWidget(self.btnMessagetypeSettings)
        self.btnAddMessagetype = QtWidgets.QToolButton(self.frame)
        icon = QtGui.QIcon.fromTheme("list-add")
        self.btnAddMessagetype.setIcon(icon)
        self.btnAddMessagetype.setObjectName("btnAddMessagetype")
        self.horizontalLayout.addWidget(self.btnAddMessagetype)
        self.btnRemoveMessagetype = QtWidgets.QToolButton(self.frame)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.btnRemoveMessagetype.setIcon(icon)
        self.btnRemoveMessagetype.setObjectName("btnRemoveMessagetype")
        self.horizontalLayout.addWidget(self.btnRemoveMessagetype)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.listViewLabelNames = ProtocolLabelListView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listViewLabelNames.sizePolicy().hasHeightForWidth())
        self.listViewLabelNames.setSizePolicy(sizePolicy)
        self.listViewLabelNames.setAcceptDrops(False)
        self.listViewLabelNames.setObjectName("listViewLabelNames")
        self.gridLayout.addWidget(self.listViewLabelNames, 2, 0, 1, 1)
        self.tblLabelValues = LabelValueTableView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tblLabelValues.sizePolicy().hasHeightForWidth())
        self.tblLabelValues.setSizePolicy(sizePolicy)
        self.tblLabelValues.setAlternatingRowColors(True)
        self.tblLabelValues.setShowGrid(False)
        self.tblLabelValues.setObjectName("tblLabelValues")
        self.tblLabelValues.horizontalHeader().setVisible(True)
        self.tblLabelValues.horizontalHeader().setCascadingSectionResizes(False)
        self.tblLabelValues.horizontalHeader().setDefaultSectionSize(150)
        self.tblLabelValues.horizontalHeader().setStretchLastSection(True)
        self.tblLabelValues.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tblLabelValues, 1, 1, 2, 1)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.splitter)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(FAnalysis)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidgetLogicAnalysis.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FAnalysis)

    def retranslateUi(self, FAnalysis):
        _translate = QtCore.QCoreApplication.translate
        FAnalysis.setWindowTitle(_translate("FAnalysis", "Frame"))
        self.btnSaveProto.setText(_translate("FAnalysis", "Save current protocol..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("FAnalysis", "Protocols"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("FAnalysis", "Participants"))
        self.cbProtoView.setToolTip(_translate("FAnalysis", "<html><head/><body><p>Set the desired view here.</p></body></html>"))
        self.cbProtoView.setItemText(0, _translate("FAnalysis", "Bits"))
        self.cbProtoView.setItemText(1, _translate("FAnalysis", "Hex"))
        self.cbProtoView.setItemText(2, _translate("FAnalysis", "ASCII"))
        self.cbDecoding.setItemText(0, _translate("FAnalysis", "NRZ"))
        self.cbDecoding.setItemText(1, _translate("FAnalysis", "Manchester"))
        self.cbDecoding.setItemText(2, _translate("FAnalysis", "Manchester II"))
        self.cbDecoding.setItemText(3, _translate("FAnalysis", "Differential Manchester"))
        self.cbDecoding.setItemText(4, _translate("FAnalysis", "..."))
        self.lEncodingErrors.setText(_translate("FAnalysis", "Decoding errors for message:"))
        self.lDecodingErrorsValue.setText(_translate("FAnalysis", "0 (0.00%)"))
        self.cbShowDiffs.setText(_translate("FAnalysis", "Mark diffs in protocol"))
        self.chkBoxShowOnlyDiffs.setText(_translate("FAnalysis", "Show only diffs in protocol"))
        self.chkBoxOnlyShowLabelsInProtocol.setText(_translate("FAnalysis", "Show only labels in protocol"))
        self.btnAnalyze.setText(_translate("FAnalysis", "Analyze"))
        self.lineEditSearch.setPlaceholderText(_translate("FAnalysis", "Search Pattern"))
        self.btnSearchSelectFilter.setText(_translate("FAnalysis", "Search"))
        self.lFilterShown.setText(_translate("FAnalysis", "shown: 42/108"))
        self.btnPrevSearch.setText(_translate("FAnalysis", "<"))
        self.lSearchCurrent.setText(_translate("FAnalysis", "-"))
        self.lSlash.setText(_translate("FAnalysis", "/"))
        self.lSearchTotal.setText(_translate("FAnalysis", "-"))
        self.btnNextSearch.setText(_translate("FAnalysis", ">"))
        self.label_2.setToolTip(_translate("FAnalysis", "<html><head/><body><p>The <span style=\" font-weight:600;\">Received Signal Strength Indicator</span> indicates the average signal power of the current message.</p></body></html>"))
        self.label_2.setText(_translate("FAnalysis", "RSSI:"))
        self.lblRSSI.setToolTip(_translate("FAnalysis", "<html><head/><body><p>The <span style=\" font-weight:600;\">Received Signal Strength Indicator</span> indicates the average signal power of the current message.</p></body></html>"))
        self.lblRSSI.setText(_translate("FAnalysis", "1.04"))
        self.label_3.setToolTip(_translate("FAnalysis", "<html><head/><body><p>The <span style=\" font-weight:600;\">Message Start</span> is the point in time when a protocol message begins. Additionally the relative time (+ ...) from the previous message is shown.</p></body></html>"))
        self.label_3.setText(_translate("FAnalysis", "Timestamp:"))
        self.lTime.setToolTip(_translate("FAnalysis", "<html><head/><body><p>The <span style=\" font-weight:600;\">Message</span><span style=\" font-weight:600;\">Start</span> is the point in time when a protocol message begins. Additionally the relative time (+ ...) from the previous message is shown.</p></body></html>"))
        self.lTime.setText(_translate("FAnalysis", "0 (+0)"))
        self.lBits.setText(_translate("FAnalysis", "Bit:"))
        self.lHex.setText(_translate("FAnalysis", "Hex:"))
        self.lDecimal.setText(_translate("FAnalysis", "Decimal:"))
        self.lNumSelectedColumns.setText(_translate("FAnalysis", "0"))
        self.lColumnsSelectedText.setText(_translate("FAnalysis", "Column(s) selected"))
        self.lblLabelValues.setText(_translate("FAnalysis", "Label values for message"))
        self.btnMessagetypeSettings.setToolTip(_translate("FAnalysis", "Settings for message type"))
        self.btnMessagetypeSettings.setText(_translate("FAnalysis", "..."))
        self.btnAddMessagetype.setToolTip(_translate("FAnalysis", "Add a new message type"))
        self.btnAddMessagetype.setText(_translate("FAnalysis", "..."))
        self.btnRemoveMessagetype.setToolTip(_translate("FAnalysis", "Delete current message type"))
        self.btnRemoveMessagetype.setText(_translate("FAnalysis", "..."))
        self.listViewLabelNames.setToolTip(_translate("FAnalysis", "Manage your estimations for protocol fields here. To add custom field types use Rightclick -> Edit."))
        self.label.setText(_translate("FAnalysis", "Message type:"))

from urh.ui.views.LabelValueTableView import LabelValueTableView
from urh.ui.views.ProtocolLabelListView import ProtocolLabelListView
from urh.ui.views.ProtocolTableView import ProtocolTableView
from urh.ui.views.ProtocolTreeView import ProtocolTreeView
from . import urh_rc
