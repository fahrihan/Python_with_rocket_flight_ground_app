import folium
import sys
import io
import folium  # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine

enlem = 39.7
boylam = 39.851138



class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Folium in PyQt Example')
        self.window_width, self.window_height = 300, 300
        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        m = folium.Map(location=[enlem, boylam],
                       zoom_start=20)

        folium.Marker(location=[enlem, boylam],
                      tooltip='Roket'
                      ).add_to(m)

        # dosyayı kaydediyoruz bunu Qweb ile açıcaz
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')

    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')