#importing important libraries
import numpy as np 
import pandas as pd 
import pyqtgraph as pg# from pyqtgraph import GraphicsLayoutWidget, PlotWidget 
import sys
from pyqtgraph import GraphicsLayoutWidget
# Libraries for boxplot 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
#Pyqt libraries 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_ACPC(object):
    #initial variables 
    def __init__(self):
        self.file_location = '' 
        self.data_df = pd.DataFrame()
        self.plot = pg.GraphicsLayoutWidget(show=True)
        self.all_header_list =[]
        self.color_code_column_name = []
        self.color_code_dict = {}
        self.attribute_list = [] 
        self.comboboxfilled = False
    
    
    def setupUi(self, ACPC):
        ACPC.setObjectName("ACPC")
        ACPC.resize(1190, 738)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ACPC.sizePolicy().hasHeightForWidth())
        ACPC.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(ACPC)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainframe.sizePolicy().hasHeightForWidth())
        self.mainframe.setSizePolicy(sizePolicy)
        self.mainframe.setMinimumSize(QtCore.QSize(600, 600))
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mainframe)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Data_Selection_Frame = QtWidgets.QFrame(self.mainframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Data_Selection_Frame.sizePolicy().hasHeightForWidth())
        self.Data_Selection_Frame.setSizePolicy(sizePolicy)
        self.Data_Selection_Frame.setMinimumSize(QtCore.QSize(200, 0))
        self.Data_Selection_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Data_Selection_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Data_Selection_Frame.setObjectName("Data_Selection_Frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Data_Selection_Frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Data_Selection_Title = QtWidgets.QLabel(self.Data_Selection_Frame)
        self.Data_Selection_Title.setTextFormat(QtCore.Qt.AutoText)
        self.Data_Selection_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Data_Selection_Title.setObjectName("Data_Selection_Title")
        self.verticalLayout_2.addWidget(self.Data_Selection_Title)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.Colored_Data_Label = QtWidgets.QLabel(self.Data_Selection_Frame)
        self.Colored_Data_Label.setObjectName("Colored_Data_Label")
        self.verticalLayout_2.addWidget(self.Colored_Data_Label)
        self.Colored_Data_comboBox = QtWidgets.QComboBox(self.Data_Selection_Frame)
        self.Colored_Data_comboBox.setObjectName("Colored_Data_comboBox")
        self.verticalLayout_2.addWidget(self.Colored_Data_comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.Xaxis_Data_Label = QtWidgets.QLabel(self.Data_Selection_Frame)
        self.Xaxis_Data_Label.setObjectName("Xaxis_Data_Label")
        self.verticalLayout_2.addWidget(self.Xaxis_Data_Label)
        self.Xaxis_Data_comboBox = QtWidgets.QComboBox(self.Data_Selection_Frame)
        self.Xaxis_Data_comboBox.setObjectName("Xaxis_Data_comboBox")
        self.verticalLayout_2.addWidget(self.Xaxis_Data_comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.Yaxis_Data_Label = QtWidgets.QLabel(self.Data_Selection_Frame)
        self.Yaxis_Data_Label.setObjectName("Yaxis_Data_Label")
        self.verticalLayout_2.addWidget(self.Yaxis_Data_Label)
        self.Yaxis_Data_comboBox = QtWidgets.QComboBox(self.Data_Selection_Frame)
        self.Yaxis_Data_comboBox.setObjectName("Yaxis_Data_comboBox")
        self.verticalLayout_2.addWidget(self.Yaxis_Data_comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.Plot_Data_pushButton = QtWidgets.QPushButton(self.Data_Selection_Frame)
        self.Plot_Data_pushButton.setObjectName("Plot_Data_pushButton")
        self.verticalLayout_2.addWidget(self.Plot_Data_pushButton)
        self.Legend_Window = GraphicsLayoutWidget(self.Data_Selection_Frame)
        self.Legend_Window.setObjectName("Legend_Window")
        self.verticalLayout_2.addWidget(self.Legend_Window)
        self.gridLayout_2.addWidget(self.Data_Selection_Frame, 0, 0, 1, 1)
        self.Data_Selected_Label = QtWidgets.QLabel(self.mainframe)
        self.Data_Selected_Label.setObjectName("Data_Selected_Label")
        self.gridLayout_2.addWidget(self.Data_Selected_Label, 1, 0, 1, 1)
        self.PlotWindow = GraphicsLayoutWidget(self.mainframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlotWindow.sizePolicy().hasHeightForWidth())
        self.PlotWindow.setSizePolicy(sizePolicy)
        self.PlotWindow.setMinimumSize(QtCore.QSize(550, 550))
        self.PlotWindow.setObjectName("PlotWindow")
        self.gridLayout_2.addWidget(self.PlotWindow, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.mainframe)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.mainframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(300, 600))
        self.widget.setObjectName("widget")
        self.gridLayout_2.addWidget(self.widget, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.mainframe, 0, 0, 1, 1)
        ACPC.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ACPC)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1190, 26))
        self.menubar.setObjectName("menubar")
        self.DATA = QtWidgets.QMenu(self.menubar)
        self.DATA.setObjectName("DATA")
        ACPC.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ACPC)
        self.statusbar.setObjectName("statusbar")
        ACPC.setStatusBar(self.statusbar)
        self.actionLoad_CSV_File = QtWidgets.QAction(ACPC)
        self.actionLoad_CSV_File.setObjectName("actionLoad_CSV_File")
        self.DATA.addAction(self.actionLoad_CSV_File)
        self.menubar.addAction(self.DATA.menuAction())


        self.retranslateUi(ACPC)
        QtCore.QMetaObject.connectSlotsByName(ACPC)
        
        #Adding a Plot to the plotwindow
        self.plot1 = self.PlotWindow.addPlot()
        #main scatterplot used for displaying data 
        self.scatter = pg.ScatterPlotItem(pxMode = True,hoverable = True)
        #Adding a Plot to the Legendwindow
        self.plotlegend = self.Legend_Window.addPlot()
        
        #adding boxplot 
        self.fig = Figure()
        self.ax1 = self.fig.add_subplot(211)
        self.ax2 = self.fig.add_subplot(212)
        self.axes=[self.ax1, self.ax2]
        self.canvas = FigureCanvas(self.fig)

        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, 
                                  QtWidgets.QSizePolicy.Expanding)
        self.canvas.updateGeometry()
        # creating a Vertical Box layout
        self.layout = QtWidgets.QGridLayout(self.widget)
        # adding canvas to the layout
        self.layout.addWidget(self.canvas)
        
        
        
        #connection to load the csv file in: 
        self.actionLoad_CSV_File.triggered.connect(self.loaddata)
        #connection once the colored code 
        self.Colored_Data_comboBox.activated.connect(lambda: self.organizedata(self.all_header_list))
        #connection to plot the data: 
        self.Plot_Data_pushButton.clicked.connect(self.plotdata)
        #connection to when data in the mainplot is selected 
        self.scatter.sigClicked.connect(self.selecteddata)
        #connection to auto update boxplots: 
        self.Xaxis_Data_comboBox.activated.connect(self.updateboxplot)
        self.Yaxis_Data_comboBox.activated.connect(self.updateboxplot)
        

    def retranslateUi(self, ACPC):
        _translate = QtCore.QCoreApplication.translate
        ACPC.setWindowTitle(_translate("ACPC", "ACPC"))
        self.Data_Selection_Title.setText(_translate("ACPC", "Data Selection "))
        self.Colored_Data_Label.setText(_translate("ACPC", "Colored Data:"))
        self.Xaxis_Data_Label.setText(_translate("ACPC", "X-Axis Data:"))
        self.Yaxis_Data_Label.setText(_translate("ACPC", "Y-Axis Data:"))
        self.Plot_Data_pushButton.setText(_translate("ACPC", "Plot Data"))
        self.label.setText(_translate("ACPC", "None"))
        self.Data_Selected_Label.setText(_translate("ACPC", "Data Selected:"))
        self.DATA.setTitle(_translate("ACPC", "DATA"))
        self.actionLoad_CSV_File.setText(_translate("ACPC", "Load CSV File"))

    
    #loading the csv file in 
    def loaddata(self): 
        #getting input for data location 
        file_location = QFileDialog.getOpenFileName(None, 'Open File', 'C:\ ')
        # if file_location input is empty, then load most recent file 
        if file_location == '': 
            file_location = "C:/Users/jonak/OneDrive - University of Calgary/Desktop/Rockyview_Geoservices/Attribute Crossplot Program/Dataset/NTKN facies.csv"
        #storing the file location for future use 
        self.file_location = file_location[0]
        print(file_location[0])
        #loading data as a dataframe
        data_df = pd.read_csv(file_location[0],header=0) #turns data into a dataframe and read the first line as the header 
        #storing dataframe for functional use 
        self.data_df = data_df 
        
        #Determine the number of different attributes, UWI and well_info/parameter 
        header_list = self.data_df.columns.values
        #storing the header columns to organize the data 
        self.all_header_list = header_list
        
        self.popcomboboxes(header_list)
        
    def popcomboboxes(self,header_list):
        self.Colored_Data_comboBox.addItems(header_list)
        
    #method to automatically organize the data: 
    def organizedata(self,header_list): 
        #clearing the colored dictionary: 
        self.color_code_dict = None 
        #Determining which value will be used to color code the data points 
        color_code_column = self.Colored_Data_comboBox.currentText()
        
        self.color_code_column_name = color_code_column 
        #Creating a dictionary to automatically define the color for each value in the color code column 
        color_code_columm_values = self.data_df[color_code_column].values
        print(color_code_columm_values)
        color_code_dict = {}
        ## for each values in the color code column valuues 
        for item in color_code_columm_values:
            ## if color code column values is not in the dictionary keys
            if item not in color_code_dict.keys():
                #create a dictionary key for that value along with a 3 array number from 0 to 250 for color code 
                itemkey = item 
                colorcode = list(np.random.randint(0,250,2))
                color_code_dict[itemkey]=colorcode
            ## else skip to the next line 
        self.color_code_dict = color_code_dict 
        
        
        #Determining which columns are non coordinate values 
        attribute_list = []
        ## for each header column names
        for i in header_list: 
            ## if the name includes UWI,UTMX,UTMY and the color code name is not in the header,
            if 'UWI' not in i and 'UTMX' not in i and 'UTMY' not in i and color_code_column not in i:
                attribute_list.append(i) 
        self.attribute_list = attribute_list
        
        if self.comboboxfilled == False: 
            self.Xaxis_Data_comboBox.addItems(attribute_list)
            self.Yaxis_Data_comboBox.addItems(attribute_list)
        self.comboboxfilled = True
        
        #Want to automatically plot the legends here 
        spots = [] 
        self.plotlegend.clear() 
        self.plotlegend.addLegend() 
        scatter = pg.ScatterPlotItem(pxMode = True)
        #made itemkeys and values earlier in code 
        # for each colorcodekey - create a coordinate key paur 
        xycoord = []
        coord = 0
        '''
        for i in range(len(color_code_dict.keys())): 
            #create an xycord for each item 
            xycoord.append([1,coord])
            coord += 1
        print(xycoord)
        print(color_code_dict.keys())
        print(color_code_dict.values())
        #set the data for the scatterplot 
        scatter.setData(pos=xycoord,data=list(color_code_dict.keys()),brush=list(color_code_dict.values()))
        '''
        spots = []
        #for each dataset row, 
        for i in range(len(color_code_dict.keys())):
            #create a dictionary of items that contains the scatter plot position, size, pen, brush and width) 
            spot_dic = {'pos': (0, coord), 'data': list(color_code_dict.keys()),
                'brush': list(color_code_dict.values())[i]}
            coord +=1
            # adding spot_dic in the list of spots
            spots.append(spot_dic)
        scatter.addPoints(spots)
        self.plotlegend.addItem(scatter)
        
    def plotdata(self):        
        
        #clearing the plot
        self.plot1.clear() 
        self.plot1.addLegend()
        self.scatter.clear()
        
        #getting the current selected attributes: 
        attributex = self.Xaxis_Data_comboBox.currentText()
        attributey = self.Yaxis_Data_comboBox.currentText()
        #getting all UWI,x-data,y-data,colorcodecolumnname,colorcodedictionary
        datax = self.data_df[attributex].values
        datay = self.data_df[attributey].values
        datacolorkey = self.data_df[self.color_code_column_name].values
        dataUWI = self.data_df['UWI'].values
        spots = []
        #for each dataset row, 
        for i in range(len(datax)):
            #create a dictionary of items that contains the scatter plot position, size, pen, brush and width) 
            spot_dic = {'pos': (datax[i], datay[i]), 
                'data' : dataUWI[i], 
                'brush': self.color_code_dict[datacolorkey[i]]}
            # adding spot_dic in the list of spots
            spots.append(spot_dic)
            #creating data needed for each item 
        # adding spots to the scatter plot
        self.scatter.addPoints(spots)
        # adding scatter plot to the plot window
        self.plot1.addItem(self.scatter)
        #Adding Axis labels
        self.plot1.setLabel(axis='left',text=attributey)
        self.plot1.setLabel(axis='bottom',text=attributex)
    
    
    def updateboxplot(self): 
        # Clearing boxplot of data 
        self.ax1.clear()
        self.ax2.clear() 
        #getting the current selected attributes: 
        attributex = self.Xaxis_Data_comboBox.currentText()
        attributey = self.Yaxis_Data_comboBox.currentText()
        #getting all UWI,x-data,y-data,colorcodecolumnname,colorcodedictionary
        datax = self.data_df[attributex].values
        datay = self.data_df[attributey].values
        #removing nan from data 
        datax = datax[np.logical_not(np.isnan(datax))]
        datay = datay[np.logical_not(np.isnan(datay))]
        #plotting the data 
        self.ax1.boxplot(datax)
        self.ax2.boxplot(datay)
        self.axes[0].set_title("datax: "+attributex)
        self.axes[1].set_title("datay: "+attributey)
        #refreshing canvases 
        self.canvas.draw()
        
    def selecteddata(self,obj, points): 
        print('selected point:',obj,points)
    
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ACPC = QtWidgets.QMainWindow()
    ui = Ui_ACPC()
    ui.setupUi(ACPC)
    ACPC.show()
    sys.exit(app.exec_())

    