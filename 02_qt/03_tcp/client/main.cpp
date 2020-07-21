#include <QCoreApplication>
#include <QObject>

#include "client.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    client *c = new client();

    QObject::connect(c, SIGNAL(sig_quit()), &a, SLOT(quit()));

    c->open("127.0.0.1", 9601);

    c->write("Hello World!");

    return a.exec();
}
