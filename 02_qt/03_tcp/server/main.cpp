#include <QCoreApplication>
#include <QObject>

#include "server.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    server *s = new server;

    QObject::connect(s, SIGNAL(sig_quit()), &a, SLOT(quit()));

    return a.exec();
}
