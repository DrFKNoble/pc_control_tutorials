#ifndef DELAY_H
#define DELAY_H

#include <QObject>

class delay : public QObject
{
    Q_OBJECT
public:
    explicit delay(QObject *parent = nullptr);

signals:

};

#endif // DELAY_H
