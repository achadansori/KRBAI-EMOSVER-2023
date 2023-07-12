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
    int iLowH = 83;
    int iHighH = 179;

    int iLowS = 0;
    int iHighS = 255;

    int iLowV = 0;
    int iHighV = 73;

    VideoCapture cap(0);
    cap.set(CAP_PROP_FRAME_WIDTH, 320);
    cap.set(CAP_PROP_FRAME_HEIGHT, 240);

    elementEro = getStructuringElement(MORPH_CROSS, Size(kernelEro, kernelEro));
    elementDil = getStructuringElement(MORPH_CROSS, Size(kernelDil, kernelDil));

    while (true)
    {
        cap.read(imgOriginal);

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
            }
        }

        // Center of Single Object
        Moments m = moments(imgShape, true);
        Point pc(m.m10 / m.m00, m.m01 / m.m00);

        // UAV Movement
        pwm = ((m.m10 / m.m00) / 320) * 100;
        //int mappedValue = ((int)pwm * (2000 - 1000) / 100) + 1000;
        int mappedValue = ((100 - (int)pwm) * (2000 - 1000) / 100) + 1000;
        int switchedValue = 2000 - mappedValue + 1000;
        if (std::isnan((m.m10 / m.m00)) == true) {
            switchedValue = 1500;
        }
        std::cout << switchedValue << std::endl;
    }
    return 0;
}
