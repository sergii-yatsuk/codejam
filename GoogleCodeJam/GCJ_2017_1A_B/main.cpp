#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <fstream>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <iomanip>
#include <array>
#include <cmath>
#include <limits>
#include <cassert>
#include <math.h>
#include <memory.h>

//#pragma comment(linker, "/STACK:134217728")

using namespace std;
using namespace tr1;

#define all(c) (c).begin(), (c).end()
#define CLEAR(x) memset(x,0,sizeof x)

typedef long long ll;
typedef unsigned long long ull;

void solve(int test)
{
   printf("Case #%d: ", test + 1);
   int N;
   int P;
   cin >> N;
   cin >> P;
   vector<int> R(N);
   vector<vector<int>> Q(N, vector<int>(P));
   vector<vector<double>> Qf(N, vector<double>(P));

   for (size_t i = 0; i < N; ++i) {
      cin >> R[i];
   }

   for (size_t i = 0; i < N; ++i) {
      for (size_t j = 0; j < P; ++j) {
         cin >> Q[i][j];

         Qf[i][j] = double(Q[i][j]) / R[i];
      }
   }

   vector<vector<bool>> Qused(N, vector<bool>(P, false));

/*   for (auto & a : Qf) {
      sort(a.begin(), a.end());
   }*/
   int result = 0;

   for (size_t j = 0; j < P; ++j) {
      vector<int> usedPacks(N,0);
      usedPacks[0] = j;
      double avr = Qf[0][j];
      for (size_t i = 1; i < N; ++i) {
         int minK = 0;
         for (size_t k = 0; k < P; ++k) {
            if (!Qused[i][k] && abs(Qf[i][k] - avr) < abs(Qf[i][minK] - avr)) {
               minK = k;
            }
         }
         usedPacks[i] = minK;
         avr = (avr*i + Qf[i][minK]) / (i + 1);
      }
      // check usedPack
      vector<double> usedF(N, 0);
//      int avrI = int (Qf[0][usedPacks[0]]);
      for (size_t i = 0; i < N; ++i) {
         usedF[i] = Qf[i][usedPacks[i]];
 //        if (abs(int(usedF[i]) - avr) < abs(avrI - avr) ){
 //           avrI = int(usedF[i]);
         //}
      }
      bool good = true;
      for (size_t i = 0; i < N; ++i) {
         int usedIntUp = int(usedF[i]*1.1);
         int usedIntDown = int(usedF[i] * 0.9);
         if (usedIntUp > avr|| usedIntDown < avr) {
            good = false;
            break;
         }
      }

      if (good) {
         ++result;
         for (size_t i = 0; i < N; ++i) {
            Qused[i][usedPacks[i]] = true;
         }
      }

      

   }

   cout << result << '\n';
}

int main()
{
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);

   int tests;
   scanf("%d", &tests);

   for (int test = 0; test < tests; ++test)
   {
      fprintf(stderr, "Solving %d/%d\n", test + 1, tests);
      solve(test);
   }

   return 0;
}
