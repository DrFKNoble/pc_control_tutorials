#ifndef DELAY_H
#define DELAY_H

#include <QObject>

class Delay : public QObject
{
    Q_OBJECT
public:
    explicit Delay(QObject *parent = nullptr);

signals:

};

#endif // DELAY_H
