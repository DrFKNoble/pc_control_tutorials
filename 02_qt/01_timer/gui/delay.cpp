#include "delay.h"

Delay::Delay(QObject *parent) : QObject(parent)
{
    timer = new QTimer();

    QObject::connect(timer, SIGNAL(timeout()), this, SLOT(slot_timerElapsed()));

    return;
}

void Delay::start(const float &time)
{
    qDebug() << "Timer Started!";

    timer->setSingleShot(true);
    timer->start(time);

    return;
}

void Delay::slot_startTimer(const float &time)
{
    start(time);

    return;
}

void Delay::slot_timerElapsed()
{
    qDebug() << "Timer Elapsed!";

    emit sig_quit();

    return;
}
