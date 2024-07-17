import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
import plotly.graph_objects as go

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plotly Horizontal Bar Chart")
        self.setGeometry(100, 100, 800, 600)

        # Create the plot
        fig = go.Figure(go.Bar(
            y=['Category A', 'Category B', 'Category C', 'Category D', 'Category E','Category B','Category B','Category B','Category B','Category B','Category B','Category B','Category B','Category B','Category B','Category B','Category B','Category B','Category B','Category B','Category B','Category B','Category B','Category B'],
            x=[20, 14, 23, 25, 22,22,33,44,55,66,77,88,99,13,23,42,42,42,52,52,52,42,3,2,3],
            orientation='h'
        ))

        fig.update_layout(
            title='Sample Horizontal Bar Chart',
            xaxis_title='Value',
            yaxis_title='Category'
        )

        # Convert the plot to HTML
        html = fig.to_html(include_plotlyjs='cdn')

        # Create a QWebEngineView to display the plot
        view = QWebEngineView()
        view.setHtml(html)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(view)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())