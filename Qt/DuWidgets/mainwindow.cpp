#include "mainwindow.h"

#include "simpleslider.h"
#include "intslider.h"
#include "doubleslider.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
{
    setupUi(this);

    // SimpleSlider
    mainLayout->insertWidget(0,new QLabel("Simple Slider:"));
    mainLayout->insertWidget(1,new SimpleSlider(this));

    // IntSlider
    mainLayout->insertWidget(2,new QLabel("Int Slider:"));
    mainLayout->insertWidget(3,new IntSlider(this));

    // DoubleSlider
    mainLayout->insertWidget(4,new QLabel("Double Slider:"));
    mainLayout->insertWidget(5,new DoubleSlider(this));
}

