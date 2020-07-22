#ifndef DELAY_H
#define DELAY_H

#include <QDebug>
#include <QObject>
#include <QTimer>

class Delay : public QObject
{
    Q_OBJECT
public:
    explicit Delay(QObject *parent = nullptr);

    void start(const float &time);

signals:
   void sig_quit();

public slots:
    void slot_startTimer(const float &time);

private slots:
    void slot_timerElapsed();

private:
    QTimer *timer;

};

#endif // DELAY_H
