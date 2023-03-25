"""
1. Сборка в .exe (без консоли)
2. Подготовить скрипты для сборки, восстановления
3. Настройки хранятся в json / sql lite (import/export)
4. Основные данные хранятся в postgres
5. Threading / asyncio
6. tray
7. debugging
8. авторизация/аутентификация
9. веб запросы
10. обработка данных в отдельном процессе
"""
import json
import threading
import time
import asyncio
from typing import List

import cv2
from cv2 import *
from numpy import *

import aiohttp
import os
from PyQt6 import uic
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu, QMainWindow, QTextEdit, QPushButton, \
    QInputDialog, QLabel
import sys
from PyQt6 import QtCore, QtWidgets, QtGui


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAction = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


class Ui2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui2, self).__init__()
        uic.loadUi('uic.ui', self)

        self.pushButtonExport = self.findChild(QtWidgets.QPushButton, 'pushButtonExport')
        self.pushButtonExport.clicked.connect(self.export_settings)

        self.pushButtonImport.clicked.connect(self.import_settings)

        self.pushButtonDownload = self.findChild(QtWidgets.QPushButton, 'pushButtonDownload')
        self.pushButtonDownload.clicked.connect(self.download_images)

        self.pushButtonWebcam = self.findChild(QtWidgets.QPushButton, 'pushButtonWebcam')
        self.pushButtonWebcam.clicked.connect(self.webcam)

        self.show()

    async def download_image(self, session: aiohttp.ClientSession, url: str, filename: str):
        async with session.get(url) as response:
            with open(filename, 'wb') as f:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f.write(chunk)

    async def download_images_async(self, urls: List[str]):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i, url in enumerate(urls):
                filename = f"temp/image{i}.jpg"
                task = asyncio.create_task(self.download_image(session, url, filename))
                tasks.append(task)
            await asyncio.gather(*tasks)

    def download_images(self):
        os.makedirs("temp", exist_ok=True)

        # запрос количества картинок у пользователя
        n_images, ok = QInputDialog.getInt(self, "Download Images", "How many images do you want to download?", 10, 1,
                                           100)
        if not ok:
            return

        urls = []
        # запрос ссылок на изображения у пользователя
        for i in range(n_images):
            url, ok = QInputDialog.getText(self, f"Download Images ({i + 1}/{n_images})",
                                           f"Enter URL for image {i + 1}")
            if not ok:
                return
            urls.append(url.strip())

        # скачивание изображений
        asyncio.run(self.download_images_async(urls))

    def start(self):
        print("start")

    def import_settings(self):
        with open("src/settings.json", "r") as file:
            self.store = json.load(file)
        self.update()

    def update(self):
        self.lineEditText.setText(self.store["text"])

    def export_settings(self):
        self.store["text"] = self.lineEditText.text()

        with open("src/settings1.json", "w") as file:
            json.dump(self.store, file)

    def how_many_images(self):
        value = self.spinBoxDelayHowMany.value()
        return value

    def webcam(self):
        self.cam = cv2.VideoCapture(0)
        self.label = QLabel(self)
        self.label.resize(640, 480)
        self.label.move(20, 60)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.show_frame)
        self.timer.start(1)

    def show_frame(self):
        _, frame = self.cam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        gesture = self.detect_hand_gesture(frame)

        if gesture == "ok":
            self.setStyleSheet("background-color: red")

        qimg = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], frame.shape[1] * 3, QtGui.QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(qimg))

    def detect_hand_gesture(self, frame):
        return "ok"


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uic.ui', self)

        self.pause = False

        self.setWindowTitle("My App")
        self.setWindowIcon(QtGui.QIcon("./src/images/icon.png"))
        # self.setStyle()
        self.resize(1280, 720)
        self.setMinimumSize(640, 480)
        self.setMaximumSize(1920, 1080)

        self.button1 = QtWidgets.QPushButton("старт")
        self.button2 = QtWidgets.QPushButton("стоп")
        self.button1.clicked.connect(self.start)
        self.button2.clicked.connect(self.stop)

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.button1, 0, 0)
        layout.addWidget(self.button2, 1, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def start(self):
        self.pause = False
        new_thread = threading.Thread(target=self.click)
        new_thread.start()

    def stop(self):
        self.pause = True

    def click(self):
        print("started")
        time.sleep(2.5)
        while not self.pause:
            print("action\n")
            time.sleep(2.0)
        print("stopped")
        pass

    @staticmethod
    def init():
        app = QApplication([])
        window = Ui2()

        window.show()
        app.exec()


if __name__ == "__main__":
    Ui.init()


