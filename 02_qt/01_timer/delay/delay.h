#ifndef DELAY_H
#define DELAY_H

#include <iostream>

#include <QObject>
#include <QTimer>

class delay : public QObject
{
    Q_OBJECT
public:
    explicit delay(QObject *parent = nullptr);

    void start(const float &time);

public slots:
    void slot_timerElapsed();

private:
    QTimer *timer;

signals:
    void sig_quit();

};

#endif // DELAY_H
