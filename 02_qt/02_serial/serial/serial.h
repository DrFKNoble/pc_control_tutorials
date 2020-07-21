#ifndef SERIAL_H
#define SERIAL_H

#include <iostream>

#include <QObject>
#include <QSerialPort>

class serial : public QObject
{
    Q_OBJECT
public:
    explicit serial(QObject *parent = nullptr);

    void open(const QString &name);
    void write(const QString &message);

public slots:
    void slot_messageWritten();

private:
    QSerialPort *serialPort;

signals:
    void sig_quit();
};

#endif // SERIAL_H
