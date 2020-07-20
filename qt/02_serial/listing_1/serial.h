#ifndef SERIAL_H
#define SERIAL_H

#include <QObject>

class serial : public QObject
{
    Q_OBJECT
public:
    explicit serial(QObject *parent = nullptr);

signals:

};

#endif // SERIAL_H
