#include <QCoreApplication>
#include <QObject>

#include "delay.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    delay *d = new delay();

    QObject::connect(d, SIGNAL(sig_quit()), &a, SLOT(quit()));

    d->start(1000);

    return a.exec();
}
