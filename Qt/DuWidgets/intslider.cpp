#include "intslider.h"

#include <QtDebug>

IntSlider::IntSlider(QWidget *parent)
    : QStackedWidget(parent)
{
    _mouseMoving = false;
    _minimum = 0;
    _maximum = 100;
    _value = 0;

    setSizePolicy(QSizePolicy::Expanding,QSizePolicy::Preferred);
    slider = new SimpleSlider(this);

    spinBox = new QSpinBox(this);
    spinBox->setMinimum(0);
    spinBox->setMaximum(100);

    addWidget(slider);
    addWidget(spinBox);

    connect(spinBox,SIGNAL(editingFinished()),this,SLOT(setSliderMode()));
    connect(spinBox,SIGNAL(valueChanged(int)),this,SLOT(setValue(int)));
    connect(slider,SIGNAL(valueChanged(int)),this,SLOT(setValue(int)));
}

void IntSlider::setEditMode()
{
    setCurrentIndex(1);
}

void IntSlider::setSliderMode()
{
    setCurrentIndex(0);
}

int IntSlider::value() const
{
    return _value;
}

void IntSlider::setValue(int value)
{
    spinBox->setValue(value);
    slider->setValue(value);
    _value = value;
    emit valueChanged(_value);
}

QString IntSlider::suffix() const
{
    return _suffix;
}

void IntSlider::setSuffix(const QString &suffix)
{
    spinBox->setPrefix(suffix);
    slider->setFormat(_prefix + "%v" + suffix);
    _suffix = suffix;
}

QString IntSlider::prefix() const
{
    return _prefix;
}

void IntSlider::setPrefix(const QString &prefix)
{
    spinBox->setPrefix(prefix);
    slider->setFormat(prefix + "%v" + _suffix);
    _prefix = prefix;
}

int IntSlider::maximum() const
{
    return _maximum;
}

void IntSlider::setMaximum(int maximum)
{
    spinBox->setMaximum(maximum);
    slider->setMaximum(maximum);
    _maximum = maximum;
}

int IntSlider::minimum() const
{
    return _minimum;
}

void IntSlider::setMinimum(int minimum)
{
    spinBox->setMinimum(minimum);
    slider->setMinimum(minimum);
    _minimum = minimum;
}

void IntSlider::mouseMoveEvent(QMouseEvent *event)
{
    _mouseMoving = true;
    event->ignore();
}

void IntSlider::mouseReleaseEvent(QMouseEvent *event)
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
