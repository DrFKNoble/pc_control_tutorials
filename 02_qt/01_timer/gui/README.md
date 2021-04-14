# Timer Project GUI

## main.cpp

```cpp
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
```

## delay.h

```cpp
#ifndef DELAY_H
#define DELAY_H

#include <QDebug>
#include <QObject>
#include <QTimer>

class Delay : public QObject
{
    Q_OBJECT
public:
    explicit Delay(QObject *parent = nullptr);

    void start(const float &time);

signals:
   void sig_quit();

public slots:
    void slot_startTimer(const float &time);

private slots:
    void slot_timerElapsed();

private:
    QTimer *timer;

};

#endif // DELAY_H
```

## delay.cpp

```cpp
#include "delay.h"

Delay::Delay(QObject *parent) : QObject(parent)
{
    timer = new QTimer();

    QObject::connect(timer, SIGNAL(timeout()), this, SLOT(slot_timerElapsed()));

    return;
}

void Delay::start(const float &time)
{
    qDebug() << "Timer Started!";

    timer->setSingleShot(true);
    timer->start(time);

    return;
}

void Delay::slot_startTimer(const float &time)
{
    start(time);

    return;
}

void Delay::slot_timerElapsed()
{
    qDebug() << "Timer Elapsed!";

    emit sig_quit();

    return;
}
```

## mainwindow.h

```cpp
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

signals:
    void sig_startButton_clicked(const float &time);

private slots:
    void on_actionQuit_triggered();

    void on_startButton_clicked();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
```

## mainwindow.cpp

```cpp
#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_actionQuit_triggered()
{
    QApplication::quit();
}

void MainWindow::on_startButton_clicked()
{
    float time = 5000;

    emit sig_startButton_clicked(time);
}
```