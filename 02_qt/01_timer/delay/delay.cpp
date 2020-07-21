#include "delay.h"

delay::delay(QObject *parent) : QObject(parent)
{
    timer = new QTimer();

    connect(timer, SIGNAL(timeout()), this, SLOT(slot_timerElapsed()));

    return;
}

void delay::start(const float &time)
{
    std::cout << "Timer Started" << std::endl;

    timer->setSingleShot(true);
    timer->start(time);

    return;
}

void delay::slot_timerElapsed()
{
    std::cout << "Timer Elapsed" << std::endl;

    emit sig_quit();

    return;
}

