#include "doubleslider.h"

#include <QtDebug>

DoubleSlider::DoubleSlider(QWidget *parent) : QStackedWidget(parent)
{
    _mouseMoving = false;
    _decimals = 2;
    _minimum = 0;
    _maximum = 100;
    _value = 0;

    setSizePolicy(QSizePolicy::Expanding,QSizePolicy::Preferred);
    slider = new SimpleSlider(this);

    spinBox = new QDoubleSpinBox(this);
    spinBox->setMinimum(0);
    spinBox->setMaximum(100);

    addWidget(slider);
    addWidget(spinBox);

    connect(spinBox,SIGNAL(editingFinished()),this,SLOT(setSliderMode()));
    connect(spinBox,SIGNAL(editingFinished()),this,SLOT(setSliderMode()));
    connect(spinBox,SIGNAL(valueChanged(double)),this,SLOT(setValue(double)));
    connect(slider,SIGNAL(valueChanged(int)),this,SLOT(setValue(int)));
}

void DoubleSlider::setEditMode()
{
    setCurrentIndex(1);
}

void DoubleSlider::setSliderMode()
{
    setCurrentIndex(0);
}

double DoubleSlider::value() const
{
    return _value;
}

void DoubleSlider::setValue(double value)
{
    slider->setValue(value);
    spinBox->setValue(value);
    _value = value;
    updateText();
    emit valueChanged(_value);
}

void DoubleSlider::setValue(int value)
{
    slider->setValue(value);
    spinBox->setValue(value);
    _value = value;
    updateText();
    emit valueChanged(_value);
}

int DoubleSlider::decimals() const
{
    return _decimals;
}

void DoubleSlider::setDecimals(int decimals)
{
    spinBox->setDecimals(decimals);
    _decimals = decimals;
}

void DoubleSlider::updateText()
{
    int v = _value;
    double d = _value - v;
    slider->setFormat(_prefix + "%v." + QString::number(d).right(_decimals) + _suffix);
}

QString DoubleSlider::suffix() const
{
    return _suffix;
}

void DoubleSlider::setSuffix(const QString &suffix)
{
    spinBox->setPrefix(suffix);
    _suffix = suffix;
    updateText();
}

QString DoubleSlider::prefix() const
{
    return _prefix;
}

void DoubleSlider::setPrefix(const QString &prefix)
{
    spinBox->setPrefix(prefix);
    _prefix = prefix;
    updateText();
}

double DoubleSlider::minimum() const
{
    return _minimum;
}

void DoubleSlider::setMinimum(double minimum)
{
    spinBox->setMinimum(minimum);
    slider->setMinimum(minimum);
    _minimum = minimum;
}

double DoubleSlider::maximum() const
{
    return _maximum;
}

void DoubleSlider::setMaximum(double maximum)
{
    spinBox->setMaximum(maximum);
    slider->setMaximum(maximum);
    _maximum = maximum;
}

void DoubleSlider::mouseMoveEvent(QMouseEvent *event)
{
    _mouseMoving = true;
    event->ignore();
}

void DoubleSlider::mouseReleaseEvent(QMouseEvent *event)
{
    if (!_mouseMoving)
    {
        setEditMode();
        event->accept();
    }
    else
    {
        _mouseMoving = false;
        event->ignore();
    }
}
