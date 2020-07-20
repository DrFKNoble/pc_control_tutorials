#include <QCoreApplication>
#include <QObject>

#include "serial.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    serial *s = new serial();

    QObject::connect(s, SIGNAL(sig_quit()), &a, SLOT(quit()));

    s->open("COM3");

    s->write("Hello World!");

    return a.exec();
}
