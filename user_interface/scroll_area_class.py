from PySide2.QtWidgets import QScrollArea, QTextEdit, QSizePolicy
from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QFont

class ScrollAreaClass(QScrollArea):
    def __init__(self, parent):
        super().__init__()
        self.margin = 100
        self.marginRatio = .8
        self.messages = []


        # container = QtWidgets.QWidget()
        # self.setWidget(container)
        # self.setWidgetResizable(True)
        #
        # layout = QtWidgets.QVBoxLayout(container)
        # layout.addStretch()
        # self.resize(480, 360)

    def resizeEvent(self, event):
        sb = self.verticalScrollBar()
        atMaximum = sb.value() == sb.maximum()
        maxWidth = max(self.width() * self.marginRatio,
            self.width() - self.margin) - sb.sizeHint().width()
        for message in self.messages:
            message.setMaximumWidth(maxWidth)
        super().resizeEvent(event)
        if atMaximum:
            sb.setValue(sb.maximum())

class WrapLabel(QTextEdit):
    def __init__(self, text=''):
        super().__init__()
        self.setText(text)
        self.setReadOnly(True)
        font_for_msg = QFont()
        font_for_msg.setFamily(u"Segoe UI")
        font_for_msg.setPointSize(12)
        self.setFont(font_for_msg)

        # self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        # self.shadow.setBlurRadius(5)
        # self.shadow.setXOffset(0)
        # self.shadow.setYOffset(0)
        # self.shadow.setColor(QtGui.QColor(37, 37, 37))
        # self.setGraphicsEffect(self.shadow)

        self.setAlignment(Qt.AlignLeft)
        self.document().setDocumentMargin(13)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textChanged.connect(self.updateGeometry)
    def minimumSizeHint(self):
        margin = self.frameWidth() * 2
        doc = self.document().clone()
        doc.setTextWidth(self.maximumWidth())
        idealWidth = doc.idealWidth()
        idealHeight = doc.size().height()
        doc.setTextWidth(self.viewport().width())
        if doc.size().height() == idealHeight:
            idealWidth = doc.idealWidth()
        return QSize(
            max(34, idealWidth + margin), doc.size().height() + margin)

    def sizeHint(self):
        return self.minimumSizeHint()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updateGeometry()




