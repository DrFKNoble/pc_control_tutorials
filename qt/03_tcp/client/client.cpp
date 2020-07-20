#include "client.h"

client::client(QObject *parent) : QObject(parent)
{
    socket = new QTcpSocket();

    QObject::connect(socket, SIGNAL(connected()), this, SLOT(slot_onConnection()));
    QObject::connect(socket, SIGNAL(bytesWritten(qint64)), this, SLOT(slot_messageWritten()));

    return;
}

void client::open(const QString &ipAddress, const int &port)
{
    socket->connectToHost(ipAddress, port);

    return;
}

void client::write(const QString &message)
{
    std::cout << "Message: " << message.toStdString() << std::endl;

    int bytesWritten = socket->write(message.toUtf8());

    std::cout << "Bytes written: " << bytesWritten << std::endl;

    return;
}

void client::slot_onConnection()
{
    std::cout << "Connected to host." << std::endl;

    return;
}

void client::slot_messageWritten()
{
    socket->close();

    emit sig_quit();

    return;
}
