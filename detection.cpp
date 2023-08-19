#include <opencv2/opencv.hpp>

cv::Point detectBallColor(cv::Mat frame, cv::Scalar lowerColor, cv::Scalar upperColor) {
    cv::Mat hsv;
    cv::cvtColor(frame, hsv, cv::COLOR_BGR2HSV);
    cv::Mat mask;
    cv::inRange(hsv, lowerColor, upperColor, mask);
    std::vector<std::vector<cv::Point>> contours;
    cv::findContours(mask, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

    cv::Point ballCenter(-1, -1);

    for (const auto& contour : contours) {
        double area = cv::contourArea(contour);
        if (area > 100) {
            cv::Moments moment = cv::moments(contour);
            if (moment.m00 != 0) {
                ballCenter.x = static_cast<int>(moment.m10 / moment.m00);
                ballCenter.y = static_cast<int>(moment.m01 / moment.m00);
                cv::drawContours(frame, std::vector<std::vector<cv::Point>>{contour}, -1, cv::Scalar(0, 255, 0), 2);
                cv::circle(frame, ballCenter, 5, cv::Scalar(0, 255, 0), -1);
                break;
            }
        }
    }

    return ballCenter;
}

int main() {
    cv::VideoCapture cap(0);  // Change device number if needed

    cv::namedWindow("Lane Detection");

    int hMinRed = 0;
    int hMaxRed = 10;
    int hMinGreen = 35;
    int hMaxGreen = 85;

    cv::createTrackbar("H Min (Red)", "Lane Detection", &hMinRed, 180, nullptr);
    cv::createTrackbar("H Max (Red)", "Lane Detection", &hMaxRed, 180, nullptr);
    cv::createTrackbar("H Min (Green)", "Lane Detection", &hMinGreen, 180, nullptr);
    cv::createTrackbar("H Max (Green)", "Lane Detection", &hMaxGreen, 180, nullptr);

    while (true) {
        cv::Mat frame;
        cap.read(frame);

        cv::Mat hsv;
        cv::cvtColor(frame, hsv, cv::COLOR_BGR2HSV);

        cv::Scalar redLower(hMinRed, 100, 100);
        cv::Scalar redUpper(hMaxRed, 255, 255);
        cv::Scalar greenLower(hMinGreen, 100, 100);
        cv::Scalar greenUpper(hMaxGreen, 255, 255);

        cv::Point redCenter = detectBallColor(frame, redLower, redUpper);
        cv::Point greenCenter = detectBallColor(frame, greenLower, greenUpper);

        if (redCenter.x != -1 && greenCenter.x != -1) {
            cv::line(frame, redCenter, greenCenter, cv::Scalar(0, 0, 255), 2);

            if (redCenter.x < greenCenter.x) {
                cv::putText(frame, "Kiri", cv::Point(10, 30), cv::FONT_HERSHEY_SIMPLEX, 1, cv::Scalar(0, 0, 255), 2);
            } else if (redCenter.x > greenCenter.x) {
                cv::putText(frame, "Kanan", cv::Point(10, 30), cv::FONT_HERSHEY_SIMPLEX, 1, cv::Scalar(0, 0, 255), 2);
            }
        }

        cv::imshow("Lane Detection", frame);

        if (cv::waitKey(1) & 0xFF == 'q') {
            break;
        }
    }

    cap.release();
    cv::destroyAllWindows();

    return 0;
}
