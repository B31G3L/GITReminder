"""
    Copyright 2019 Christian Beigelbeck.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import logging
from conf_reader.reader import ConfReader
from src.service.MainService import MainService
from src.service.ConfigService import ConfigService

if __name__ == "__main__":
    
    ConfReader('assets/GITPuRe.ini')
    log_filename = ConfReader.get('Log', 'Filename') 
    logger = logging.getLogger('GITReminder')
    hdlr = logging.FileHandler(log_filename, mode='w')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.DEBUG)
    
    

    # 1 ini MainService
    logger.info(' 1 INI MainService')
    mainService = MainService(logger)
    
    # 2 Erstelle Config File wenn nicht vorhanden
    logger.info(' 2 INI Config File')
    configService = ConfigService(logger)
    configService.initConf()

    # 3 Start VCS REMINDER
    logger.info(' 3 Start Git Push Reminder')   
    mainService.start() 
  