#include <iostream>
#include <cstdlib>
#include <memory>
#include <vector>
using namespace std;
//stl의 vector를 사용하여 score vector 변수를 국어,영어,수학 성적을 넣고 (Push_back()함수사용) 총점과 평균 구하는 프로그램 작성

int main()
{
    vector<int> score;
    score.push_back(90); //국어
    score.push_back(85); //영어
    score.push_back(95); //수학

    int total = 0;
    for (int i = 0; i < score.size(); i++) {
        total += score[i];
    }   
    double average = total / score.size();
    cout << "총점: " << total << endl;
    cout << "평균: " << average << endl;
    
    return 0;
}