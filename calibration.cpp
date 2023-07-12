#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
using namespace cv;

int main()
{
    Mat imgOriginal, kernel1, imgColor, imgShape;
    Mat sharpeningKernel = (Mat_<double>(3, 3) << 0, -1, 0, -1, 5, -1, 0, -1, 0);
    Mat elementEro;
    Mat elementDil;

    vector<vector<Point>> contours;
    vector<Vec4i> hierarchy;
    string objPoints;

    int objCorner, ThreshLow = 30, ThreshHigh = 90;
    int area, areaMin = 1000, kernelDillate = 1, BlurLevel = 3;
    int kernelDil = 1, kernelEro = 1;
    float pwm;
    double perimeter;
    int iLowH = 0;
    int iHighH = 179;

    int iLowS = 0;
    int iHighS = 112;

    int iLowV = 0;
    int iHighV = 199;

    // Create Trackbar for Shapes Detection
    namedWindow("Shape Detect", (100, 200));
    createTrackbar("ThreshLow", "Shape Detect", &ThreshLow, 255);
    createTrackbar("ThreshHigh", "Shape Detect", &ThreshHigh, 255);
    createTrackbar("AreaMin", "Shape Detect", &areaMin, 50000);
    createTrackbar("KernelDillate", "Shape Detect", &kernelDillate, 5);
    createTrackbar("BlurLevel", "Shape Detect", &BlurLevel, 5);

    // Create Trackbar for Colors Detection
    namedWindow("Color Detect", (100, 200));
    createTrackbar("LowH", "Color Detect", &iLowH, 179);
    createTrackbar("HighH", "Color Detect", &iHighH, 179);
    createTrackbar("LowS", "Color Detect", &iLowS, 255);
    createTrackbar("HighS", "Color Detect", &iHighS, 255);
    createTrackbar("LowV", "Color Detect", &iLowV, 255);
    createTrackbar("HighV", "Color Detect", &iHighV, 255);

    VideoCapture cap(0);
    cap.set(CAP_PROP_FRAME_WIDTH, 320);
    cap.set(CAP_PROP_FRAME_HEIGHT, 240);

    elementEro = getStructuringElement(MORPH_CROSS, Size(kernelEro, kernelEro));
    elementDil = getStructuringElement(MORPH_CROSS, Size(kernelDil, kernelDil));

    while (true)
    {
        cap.read(imgOriginal);
        //flip(imgOriginal,imgOriginal,-1);
        
        //  Color Detect
        cvtColor(imgOriginal, imgColor, COLOR_BGR2HSV);
        inRange(imgColor, Scalar(iLowH, iLowS, iLowV), Scalar(iHighH, iHighS, iHighV), imgColor);

        // morphological opening (remove small objects from the foreground)
        erode(imgColor, imgColor, elementEro);
        dilate(imgColor, imgColor, elementDil);

        // morphological closing (fill small holes in the foreground)
        dilate(imgColor, imgColor, elementDil);
        erode(imgColor, imgColor, elementEro);

        // shape
        blur(imgColor, imgColor, Size(BlurLevel, BlurLevel));
        Canny(imgColor, imgShape, ThreshLow, ThreshHigh); // make image edge

        // Mempertebal image edge
        kernel1 = getStructuringElement(MORPH_CROSS, Size(kernelDillate, kernelDillate)); // size() digunakan utk mengatur ketebalan edge
        dilate(imgShape, imgShape, kernel1);

        // find the contours
        findContours(imgShape, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE);

        // Filter the image from image noise so it wont draw the contours and draw the countours
        vector<vector<Point>> conPoly(contours.size());
        vector<Rect> boundRect(contours.size());
        for (int i = 0; i < contours.size(); i++)
        {
            area = contourArea(contours[i]); // hitung area masing-masing countours
            // only draw the contours if the area > 1000
            if (area > areaMin)
            {
                perimeter = arcLength(contours[i], true);                      // menghitung panjang sisi dari kontur
                approxPolyDP(contours[i], conPoly[i], 0.01 * perimeter, true); // Menghitung perkiraan jumlah sisi
                boundRect[i] = boundingRect(conPoly[i]);                       // draw rectangular border in every object

                objCorner = (int)conPoly[i].size();
                objPoints = to_string(objCorner);

                // draw contours based on approxPolyDP
                //drawContours(imgOriginal, conPoly, i, Scalar(128, 0, 128), 3);

                // draw rectangular border in every object
                //rectangle(imgOriginal, boundRect[i].tl(), boundRect[i].br(), Scalar(0, 255, 0), 3);

                // put text based on objType in the image
                //putText(imgOriginal, "Object Points : " + objPoints, {boundRect[i].x, boundRect[i].y - 5}, FONT_HERSHEY_DUPLEX, 0.5, Scalar(0, 0, 0), 2);
            }
        }

        // Center of Single Object
        Moments m = moments(imgShape, true);
        Point pc(m.m10 / m.m00, m.m01 / m.m00);
        Point centerLine(imgShape.size().width / 2, imgShape.size().height / 2);
        circle(imgShape, pc, 30, Scalar(56, 28, 30), -1);

        // draw middle line
        Point p1(imgShape.size().width / 2 + 15, 0), p2(imgShape.size().width / 2 + 15, imgShape.size().height);
        line(imgOriginal, p1, p2, Scalar(0, 0, 255), 2);

        // draw middle line
        Point p3(imgShape.size().width / 2 - 15, 0), p4(imgShape.size().width / 2 - 15, imgShape.size().height);
        line(imgOriginal, p3, p4, Scalar(0, 0, 255), 2);

        // draw line from mid line to object center
        line(imgOriginal, centerLine, pc, Scalar(128, 0, 255), 2);

        // UAV Movement
        pwm = ((m.m10 / m.m00) / 320) * 100;
        int mappedValue = ((int)pwm * (2000 - 1000) / 100) + 1000;
        std::cout << mappedValue << std::endl;

        imshow("Colors Detect", imgColor);
        imshow("Original Image", imgOriginal);
        waitKey(1);
    }
}
