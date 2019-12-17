#include <QCoreApplication>
#include<QJsonObject>
#include<QJsonDocument>
#include<QFile>
#include<QBuffer>

#include"worker.h"

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    Worker worker;

    QJsonObject jObj;

    QFile fileImg("source_2.jpg");

    fileImg.open(QIODevice::ReadOnly);
    QByteArray imageData = fileImg.readAll();
    QByteArray imageData_Base64 = imageData.toBase64();

    QString imgdata(imageData_Base64);

    jObj.insert("image",QJsonValue::fromVariant(imgdata));
    jObj.insert("Kammel",QJsonValue::fromVariant("HI "));
    QJsonDocument doc(jObj);
    worker.post("http://10.144.66.31:5000",doc.toJson());

    return a.exec();
}
