
#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

#include <iostream>
#include <stdio.h>

using namespace std;
using namespace cv;


String face_cascade_name = "/home/ahmad/opencv/data/haarcascades/haarcascade_frontalface_alt.xml";

vector<Mat*> detect_faces( Mat frame )
{
    CascadeClassifier face_cascade;
    vector<Mat*> cropped_faces;

    if( !face_cascade.load( face_cascade_name ) ) { cout << "Error loading face cascade file\n" << endl; return cropped_faces;  };
    vector<Rect> faces;
    Mat frame_gray;
    Mat* crop = nullptr;
    cvtColor( frame, frame_gray, COLOR_BGR2GRAY );
    equalizeHist( frame_gray, frame_gray );

    face_cascade.detectMultiScale( frame_gray, faces, 1.1, 2, 0, Size(30, 30) );

    for( size_t i = 0; i < faces.size(); i++ )
    {

        Rect rect(faces[0].x , faces[0].y - ( 0.8 * faces[i].height ) , faces[i].width, faces[i].height + 0.5 * faces[i].height );
//        Rect rect(faces[0].x -50 , faces[0].y - 100 , 300, 300 );

        rectangle(frame, rect, Scalar(255, 255, 255), 4, 8);

        if (rect.height + rect.y > frame.rows || rect.width + rect.x > frame.cols || rect.x < 0 || rect.y < 0||  rect.height < 0 || rect.width < 0)
        {
            continue;
        }

        Mat cropped  = frame(rect);
        crop = new Mat(cropped);

        cropped_faces.push_back(crop);
    }

    return cropped_faces;
}



double check_helmet(Mat* head)
{
    Mat frame = *head;
    cv::imshow("src", frame);

    Mat hsv, mask1;
    cvtColor(frame, hsv, COLOR_BGR2HSV);

    inRange(hsv, Scalar(25, 120, 80), Scalar(100, 255, 255), mask1);
//    cout<<"src"<<endl;

    double image_size = frame.cols*frame.rows;
    double green_percent = ((double) cv::countNonZero(mask1))/image_size;
//    cout << green_percent << endl;

    if(green_percent < 0.05)
    {
        cout << "head with no helmet" << endl;
        cout << green_percent << endl;
        return green_percent;
    }

    cv::imshow("mask1", mask1);
    cout << "detected" << endl;
    cout << green_percent << endl;

    return green_percent;
}


int main( int argc, const char** argv )
{
    VideoCapture capture(0);
    Mat frame, prevFrame;

    while( true )
    {
        capture >> frame;
        float downsampleFactor = 1;
        resize(frame, frame, Size(), downsampleFactor, downsampleFactor, INTER_NEAREST);

        if( !frame.empty() )
        {

             vector<Mat*> cropped_images = detect_faces(frame);
             if (cropped_images.empty())
             {
                 cout << "no face detected !!! " << endl;

                 continue;
             }
//             cout << cropped_images.size() << endl;
             for(Mat* crop:cropped_images)
             {
                 if(crop != nullptr)
                 {
                     check_helmet(crop);
                     free(crop);
                 }
             }

        }

        else
        {
            cout << "No captured frame. Stopping!" << endl;
            break;
        }

        int c = waitKey(10);
        if( (char)c == 27 ) { break; }
    }

    capture.release();

    return 0;
}

