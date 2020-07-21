#include "serial.h"

serial::serial(QObject *parent) : QObject(parent)
{
    serialPort = new QSerialPort();

    connect(serialPort, SIGNAL(bytesWritten(qint64)), this, SLOT(slot_messageWritten()));

    return;
}

void serial::open(const QString &name)
{

    serialPort->setPortName(name);
    serialPort->setBaudRate(115200);
    serialPort->setDataBits(QSerialPort::Data8);
    serialPort->setParity(QSerialPort::NoParity);
    serialPort->setStopBits(QSerialPort::OneStop);

    if (!serialPort->isOpen())
    {
        serialPort->close();
    }

    serialPort->open(QIODevice::ReadWrite);

    return;
}

void serial::write(const QString &message)
{

    std::cout << "Message: " << message.toStdString() << std::endl;

    int bytesWritten = serialPort->write(message.toUtf8());

    std::cout << "Bytes written: " << bytesWritten << std::endl;

    return;
}

void serial::slot_messageWritten()
{

    serialPort->close();

    emit sig_quit();

    return;
}
