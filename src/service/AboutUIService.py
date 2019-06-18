import logging

from PySide2 import QtWidgets, QtCore, QtGui
from conf_reader.reader import ConfReader

from src.gui.settingsUI import Ui_Dialog

class AboutUIService(QtWidgets.QDialog, Ui_Dialog):
    
    def __init__(self, logger, parent = None):
        super(AboutUIService, self).__init__(parent)
        
        ConfReader('VCSR_INI.ini')
        name = ConfReader.get('MetaInformations', 'Name') 
        icon = ConfReader.get('Icons', 'success') 

        logger.debug('Run: init')
        self.setupUi(self)
        self.setWindowTitle(name)
        self.setWindowIcon(QtGui.QIcon(icon))
        self.setFixedSize(400,300)

        
        
        
    