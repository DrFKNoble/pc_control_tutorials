#include "mainwindow.h"
#include "delay.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;

    Delay *d = new Delay();

    QObject::connect(&w, SIGNAL(sig_startButton_clicked(const float &)), d, SLOT(slot_startTimer(const float &)));
    QObject::connect(d, SIGNAL(sig_quit()), &a, SLOT(quit()));

    w.show();
    return a.exec();
}
