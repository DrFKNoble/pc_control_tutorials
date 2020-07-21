#ifndef CLIENT_H
#define CLIENT_H

#include <QObject>
#include <QTcpSocket>

#include <iostream>

class client : public QObject
{
    Q_OBJECT
public:
    explicit client(QObject *parent = nullptr);

    void open(const QString &ipAddress, const int &port);
    void write(const QString &message);

public slots:
    void slot_onConnection();
    void slot_messageWritten();

private:
    QTcpSocket *socket;

signals:
    void sig_quit();
};

#endif // CLIENT_H
