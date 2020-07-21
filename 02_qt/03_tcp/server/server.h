#ifndef SERVER_H
#define SERVER_H

#include <QObject>
#include <QTcpSocket>
#include <QTcpServer>

#include <iostream>

class server : public QObject
{
    Q_OBJECT
public:
    explicit server(QObject *parent = nullptr);

public slots:
    void slot_acceptConnection();
    void slot_readMessage();

private:
    QTcpSocket *socket;
    QTcpServer *messageServer;

signals:
    void sig_quit();

};

#endif // SERVER_H
